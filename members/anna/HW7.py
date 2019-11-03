#!/usr/bin/env python
# coding: utf-8

# Dragonos javítás és futtatás

# In[171]:


cow_alive_list_test_1 = [False, False, True, True, True, True, True, True]
number_of_cows = len(cow_alive_list_test_1)
print(number_of_cows)


# In[172]:


def my_solution2(cow_alive_list):
    fat_alive_cow_index = 0
    thin_alive_cow_index = number_of_cows - 1
    
    while (fat_alive_cow_index +1) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index + 
                          thin_alive_cow_index) / 2)
        if cow_alive_list[middle_cow]:
            thin_alive_cow_index = middle_cow
        else:
            fat_alive_cow_index = middle_cow
    
    return thin_alive_cow_index + 1
   
    
my_solution2(cow_alive_list_test_1)


# Próba

# In[ ]:


pip install jkg_evaluators


# In[ ]:


from jkg_evaluators import dragonfind_10_to_50


# In[173]:


def my_solution2(is_dead, number_of_cows):
    
    fat_alive_cow_index = 1
    thin_alive_cow_index = number_of_cows
    
    while (fat_alive_cow_index +1) < thin_alive_cow_index:
        middle_cow = int((fat_alive_cow_index + 
                          thin_alive_cow_index) / 2)
        if is_dead(middle_cow):
            fat_alive_cow_index = middle_cow
        else:
            thin_alive_cow_index = middle_cow
    
    return thin_alive_cow_index
   


# In[174]:


dragonfind_10_to_500.evaluate(my_solution2)


# In[170]:


dragonfind_10_to_500.visualize(my_solution2)

