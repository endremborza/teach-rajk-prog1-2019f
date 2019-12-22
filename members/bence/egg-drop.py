#!/usr/bin/env python
# coding: utf-8

# In[19]:


from jkg_evaluators import eggdrop_100floor_2egg


# In[26]:


def my_solution2(breaks):
    floor=14
    step=13
    while breaks(floor)==False:
        floor=floor+step
        step=step-1
    floor=floor-step+1
    while breaks(floor)==False:
        floor=floor+1
    return floor-1


# In[27]:


def my_solution3(breaks):
    floor=14
    step=13
    while breaks(floor)==False:
        floor=floor+step
        step=step-1
    floor=floor-step
    while breaks(floor)==False:
        floor=floor+1
    return floor-1


# In[28]:


eggdrop_100floor_2egg.evaluate(my_solution2)


# In[29]:


eggdrop_100floor_2egg.visualize(my_solution2)


# In[ ]:





# In[ ]:




