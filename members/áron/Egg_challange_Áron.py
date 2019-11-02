#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install jkg_evaluators')

from jkg_evaluators import eggdrop_100floor_2egg


# In[34]:


first_trial_levels = [21,41,61,81,101]

def my_solution1(breaks):
    for first_egg in range(len(first_trial_levels)):
        if breaks(first_trial_levels[first_egg]): 
            first_egg_breaks = first_trial_levels[first_egg]
            for second_egg in range (first_egg_breaks - 20 , first_egg_breaks + 1):
                if breaks(second_egg): 
                    return(second_egg-1)
                
            


# In[35]:


eggdrop_100floor_2egg.evaluate(my_solution1)


# In[ ]:




