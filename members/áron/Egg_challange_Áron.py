#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
#get_ipython().system('{sys.executable} -m pip install jkg_evaluators')

from jkg_evaluators import eggdrop_100floor_2egg


# In[34]:


first_trial_levels = [21,41,61,81,101]

def my_solution1(breaks):
    #Ha lehet ne hasznalj egy fuggvenyen belul olyan valtozot amit nem a fuggvenyen belul hozol letre,
    #vagy mint bemeneti parameter adsz meg neki.
    #Jelen esetben az first_trial_levels-t nyugodtan behozhattad volna fuggvenybe.
    for first_egg in range(len(first_trial_levels)):

        #A for ciklus ugy mukodik, hogy az altalad ujonnan deklaralt valtozo (jelen esetben first_egg) egyesevel felveszi egy iteralhato objektum osszes erteket.
        #A range az egy beepitett fuggveny, ami leegyszerusitve general egy listat,
        #melynek elemei alapesetben 0-tol (adott inputkent beadott objektum hossza) - 1 ig tarto egesz szamok egyes lepeskozzel.
        #Akkor erdemes ezt hasznalni for ciklusban, ha fontos az indexalas is, ha nem akkor hasznalhatod magad az iterhalhato objektumot.
        #Pl. for first_egg in first_trial_levels eseteben az i ugyan az, mint most nalad first_trial_levels[first_egg].

        if breaks(first_trial_levels[first_egg]):
            first_egg_breaks = first_trial_levels[first_egg]
            for second_egg in range (first_egg_breaks - 20 , first_egg_breaks + 1):
                if breaks(second_egg):
                    return(second_egg-1)




# In[35]:
#Jo megoldas!

eggdrop_100floor_2egg.evaluate(my_solution1)


# In[ ]:
