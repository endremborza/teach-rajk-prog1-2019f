Projekt állapot, tervek.

előző héten kitűzött célok közül megvalósult:
- kitaláltam potenciális irányokat a projektemnek:
  
  (1) lehet hogy írnek valamilyen függvényt, ami automatikusan átalakít nem megfelelő
  formátumban lévő adatbázisokat használható formátumba, ebből több külön dataframe-t es adatfájlt is csinál (csv). 
  egy külön függvény az összes elkészült dataframe-ből ábrákat készít
  Pl. a függvény paraméterei: maga az adat dataframe formában (pl. segély tranzakciókat tartalmazó táblázat), a változok, ami alapján az aggregálás mindig megtörténik (nekem kézenfekvő az év, fogadó ország, aggregált változó a segély mennyisége)
  a változok, ami alapján külön-külön aggregál es külön adatfájlokat csinál (itt az ország év mellett felmerülő más aggregálási szempontok vannak, ez alapján aggregál es csinál egy csv file-t)
  
  (2) adatbázisok összekapcsolásánál mindig visszatérő probléma, hogy az identifikáció kulcsa az ország név, ami sok helyen eltér 
  egy olyan függvényt írnék, ami meglevő adatbázisokat kiegészít egy új változóval, ami az ország valamilyen sztenderd betű-számkódja
  ehhez létre kell hozni egy dictionary-t ami tartalmazza az adott országkódokhoz tartozó különböző leiratú országneveket
  jó lenne ezt úgy megcsinálni, hogy valamilyen automatizált formában tartalmazza az elgépeléseket is
  ennek talán egy haladóbb változata lenne, ha mondjuk google fordítóval lefordítani az országneveket mindenfele nyelvre es igy is fel tudna ismerni a különböző nyelveken leírt országneveket is
  ez lehetne egy nyílt forráskódú git projekt is, amit mindenki kiegészíthet, ha talál fura országnév leiratokat
  
  (3) egy korábbi házi során írtam programozási problémaként, hogy jó lenne Twitter-ről lescrapelni mindig automatikusan a Political Science témájú ösztöndíjakat, amit elküldene az emailemre automatikusan a program
  talán haladóbb, de lehetne írni egy függvényt, ami kulcsszavak alapján scrapel es csak egy limitalt mennyiségű tweetet küld el emailben

előző héten kitűzött célok közül nem valósult meg:
- nem dontottem el, hogy melyik iranyt valasztom a projektemnek
- ez nem tudom, hogy ide tartozik-e: nem kezdtem el az AOC-t


következő hétre kitűzött célok:
- utánanézni alaposabban a Twitter scrapelésnek, python-oauth2 dokumentaciojanak
- utánanézni a Googletrans dokumentációjának
- a Pandas dataframe-mel tovább barátkozni, python vizualizációkat nézegetni
- ezek alapján eldönteni, hogy melyik irányt válasszam a projektnek
- a Twitteresnél látok leginkább konkrét továbblépést, ha ezt választanám, akkor telepíteni a python-oauth2-t, egy "teszt scrapelést" csinálni
- megcsinálni 5 AOC csillagot

heti források

- Twitter scrapeles: https://mdl.library.utoronto.ca/technology/tutorials/scraping-tweets-using-python#twitter-api
- fordítás: https://pypi.org/project/googletrans/
- Adatvizualizálás: https://python-graph-gallery.com/


Hasznos dolgok:

- Jucust megkérdeztem, hogy mennyire volt bonyolult a scrapelos projektje, azt mondta, hogy neki elég egyszerű volt 
(nem kellett végtelenul sokat alakítania előre megírt programkódokon) 

- Jani segitett a fejlgazd beszamolomhoz és a munkahelyemre írt tanulmányhoz Pandas-szal adatokat aggregálni,
ez az (1)-es projekt ötlethez kapcsolódik


