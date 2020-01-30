
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def targyfelvevo(targylista, browser, maximum_time_waiting):

    #vár amíg a fenti menüsáv nem töltődik be (köztük a Tárgyak gomb)

    el = WebDriverWait(browser, maximum_time_waiting).until(lambda browser: browser.find_element_by_id("mb1"))

    # a Tárgyak gombra kattint, utána pedig azonnal a Tárgyfelvételre a lenyíló menüből

    targyak_menu_gomb =browser.find_element_by_xpath("//ul[@id='mb1']/li[3]").click()

    wait = WebDriverWait(browser, 100)

    targyfelvetel_gomb = browser.find_element_by_xpath("//li[@id='mb1_Targyak']/ul/li[3]").click()

    #ez akkor működik jól, ha a szerver számokkal jelöli a szemesztereket (70619 = 2019/20/2)
    #neptun_date_option = browser.find_element_by_xpath("//table[@id = 'upFilter_bodytable']/tbody/tr[1]/td/select/option[@value = 70619]")
    #neptun_date_option.click()

    #megvárja, amíg az adatmazők meg nem jelennek (maga a tábla, ami tartalmazza őket)

    el = WebDriverWait(browser, maximum_time_waiting).until(lambda browser: browser.find_element_by_id("upFilter_bodytable"))

    #ez akkor működik jól, ha mindig az első opció a legfrissebb szemeszter / ami szerintem mindig igaz
    #kiválasztja a legfelső (legfrissebb) félévet

    neptun_date_option = browser.find_element_by_xpath("//table[@id = 'upFilter_bodytable']/tbody/tr[1]/td/select/option[1]")
    neptun_date_option.click()

    time.sleep(0.5)

    #a tárgytípusok között bepipálja a mintatanterv tárgyai opciót (az "egyéb szabadon felvehető tárgyak" helyett)

    mintatanterv_targyak_gomb = browser.find_element_by_xpath("//table[@id = 'upFilter_rbtnSubjectType']/tbody/tr[1]/td/input")
    mintatanterv_targyak_gomb.click()

    time.sleep(0.5)

    #kiválasztja hogy minden tárgy között keressen a kereső (mintatantervek = minden)

    syllabus_option = browser.find_element_by_xpath("//select[@id = 'upFilter_cmbTemplates']/option[@value = 'All']")
    syllabus_option.click()

    time.sleep(0.5)

    #kiválasztja, hogy minden tárgycsoport között keressen (tárgycsoportok = minden)

    #subject_classes_option = browser.find_element_by_xpath("//table[@id = 'upFilter_bodytable']/tbody/tr[5]/td[4]/select/option[@value = 'All']")
    #subject_classes_option.click()

    time.sleep(0.5)

    #beállítja, hogy minden nyelvű kurzus kereshető legyen

    subject_languages = browser.find_element_by_xpath("//table[@id = 'upFilter_bodytable']/tbody/tr[6]/td[4]/select/option[@value = 0]")
    subject_languages.click()

    time.sleep(0.5)

    for aktualis_targy in range(len(targylista)):
        print(targylista[aktualis_targy])
        targy_neve = targylista[aktualis_targy]['name']
        szeminarium_kodja = targylista[aktualis_targy]['code']

        #megkeresei a tárgynév mezőt, kitörli a tartalmát, belekattint és beírja a megadott tárgynevet, majd nyom egy entert.

        subject_name = browser.find_element_by_xpath("//table[@id = 'upFilter_bodytable']/tbody/tr[5]/td[2]/input")
        subject_name.clear()
        subject_name.click()
        subject_name.send_keys(targy_neve + Keys.RETURN)

        #vár, amíg a tárgyakat kategorizáló felső sáv (tárgyneve, tárgy kódja (...) meg nem jelenik

        el = WebDriverWait(browser, maximum_time_waiting).until(lambda browser: browser.find_element_by_id("h_addsubjects_gridSubjects_headerrow"))
        time.sleep(1)
        for i in range(1,4):
            print("próba:", i)
            try:
                specific_seminar = browser.find_element_by_xpath("//table[@id = 'h_addsubjects_gridSubjects_bodytable']/tbody/tr[%i]/td[2]/span" %(i)).text
                print(specific_seminar)
                if specific_seminar == targy_neve:
                    browser.find_element_by_xpath("//table[@id = 'h_addsubjects_gridSubjects_bodytable']/tbody/tr[%i]/td[2]/span" %(i)).click()
                    break
            except:
                print('Nem található ez a tárgynév!')

        #megvárja, amíg a szemináriumokat tartalmazó tábla nem töltődik be.

        el = WebDriverWait(browser, maximum_time_waiting).until(lambda browser: browser.find_element_by_id("Addsubject_course1_gridCourses_bodytable"))

        for i in range(1,40):
            exist = True
            try:
                found_seminar = browser.find_element_by_xpath("//table[@id = 'Addsubject_course1_gridCourses_bodytable']/tbody/tr[%i]/td[2]/span" %(i))
                print(found_seminar.text)
            except:
                exist = False
            if exist:
                if found_seminar.text == szeminarium_kodja:
                    assert exist
                    seminar_pipa = browser.find_element_by_xpath("//table[@id = 'Addsubject_course1_gridCourses_bodytable']/tbody/tr[%i]/td[13]/input" % i)
                    seminar_pipa.click()

        #rákattint a mentés gombra

        save_button = browser.find_element_by_xpath("//table[@id = 'Addsubject_course1_gridCourses_tablebottom']/tbody/tr[1]/td[3]/table/tbody/tr/td/input").click()
        
        print("Ezt a tárgyat sikeresen felvettem:", specific_seminar) 
        
        #orarend_tervezo_bezaro = browser.find_element_by_xpath("//div[@id = 'upFunction_h_addsubjects_upOrarendTervezo_OrarendTervezo']/input[2]").click()

    return "Mindent sikeresen felvettem!"


#Kiszámolja az adott félévet

#currentMonth = datetime.now().month
#currentYear = datetime.now().year
#semester = 2

#if 3 < currentMonth < 11:
#    semester = 1
#    currentYear += 1
#elif currentMonth == 11 or 12:
#    currentYear += 1

#neptun_date = str(currentYear - 1) + '/' + str(currentYear)[-2:] + '/' + str(semester)
#70619 = 2019/20/2