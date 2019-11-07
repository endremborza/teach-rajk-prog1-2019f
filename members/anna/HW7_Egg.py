#!/usr/bin/env python
# coding: utf-8

# Tojásos feladat

# Optimális algoritmus: 14 lépésből tudja biztosan azt, hogy hol tört el a dolog.
#     Mechanizmus - első tojásom valamekkora ugrásközönként megy felfele, ha eltörik, akkor a második tojásom a törést megelőző ledobott helyről
#     egyesével bandukol felfele.
#
#     1) Egyenlő ugrás
#     Kezdetben arra gondoltam, hogy egyenlő, optimális nagyságú ugrásokkal megyek felfele és így minimalizálok. Erre az egyenlet:
#             min 100/x + x - 1
#     Optimális osztályköz: 10
#             Így a minimum biztos lépés 19
#
#     2) Egyenlő ugrás + az első ugrás magasabbról
#     Ezután arra gondoltam, hogy kicsit lehetne magasabbról lehetne kezdeni, pont annyival, hogy ha esetleg eltörik az első ledobással,
#     akkor a másik tojással ahogy egyesével feljövök, úgy ne legyen több a lépésem, mint az optimális.
#             Így le tudtam csípni egy-kettő lépést
#
#     3) Eltérő ugrásközök
#     Végül arra jutottam, hogyha az elején megengedem magamnak hogy feljebb kezdjem, hogy kimaxoljam a szintek közötti ugrást, akkor ezt
#     később is megtehetném. Ha mondjuk 14 a minimum biztos dobásszám, akkor bármelyik első tojásos ledobásnál ha eltörik, akkor pont 14
#     lépéssel tudom biztosra, hogy hol a törés.
#

#Jo gondolatmenet és nagyon jo megoldas! :)

# In[22]:


floors_where_egg_broken_test = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
#number_of_floors=len(floors_egg_broken)
number_of_floors=len(floors_where_egg_broken_test)
#Nincsen letezik a floors_egg_broken. Ha a jupyterben egyszer lefuttattal egy cellat akkor megjegyzi az ott letrehozott valtozokat,
# viszont figyelj arra, hogyha atirod a valtozo nevet akkor azt mindnehol modositsd.
print(number_of_floors)


# In[80]:


optimal_floors = [14, 27, 39, 51, 61, 70, 78, 85, 91, 96, 100]
def egg_solution(floors_where_egg_broken):
    #Ha lehet ne hasznalj egy fuggvenyen belul olyan valtozot amit nem a fuggvenyen belul hozol letre,
    #vagy mint bemeneti parameter adsz meg neki.
    #Jelen esetben az optimal_floors-t nyugodtan behozhattad volna fuggvenybe.
    current_floor = int(optimal_floors[0])
    jump = 13
    while floors_where_egg_broken[current_floor]==False:
        current_floor= current_floor + jump
        jump = jump - 1

    sure_it_breaks = current_floor
    print(sure_it_breaks)
    jump = jump + 1
    current_floor= current_floor - jump +1

    while floors_where_egg_broken[current_floor]==False & (current_floor+1 <sure_it_breaks):
        current_floor=current_floor+1

    print(current_floor)
    if current_floor+1==sure_it_breaks:
        return current_floor
    else:
        return current_floor -1


# In[152]:


def egg_solution_general(breaks):
    current_floor = 14
    jump = 13
    while breaks(current_floor)==False:
        current_floor= current_floor + jump
        jump = jump - 1

    sure_it_breaks = current_floor
    jump = jump + 1
    current_floor = current_floor - jump +1

    while (breaks(current_floor)==False):
        if (current_floor+1)==sure_it_breaks:
            return current_floor
        else:
            current_floor=current_floor+1

    return current_floor - 1


# Evaluation

# In[81]:


egg_solution(floors_where_egg_broken_test)


# In[37]:


from jkg_evaluators import eggdrop_100floor_2egg


# In[153]:


eggdrop_100floor_2egg.evaluate(egg_solution_general)


# In[154]:


eggdrop_100floor_2egg.visualize(egg_solution_general)
