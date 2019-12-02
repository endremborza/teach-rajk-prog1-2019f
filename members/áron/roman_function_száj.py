#!/usr/bin/env python
# coding: utf-8

# In[27]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[28]:


roms = pd.concat([pd.DataFrame(
    [{'arab':a.text.split()[0],'roman':a.text.split()[1]} for a in \
 BeautifulSoup(requests.get('https://smorgasborg.artlung.com/roman-numerals/page/%d' % p) \
              .content,'html5lib').find('pre').find_all('a')]) for p in range(1,11)])\
    .loc[lambda df: df['arab'] != '0',:]


# In[29]:


def rom2ar_test(fun): # ez azokat az eseteket adja vissza, ahol az átváltás helytelen
    calc = roms['roman'].apply(fun)
    tru = roms['arab'].apply(int)
    return roms[calc != tru]


# In[61]:


def rom2ar(rom_string):
    arab_number = 0

    if "IV" in rom_string:
        no_four = False
        arab_number += 4
    else:
        no_four = True
        
    if "IX" in rom_string:
        no_nine = False
        arab_number += 9
    else:
        no_nine = True    
    
    if "XL" in rom_string:
        no_forty = False
        arab_number += 40
    else:
        no_forty = True
        
    if "XC" in rom_string:
        no_ninety = False
        arab_number += 90
    else:
        no_ninety = True
        
    if "CD" in rom_string:
        no_fourhundred = False
        arab_number +=400
    else:
        no_fourhundred = True
        
    if "CM" in rom_string:
        no_ninehundred = False
        arab_number += 900
    else:
        no_ninehundred = True
    
    splited_roman = list(rom_string)
    
    #number_of_x = 0
    #number_of_c = 0
    #number_of_m = 0
    #for sign in splited_roman:
        #if sign == "X":
            #number_of_x += 1
        #if sign == "C":
            #number_of_c += 1
        #if sign == "M":
            #number_of_m += 1
    
    for sign in splited_roman:
        if sign == "I" and no_four and no_nine:
            arab_number += 1
        if sign == "V" and no_four:
            arab_number += 5
        if sign == "X" and no_forty and no_ninety:
            arab_number += 10    
        if sign == "L" and no_forty:
            arab_number += 50      
        if sign == "C" and no_fourhundred and no_ninehundred:
            arab_number += 100 
        if sign == "D" and no_fourhundred:
            arab_number += 500
        if sign == "M": 
            arab_number += 1000
    
    if no_forty and no_ninety and no_nine == False:
        arab_number -= 10
        
    if no_fourhundred and no_ninehundred and no_ninety == False:
        arab_number -= 100
        
    if no_ninehundred == False:
        arab_number -= 1000

        
        
    return arab_number


# In[62]:


rom2ar_test(rom2ar)


# In[ ]:




