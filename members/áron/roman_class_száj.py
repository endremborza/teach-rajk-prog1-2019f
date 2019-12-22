#!/usr/bin/env python
# coding: utf-8

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


# In[ ]:





# In[15]:


class Roman:
    

    
    def __init__(self, num):
        
        if isinstance(num, str):
            self.roman = num
            self.arab = self.rom2ar()
            # TODO: somehow add .arab !!
        
        if isinstance(num, int):
            self.arab = num
            self.roman = 'I'
            
    def rom2ar(self):
        arab_number = 0

        if "IV" in self.roman:
            no_four = False
            arab_number += 4
        else:
            no_four = True
        
        if "IX" in self.roman:
            no_nine = False
            arab_number += 9
        else:
            no_nine = True    
    
        if "XL" in self.roman:
            no_forty = False
            arab_number += 40
        else:
            no_forty = True
        
        if "XC" in self.roman:
            no_ninety = False
            arab_number += 90
        else:
            no_ninety = True
        
        if "CD" in self.roman:
            no_fourhundred = False
            arab_number +=400
        else:
            no_fourhundred = True
        
        if "CM" in self.roman:
            no_ninehundred = False
            arab_number += 900
        else:
            no_ninehundred = True
    
        splited_roman = list(self.roman)
        
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
    
    def __add__(self, other):
        
        summa = self.arab + other.arab
        
        return Roman(summa)
    
    def __lt__(self, other):
        
        return self.arab < other.arab


# In[18]:


r = Roman("CCLXIV")


# In[19]:


r.arab


# ### TDD
# 
# - Test Driven Development

# In[30]:


r1 = Roman(5)
r1.roman == 'V'


# In[31]:


r2 = Roman('XV')
r2.arab == 15


# In[32]:


r3 = r1 + r2
r3.arab == 20


# In[33]:


r3.roman == "XX"


# In[34]:


r1 < r2


# In[ ]:


r4 = r3 * r2
r4.arab == 300


# In[38]:


for a in range(2000, 30000):
    rt1 = Roman(a)
    rt2 = Roman(rt1.roman)
    if rt1.arab != rt2.arab:
        print('JAJJJ')
        break


# In[39]:


rt1.arab


# In[40]:


rt2.arab


# In[41]:


rt1.roman

