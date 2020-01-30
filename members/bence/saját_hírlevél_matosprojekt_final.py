#!/usr/bin/env python
# coding: utf-8

# Projekt leírás
# 
# Probléma definíció: számos híroldalról fogyasztunk tartalmat, de nehéz jól válogatni,
#     ráadásul minden nap érkeznek emellett az értesítések is. Hiába vannak beállított hírlevelek reggel 7 óra előtt,
#     nehezen lehet jól híreket válogatni, ha nem feltétlen csak a fő témákról akarunk értesülni. Személyesen cél, hogy olyan híroldalt vonjak be, amit kevesebbszer nézek. pl 24.hu
#     
# Eredeti leírás kommentekkel 
# 
# Programozási feladat: 
# 1. automatizáció rész: személyre szabott hírlevelet készítene a program, naponta 3-szor.
#     Egyet reggel, egyet napközben egyet pedig este.
#     A programnak lehessen megadni, hogy milyen híroldalakról válogasson
#     (ennek lenne egy maximuma, mondjuk max 6). ###legyen inkább 2 jól működő, tudja elküldeni nekem. utána esetleg update, hogy legyen külön felület, ahol erre fel lehet 'iratkozni'
# 2. scrapelés rész: szedje le a főcím linkeket + max 10-15 keresési szó
#     (ezeket inputként lehessen változtatni) ### a keresési szavakat lehet meg kell előre adni, hogy miből lehet válogatni
#     alapján a releváns cikkek linkjeit a megadott oldalakról és ezeket tegye be az emailbe
# 3. adatvizualizáció rész: hét végén küldjön egy összesítő e-mailt, hogy a megadott héten melyik oldalról
#     1) hány cikket küldött 2) milyen gyakran jöttek elő a megadott keresési szavak ### itt bármi jó, ami kijön de nem olyan fontos ### valószínűleg könnyebb összesített statisztikát küldeni az adott levélben, mint külön egy 'heti összegzőt' beállítani. valami + adat kéne bele, ezért inkább az adott időszaki levélről kéne érdekes információkat közölni
# 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import time
import datetime
last_day_sent = datetime.datetime.now()

while True:
    time.sleep(200)
    if datetime.datetime.now() - datetime.timedelta(days=1) > last_day_sent:
    
    
        keresoszavak_dict = {
            "24.hu": ["orban", "klima", "kozelet"],
            "mandiner": ["orosz", "eu", "trump", "meszaros"]
        }
        name = "Bence"
        email_cim = "matos.bence@gmail.com"

        def kereso(kulcsszo, hirek):
            found_list = []
            for hir in hirek:
                hir_link = hir.find('a')["href"]
                found_element = hir_link.find(kulcsszo)
                if found_element > 0:
                    found_list.append(hir)
            return found_list

        def hirlevel(kulcsszavak, oldal_hirlista):
            oldal_kapcsolodo_hirei = {}
            for kulcsszo in kulcsszavak:
                kulcsszo_linkejei = kereso(kulcsszo, oldal_hirlista)
                oldal_kapcsolodo_hirei[kulcsszo] = kulcsszo_linkejei
            return oldal_kapcsolodo_hirei


        hiroldal_url = "https://24.hu"
        resp = requests.get(hiroldal_url)
        soup = BeautifulSoup(resp.content)
        cimek = soup.find_all("h2", class_="m-entryWidget__title")
        relevans_24 = hirlevel(keresoszavak_dict["24.hu"], cimek)

        str_24 = "<h3>24hu hírek</h3>"
        for kulcsszo, kulcsszo_hirlista in relevans_24.items():
            str_24 += "<h4>{}</h4>".format(kulcsszo)
            for hir in kulcsszo_hirlista:
                hir_link = hir.find('a')["href"]
                hir_cim = hir.text

                str_24 += '<h5><a href="{}">{}</a><h5>'.format(hir_link, hir_cim) 

        mandiner_url = "https://mandiner.hu"
        resp2 = requests.get(mandiner_url)
        soup2 = BeautifulSoup(resp2.content)
        cimek_2 = soup2.find_all("div", class_="title")
        relevans_mand = hirlevel(keresoszavak_dict["mandiner"], cimek_2)

        str_mandiner = "<h3>Mandiner hírek</h3>"
        for kulcsszo, kulcsszo_hirlista in relevans_mand.items():
            str_mandiner += "<h4>{}</h4>".format(kulcsszo)
            for hir in kulcsszo_hirlista:
                hir_link = hir.find('a')["href"]
                if hir_link[0] == '/':
                    hir_link = 'https://mandiner.hu' + hir_link
                hir_cim = hir.text

                str_mandiner += '<h5><a href="{}">{}</a><h5>'.format(hir_link, hir_cim)

        str_hirlista = str_24 + str_mandiner


        today = datetime.date.today()

        message = """        Subject: Napi hírlevél
        Content-Type: text/html; charset=utf-8

        """


        intro = f'Kedves {name}! \n\n Az alábbiakban a mai hírlevelet olvashatod. \n\n Dátum: {today.year}.{today.month}.{today.day}. \n\n'

        end = f'Disclaimer: Ezt a hírlevelet a következő keresőszavak alapján állitottuk össze a 24.hu-ról: {keresoszavak_dict["24.hu"]} \nmandiner.hu-ról: {keresoszavak_dict["mandiner"]}\n\nHave a good day!'

        hirfolyam = message + intro + str_hirlista + end


        import smtplib, ssl

        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "sajat.hirlevel.projekt@gmail.com" 
        receiver_email = email_cim  
        password = "Sajathirlevel0"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, hirfolyam.encode("utf-8"))


    last_day_sent = datetime.datetime.now()

