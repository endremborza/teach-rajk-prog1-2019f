#!/usr/bin/env python
# coding: utf-8

# In[4]:


with open('AOC2015_1.txt') as fp:
    aoc_map = fp.read()


def split(word): 
    return [char for char in word] 

word=aoc_map


b=0
for x in split(word):
    if x == "(" :
        b=b+1
    elif x == ")":
        b=b-1

print (b)
    


# In[ ]:




