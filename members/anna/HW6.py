#!/usr/bin/env python
# coding: utf-8

# Advent of code 2016/Day3

# Import the data

# In[87]:


with open('input2.txt') as fp:
    file_contents = fp.read()
#print(file_contents) #A vegso fajlban ez a print inkabb zavaro, mint hasznos.


# From one "sentence" generate a list
# Ertekelem a kommenteket!

# In[88]:
#Ezeket viszont torolhetted volna.


line_contents = file_contents.split('\n')
import re #Ezt hasznalod valamire? 
#print(line_contents)  


# From a list with strings generate list with numbers in a list

# In[54]:


haha_word=[]
array_haha = len(line_contents)

#A for ciklus ugy mukodik, hogy az altalad ujonnan deklaralt valtozo (jelen esetben i) egyesevel felveszi egy iteralhato objektum osszes erteket.
#A range az egy beepitett fuggveny, ami leegyszerusitve general egy listat,
#melynek elemei alapesetben 0-tol (adott inputkent beadott objektum hossza) - 1 ig tarto egesz szamok egyes lepeskozzel.
#Akkor erdemes ezt hasznalni for ciklusban, ha fontos az indexalas is, ha nem akkor hasznalhatod magad az iterhalhato objektumot.
#Pl. for i in line_contents eseteben az i ugyan az, mint most nalad line_contents[i].
for i in range(array_haha): 
    haha_word=haha_word+[line_contents[i].split()]

array_haha2 = len(haha_word)
haha_int=haha_word
for y in range(array_haha2): 
    haha_int[y] = [int(i) for i in haha_word[y]]

#print(haha_int) #A vegso fajlban ez a print inkabb zavaro, mint hasznos. 


# Sort the numbers in the list and try the lowest two whether its larger then the third

# In[89]:


array_haha = len(haha_int)-1
y=0
for i in range(array_haha):
    lol2=haha_int[i]
    lol3=haha_int[i].sort()
    #Ha megnezed a lol3 erteke None. Ez azert van mert a sort inplace vegzi el a sorbarendezet.
    #Ez azt jelent, hogy az eredeti objektumban valtozik meg az elemek sorrendje, viszont ezert a sort fuggveny visszateresi erteke None.
    #A lol3 = resz tehat elhagyhato. Illetve azert lesz jo az eredmenyek, mert a lol2-ben is megvaltozik a sorrend eppen ezert.
    #Erdemes elobb sortolni aztan deklaralni es erteket adni a lol2-nek. 
    A=lol2[:1]
    B=lol2[1:2]
    C=lol2[2:3]
    A=int(A[0])
    B=int(B[0])
    C=int(C[0])

    #Ezt lehet egy fokkal egyszerubben is. Ha egy lista konkret elemet akarod kivalsztani, akkor eleg annak az indexet megadni.
    #lol2[0] az majdnem ugyan az mint a lol2[:1]. Annyi a kulonbseg, hogy az utobbi esetben ugy adod meg mintha a lista egy adott reszet kerned
    #egy konkret elem helyett. Ez azt eredmenyezi, hogy lol2[0] tipusa a listaelem tipusa (jelen esetben string), mig a lol2[:1] az egy egyelemu lista.
    #Szoval A = lol2[:1], A = int(A[0]) helyett mehet rogton a A = int(lol2[0]).

    if A+B>C:
        y=y+1

    
print('Number of triangle:',y)
#Ugyes megoldas! :)  


# In[ ]:




