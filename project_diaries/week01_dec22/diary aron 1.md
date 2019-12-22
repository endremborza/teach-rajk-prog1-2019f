Projekt állapot, tervek.

előző héten kitúzött célok közül megvalósult:
- kitalatam potencialis iranyokat a projektemnek:
  
  (1) lehet hogy irnek valamilyen fuggvenyt, amiben automatikusan at tud alakitani nem megfelelo
  formatumban levo adatbazisokat hasznalhato formatumba, ebbol tobb kulon dataframe-t es adatfajlt is csinal (csv). 
  egz kulon fuggveny az osszes elkeszult dataframe-bol abrakat keszit
  Pl. a fuggveny parameterei: maga az adat dataframe formaban (pl. segely tranzakciokat tartalmazo tablazat), a valtozok, ami alapjan az aggregalas mindig megtorenik (nekem kezenfekvo az ev, fogado orszag, aggregalt valtozo a segely mennyisege)
  a valtozok, ami alapjan kulon-kulon aggregal es kulon adatfajlokat csinal (itt az orszag ev mellett felmerulo mas aggregalasi szempontok vannak, ez alapjan aggregal es csinal egy csv file-t)
  
  (2) adatbazisok merge-lesenel mindig visszatero problema, hogy az identifikacio kulcsa az orszag nev, ami sok helyen elter 
  egy olyan fuggvenyt irnek, ami meglevo adatbazisokat kiegeszit egy uj valtozoval, ami az orszag valamilyen sztenderd betu-szamkodja
  ehhez letre kell hozni egy dictionary-t ami tartalmazza az adott orszagkodokhoz tartozo kulonbozo leiratu orszagneveket
  jo lenne ezt ugy megcsinalni, hogy valamilyen automatizalt formaban tartalmazza az elgepeleseket is
  ennek talan egy haladobb valtozata lenne, ha mondjuk google forditoval leforditana az orszagneveket mindenfele nyelvre es igy is fel tudna ismerni a kulonbozo nyelveken leirt orszagneveket is
  ez lehetne egy nyilt forraskodu git projekt is, amit mindenki kiegeszithet, ha talal fura orszagnev leiratokat
  
  (3) egy korabbi hazi soran irtam programozasi problemakent, hogy jo lenne Twitter-rol lescrapelni mindig automatikusan a Political Science temaju osztondijakat, amit elkuldene az emailemre automatikusan a program
  talan haladobb, de lehetne irni egy fuggvenyt, ami kulcsszavak alapjan scrapel es csak egy limitalt mennyisegu tweetet kuld el emailben

előző héten kitúzött célok közül nem valósult meg:
- nem dontottem el, hogy melyik iranyt valasztom a projektemnek
- ez nem tudom, hogy ide tartozik-e: nem kezdtem el az AOC-t


következő hétre kitűzött célok:
- eldonteni, hogy melyik ranyt valasszam a projektnek
- utananezni alaposabban a Twitter scrapelsnek, python-oauth2 dokumentaciojanak
- a Pandas dataframe-mel baratkozni
- megcsinlani 5 AOC csillagot


elolvasni X package dokumentációjának releváns részét
működő prototípust csinálni Y ötlethez
olvasni cikkeket és use caseket Z témában

heti források

- Twitter scrapeles: https://mdl.library.utoronto.ca/technology/tutorials/scraping-tweets-using-python#twitter-api


Hasznos dolgok:

- Jucust megkerdeztem, hogy mennyire volt bonyolult a scrapelos projektje, azt mondta, hogy neki eleg egyszeru volt 
(nem kellett vegtelenul sokat alakitania elore megirt programkodokon) 

- Jani segitett a fejlgazd beszamolomhoz es egyben a munkahelyemre irt tanulmanyhoz Pandas-szal adatokat aggregalni,
ez az (1)-es projekt otlethez kapcsolodik

AoC csillagok eddig
