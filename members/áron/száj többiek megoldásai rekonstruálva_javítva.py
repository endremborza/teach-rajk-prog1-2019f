#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.insert(0, '..')
from __import_file__ import danka
from __import_file__ import szaj
from __import_file__ import flora
from __import_file__ import petra
from __import_file__ import lili
from __import_file__ import marci
from __import_file__ import matos
from __import_file__ import kornel
from __import_file__ import anna


# ## danka

# In[9]:


def danka_solution(inputlist):
    ordered_list = sorted(inputlist)
    new_variable1 = int(ordered_list[0] * ordered_list[1])
    reverse_ordered_list = sorted(inputlist, reverse=True)
    new_variable2 = int(reverse_ordered_list[0] * reverse_ordered_list[1])
    newlist = []
    newlist.append(new_variable1)
    newlist.append(new_variable2)
    newlist.sort(reverse=True)                                                                
    return newlist[0]


# In[10]:


danka.evaluate(danka_solution)


# ## száj

# In[ ]:


def szaj_solution():
    # modify this function
    # return value and parameters and all
    return 0


# In[ ]:


szaj.evaluate(szaj_solution)


# ## flóra

# In[26]:



def flora_solution(list_of_numbers):
    list_of_good_numbers = []
    for number in list_of_numbers:
        number = str(number)
        good_number = True
        
        for digit in range(0, len(number)-1):
            if not number[digit] == "-":
                if  float(number[digit]) > float(number[digit+1]):
                    good_number = False
                    break
        if good_number:
                list_of_good_numbers.append(int(number))
    list_of_good_numbers.sort
    
    if not list_of_good_numbers == False:
        return max(list_of_good_numbers)
    else:
        return 0


# In[29]:


flora.evaluate(flora_solution)


# ## petra

# In[16]:


def petra_solution(inputlist):
    inputlist_without_muliple_items = set(inputlist)
    empty_list = []
    for number in inputlist_without_muliple_items:
        if number > 0:
            if not number % 2 == 0:
                empty_list.append(number)
    sum_of_even = sum(empty_list)
    return sum_of_even


# In[17]:


petra.evaluate(petra_solution)


# ## lili

# In[2]:


def lili_solution(list_of_numbers):
    int_halves = []
    for dividend in list_of_numbers:
        for divisor in list_of_numbers:
            if divisor*2 == dividend:
                int_halves.append(divisor)
                
    if int_halves == []:
        return 0
    else:
        int_halves.sort
        smallest_where_double = int(min(int_halves))
        
        return smallest_where_double


# In[3]:


lili.evaluate(lili_solution)


# ## marci

# In[113]:


def marci_solution(list_of_strings, inputstring):
    character_counter = []
    for element in list_of_strings:
        letter_counter = 0
        for character in element:
            if character == inputstring:
                letter_counter = letter_counter + 1
        element = element.swapcase()
        for character in element:
            if character == inputstring:
                letter_counter = letter_counter + 1
        character_counter.append(letter_counter)

    if max(character_counter) == 0:
        return ""
    else:
        indexofmaxcharacter = character_counter.index(max(character_counter))
        return list_of_strings[indexofmaxcharacter]


# In[114]:


marci.evaluate(marci_solution)


# ## matos

# In[33]:


def matos_solution(inputlist):
    list_lenght = len(inputlist)
    list_numberofa_in_inputlistelements = []
    
    for texts in inputlist:
        numberofa = texts.count('a') + texts.count('A')
        list_numberofa_in_inputlistelements.append(numberofa)
        
    sortedlist_numberofa_in_inputlistelements = sorted(list_numberofa_in_inputlistelements)
    word_of_most_a = sortedlist_numberofa_in_inputlistelements[len(sortedlist_numberofa_in_inputlistelements)-1]
    word_of_most_a_index = list_numberofa_in_inputlistelements.index(word_of_most_a)
    
    if word_of_most_a == 0:
        return -1
    else:
        return word_of_most_a_index


# In[34]:


matos.evaluate(matos_solution)


# ## kornél

# In[139]:


def kornel_solution(list_of_strings, character):
    variable = 0
    for element in list_of_strings:
        element = element.lower()
        for letter in element:
            if letter == character.lower():
                variable+=1
                break
    return variable


# In[133]:


def kornel_solution(list_of_strings, character):
    variable = 0
    for element in list_of_strings:
        if character.lower() in element.lower():
            variable+=1
    return variable


# In[140]:


kornel.evaluate(kornel_solution)


# ## anna

# In[174]:


def anna_solution(list_of_integers, number):
    #solution = []
    for element in list_of_integers:
        variable = element-number
        number_of_solutions = 0
        if variable % 3 == 0:
            #solution.append(element)
            solution=element
            number_of_solutions+=1
            if number_of_solutions == 2:
                break
    return solution


# In[ ]:





# In[175]:


anna.evaluate(anna_solution)


# In[ ]:




