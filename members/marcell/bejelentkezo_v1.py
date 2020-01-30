from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def bejelentkezo(neptunkod, jelszo, maximum_time_waiting):
    "A függénynek 3 paramétere van: (1) Neptun-kód (idézőjelben), (2) Neptun-jelszó (idézőjelben), maximum várakozási idő a belépési probálkozások során (másodpercben) "

    #chrome megnyitása
    #neptun oldalának lekérése

    browser = webdriver.Chrome()
    url = 'https://neptun3r.web.uni-corvinus.hu/hallgatoi_1/login.aspx'
    browser.get(url)

    neptun_code = neptunkod
    password = jelszo
  
    #vár, amíg a felhasználónév mező nem töltődik be

    el = WebDriverWait(browser, maximum_time_waiting).until(lambda browser: browser.find_element_by_name("user"))

    #beírja a megadott neptun kódot
 
    browser.find_element_by_name('user').send_keys(neptun_code)

    #beírja a megadott jelszót

    browser.find_element_by_name('pwd').send_keys(password)

    #megnyomja a belépés gombot

    browser.find_element_by_name('btnSubmit').click()

    print('Sikeresen bejelentkeztem!')
    
    return browser

