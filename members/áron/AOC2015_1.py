#!/usr/bin/env python
# coding: utf-8

# In[4]:


with open('AOC2015_1.txt') as fp:
    aoc_map = fp.read()


def split(word):
    return [char for char in word]

#A list(word) egyebkent ugyan ezt megcsinalja, az egyszerubb jovobeni hasznalat vegett.
#Viszont ugyes sajat megolda, orulok hogy irtal ilyet. A programozas elejen tok jo ha nem csak beepitett dolgokat hasznalsz.

word=aoc_map
#A word valtozo bevezetese kicsit folosleges,
#rogton elnevezhetted volna az aoc_map-ot word-nek, vagy hasznalhattad volna azt.


b=0
for x in split(word):
    if x == "(" :
        b=b+1
    elif x == ")":
        b=b-1

print (b)



# In[ ]:
