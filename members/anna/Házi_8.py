#!/usr/bin/env python
# coding: utf-8

# In[2]:


def aron_function(list_of_numbers, number):
    solution = 0
    list_of_numbers.sort()
    for value in list_of_numbers:
        if ((value / number) % 2) == 0:
            solution = value
    return solution

aron_function(list_of_numbers, number)


# In[7]:


def kornel_function(list_of_strings, string):
    solution = 0
    for value in list_of_strings:
        if value.lower() == string:
            solution += 1
            
    return solution

kornel_function(list_of_strings, string)


# In[8]:


list_of_numbers = [112,134,210]
def flora_function(list_of_numbers):
    list_of_good_numbers = []
    for value in list_of_numbers:
        good_number = 'TRUE'
        value_string = str(value)
        for character in range(len(value_string)-1):
            if value_string[character] > value_string[character+1]:
                good_number = 'FALSE'
                    
        if good_number == 'TRUE':
            list_of_good_numbers.append(value)
    list_of_good_numbers.sort
    return list_of_good_numbers[-1]             

flora_function(list_of_numbers)

