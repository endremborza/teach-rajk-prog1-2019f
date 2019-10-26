#!/usr/bin/env python
# coding: utf-8

# Advent of code 2016/Day3

# Import the data

# In[87]:


with open('input2.txt') as fp:
    file_contents = fp.read()
print(file_contents)


# From one "sentence" generate a list

# In[88]:


line_contents = file_contents.split('\n')
import re
print(line_contents)


# From a list with strings generate list with numbers in a list

# In[54]:


haha_word=[]
array_haha = len(line_contents)

for i in range(array_haha): 
    haha_word=haha_word+[line_contents[i].split()]

array_haha2 = len(haha_word)
haha_int=haha_word
for y in range(array_haha2): 
    haha_int[y] = [int(i) for i in haha_word[y]]

print(haha_int)


# Sort the numbers in the list and try the lowest two whether its larger then the third

# In[89]:


array_haha = len(haha_int)-1
y=0
for i in range(array_haha):
    lol2=haha_int[i]
    lol3=haha_int[i].sort() 
    A=lol2[:1]
    B=lol2[1:2]
    C=lol2[2:3]
    A=int(A[0])
    B=int(B[0])
    C=int(C[0])


    if A+B>C:
        y=y+1

    
print('Number of triangle:',y)
    


# In[ ]:




