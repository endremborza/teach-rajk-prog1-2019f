#!/usr/bin/env python
# coding: utf-8

# In[1]:


cow_alive_list_test_1=[False, False, True, True, True]


# In[2]:


def my_solution2(cow_alive_list):
    fat_alive_cow_index=0
    thin_alive_cow_index=len(cow_alive_list)-1
    
    while (fat_alive_cow_index+1) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index +
                          thin_alive_cow_index)/2)
        if cow_alive_list[middle_cow]:
            thin_alive_cow_index=middle_cow
        else:
            fat_alive_cow_index=middle_cow
            
    return thin_alive_cow_index+1


# In[3]:


my_solution2(cow_alive_list_test_1)


# In[ ]:


def my_solution1(cow_alive_list):
    place=0
    for cow_is_alive in cow_alive_list:
        place = place + 1
        if cow_is_alive:
            return place
    return place+1


# In[ ]:


my_solution1(cow_alive_list_test_1)


# In[4]:


pip install jkg_evaluators


# In[29]:


from jkg_evaluators import dragonfind_10_to_500


# In[32]:


def my_solution2(is_dead, number_of_cows):
    fat_alive_cow_index=0
    thin_alive_cow_index=number_of_cows
    
    while (fat_alive_cow_index+1) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index +
                          thin_alive_cow_index)/2)
        if is_dead(middle_cow)==False:
            thin_alive_cow_index=middle_cow
        else:
            fat_alive_cow_index=middle_cow
            
    return middle_cow


# In[33]:


dragonfind_10_to_500.evaluate(my_solution2)


# In[ ]:




