#!/usr/bin/env python
# coding: utf-8

# # Száj feladat megoldásai
# 
# # adatok betöltése, nagy lista készítése

# In[4]:


import json


# In[37]:


path_to_file = 'data/2010-msg.json'
path_to_file1 = 'data/2011-msg.json'
path_to_file2 = 'data/2012-msg.json'
path_to_file3 = 'data/2013-msg.json'
path_to_file4 = 'data/2014-msg.json'
path_to_file5 = 'data/2015-msg.json'
path_to_file6 = 'data/2016-msg.json'
path_to_file7 = 'data/2017-msg.json'
path_to_file8 = 'data/2018-msg.json'
path_to_file9 = 'data/2019-msg.json'


# In[5]:


list_of_dicts_2010 = json.load(open(path_to_file, 'r'))
list_of_dicts_2011 = json.load(open(path_to_file1, 'r'))
list_of_dicts_2012 = json.load(open(path_to_file2, 'r'))
list_of_dicts_2013 = json.load(open(path_to_file3, 'r'))
list_of_dicts_2014 = json.load(open(path_to_file4, 'r'))
list_of_dicts_2015 = json.load(open(path_to_file5, 'r'))
list_of_dicts_2016 = json.load(open(path_to_file6, 'r'))
list_of_dicts_2017 = json.load(open(path_to_file7, 'r'))
list_of_dicts_2018 = json.load(open(path_to_file8, 'r'))
list_of_dicts_2019 = json.load(open(path_to_file9, 'r'))


# In[12]:


all_lists = []


# In[13]:


all_lists.extend(list_of_dicts_2010)
all_lists.extend(list_of_dicts_2011)
all_lists.extend(list_of_dicts_2012)
all_lists.extend(list_of_dicts_2013)
all_lists.extend(list_of_dicts_2014)
all_lists.extend(list_of_dicts_2015)
all_lists.extend(list_of_dicts_2016)
all_lists.extend(list_of_dicts_2017)
all_lists.extend(list_of_dicts_2018)
all_lists.extend(list_of_dicts_2019)


# In[14]:


len(all_lists)


# # első feladat: ki vagyok én? - legtöbb üzenetet küldő

# In[26]:



event_senders = []
for dic in list_of_dicts_2011:
    event_senders.append(dic['sender_name'])


unique_senders = list(set(event_senders))

number_of_events = 0
list_of_name_occurances = []
for sender in unique_senders:
    number_of_events = 0
    for allsender in event_senders:
        if sender == allsender:
            number_of_events += 1
    list_of_name_occurances.append(number_of_events)

print(max(list_of_name_occurances))

import operator
index, value = max(enumerate(list_of_name_occurances), key=operator.itemgetter(1))

print(unique_senders[index])

list_of_name_occurances.sort()
print(list_of_name_occurances)


# # Egy olyan nested dictionary-t hozunk létre, amiben a key a thread azonosítója, az érték pedig egy dictionary, amiben a key a "number of events" string, az érték pedig ennek a tényleges értéke

# In[ ]:




#list of unique threads
threads = []
for dic in all_lists:
    threads.append(dic['thread_path'])


unique_threads = list(set(threads))


#list of number of events for each thread (the order is the same as list of unique threads)

eventsnumber = []
for thread in unique_threads:
    number_of_threads = 0
    for event_thread in threads:
        if event_thread == thread:
            number_of_threads += 1
    eventsnumber.append(number_of_threads)
    
#list of dictionaries of number of events for each thread (the order is the same as list of unique threads)

list_of_events_per_thread_dics = []
for eventsperthread in eventsnumber:
    dict_actual_feature = {"number of events": eventsperthread}
    list_of_events_per_thread_dics.append(dict_actual_feature)
    
# Create nested dictionary from list of unique threads and list of dictionaries of number of events

zip_threadid_feautures1 = zip(unique_threads, list_of_events_per_thread_dics)
                           
# Create a dictionary from zip object
dictofthreads_events = dict(zip_threadid_feautures1)


# # Ezt a nested dictionary-t kiegészítjük egy újabb értékkel, ami még egy dictionary, ennek a key-e a "sender name" nevű string, az érték pedig ennek a tényleges értéke

# In[17]:



#list of unique senders

event_senders = []
for dic in all_lists:
    event_senders.append(dic['sender_name'])

unique_senders = list(set(event_senders))

#list of number of senders per thread (order is same as unique threads)

sendersnumber = []
number_of_senders_list = []
for thread in unique_threads:
    number_of_senders = 0
    sendersthread_list = []
    for event in all_lists:
 if event['thread_path'] == thread:
     sendersthread_list.append(event['sender_name'])
     number_of_senders = len(list(set(sendersthread_list)))
    number_of_senders_list.append(number_of_senders)


list_of_number_of_senders_dics = []
for sendersperthread in number_of_senders_list:
    dict_actual_feature_sender = {"number of senders": sendersperthread}
    list_of_number_of_senders_dics.append(dict_actual_feature_sender)    

# Create nested dictionary from list dictionaries of number of senders and unique threads
                                               
zip_threadid_feautures2 = zip(unique_threads, list_of_number_of_senders_dics)
                    
# Create a dictionary from zip object
dictofthreads_senders = dict(zip_threadid_feautures2)

#merge the two nested dictionaries

for key in dictofthreads_events:
     dictofthreads_events[key].update(dictofthreads_senders.get(key, {}))


# # A nagy nested ditionary-t tovább bővítjük egy újabb értékkel, ami egy dictionary (key - "starting year" nevű string , érték ennek megfelelő)

# In[22]:


#a Marci által írt chronologic függvénnyel időrendi sorba rendezzük az input dictionary-t

def chronologic(input_list):
    sorted_list = sorted(input_list, key = lambda i: i['timestamp_ms'])
    return sorted_list


# In[23]:


sorted_all_lists = chronologic(all_lists)


# In[24]:


#list of starting years for each thread (same order as unique threads)

starting_year = []
for thread in unique_threads:
    for event in sorted_all_lists:
        if event['thread_path'] == thread:
            starting_year.append(event['year'])
            break


# In[26]:


#list of dictionaries of starting years for each thread

list_of_dicts_years_start = []
for startyear in starting_year:
    dict_actual_feature_sender3 = {"starting year": startyear}
    list_of_dicts_years_start.append(dict_actual_feature_sender3)  


# In[28]:


zip_threadid_feautures3 = zip(unique_threads, list_of_dicts_years_start)
                           
# Create a dictionary from zip object
dictofthreads_startyear = dict(zip_threadid_feautures3)

#merge nested dictionaries

for key in dictofthreads_events:
    dictofthreads_events[key].update(dictofthreads_startyear.get(key, {}))

    

    
print(dictofthreads_events)


# # A nagy nested dictionary-t tovább bővítem, hozzáadom a thread típusát (key "chat type" string, érték ennek megfelelő)

# In[ ]:


#létrehozzuk a thread type-ok listáját (ugyanaz a sorrend, mint a unique threads-nél)

chattype_list = []
for thread in unique_threads:
    for event in sorted_all_lists:
        if event['thread_path'] == thread:
            chattype_list.append(event['thread_type'])
            break

#list of chattype dictionaries 

list_of_chattype_dicts = []           
for chattypes_per_thread in chattype_list:
    dict_chattype = {"chat type": chattypes_per_thread}
    list_of_chattype_dicts.append(dict_chattype)
    
#nested dictionary: key - unique threads, value - chattype dictionary
    
zip_threadid_feautures_sok = zip(unique_threads, list_of_chattype_dicts)

dictofthreads_chattype = dict(zip_threadid_feautures_sok)

#merge dictionaries

for key in dictofthreads_events:
    dictofthreads_events[key].update(dictofthreads_chattype.get(key, {}))
    


# # find potential DB chat list: 

# In[31]:


potential_db_chat_list = []
potential_db_chat_list_events = []
potential_db_chat_list_startyear = []

for key in dictofthreads_events:
    if dictofthreads_events[key]['number of senders'] == 11:
        potential_db_chat_list.append(key)
        potential_db_chat_list_events.append(dictofthreads_events[key]['number of events'])
        potential_db_chat_list_startyear.append(dictofthreads_events[key]['starting year'])

print('IDs of potential DB chats:', potential_db_chat_list)
print('Number of events of potential DB chats:', potential_db_chat_list_events)
print('Starting year of potential DB chats:', potential_db_chat_list_startyear)


# # find potential JESZK Moments

# In[30]:


potential_jeszkmoments_list = []
potential_jeszkmoments_events = []
potential_jeszkmoments_startyear = []

for key in dictofthreads_events:
    if dictofthreads_events[key]['number of senders'] > 80:
        potential_jeszkmoments_list.append(key)
        potential_jeszkmoments_events.append(dictofthreads_events[key]['number of events'])
        potential_jeszkmoments_startyear.append(dictofthreads_events[key]['starting year'])

print('IDs of potential JESZK Moments:', potential_jeszkmoments_list)
print('Number of events of potential JESZK Moments:', potential_jeszkmoments_events)
print('Starting year of potential JESZK Moments:', potential_jeszkmoments_startyear)


# # a top10 legnagyobb chat között (amiben valaha a legtöbb ember volt) melyik chatben volt a legkevesebb esemény?

# In[86]:


#fordított sorba rendezem a küldők számának listáját

sorted_number_of_senders = sorted(number_of_senders_list, reverse = True)

#ez alapján létrehozom a top10 senderszámból álló listát

list_top10senderchat_number = []
for i in range(0,10):
    list_top10senderchat_number.append(sorted_number_of_senders[i])
    
#megkeresem, hogy ezekhez melyik thread tartozik, ezeknek az id-jából összeállítok egy listát (ugyanaz a sorrend)

list_top10senderchat_id = []
for sendernumber in list_top10senderchat_number:
    for key in dictofthreads_events:
        if dictofthreads_events[key]['number of senders'] == sendernumber:
            list_top10senderchat_id.append(key)
            
#megkeresem, hogy az előbbi lista egyes threadjei közül melyikhez hány esemény tartozik, ennek a listáját is létrehozom            

list_top10senderchat_events = []
for senderid in list_top10senderchat_id:
    for key in dictofthreads_events:
        if key == senderid:
            list_top10senderchat_events.append(dictofthreads_events[key]['number of events'])
            
#csinálok egy dictionary-t, az utóbbi két lista alapján, az id a key, a number of event az érték

zip_top10 = zip(list_top10senderchat_id, list_top10senderchat_events)
                           

dicttop10 = dict(zip_top10)

#megkeresem, hogy ebben a dictionary-ben melyik id-hez tartozik a legkisebb érték

min_value = min(dicttop10, key = dicttop10.get)

print(dicttop10)

print('A top10 legtöbb emberes chat közül, a legkevesebb esemény ebben volt (thread_id):', min_value)

#for thread in list_of_number_of_senders_dics:
    
#for thread in dictofthreads_events:
    


# # top5 legkevesebb eseményes chat ezen belül: 799: 36, 577: 36, 498: 100, 807: 150, 392: 228, 

# In[ ]:


#ugyanez, nem kibogarászva a listából

import operator
sorted_dicttop10 = sorted(dicttop10.items(), key=operator.itemgetter(1))
print(sorted_dicttop10)


# # A top10 legnagyobb groupchat között (amiben valaha a legtöbb esemény volt) melyik chatben volt a legkevesebb ember (akik valaha a chatben voltak és küldtek üzenetet az adott chatben)?

# In[80]:


#a group chatekhez tartozó eseményszámok listája, fordított sorba rendezve

events_number_list = []
for threads in dictofthreads_events:
    if dictofthreads_events[threads]['chat type'] == 'RegularGroup':
        events_number_list.append(dictofthreads_events[threads]['number of events'])

        
sorted_eventsnumber = sorted(events_number_list, reverse=True)

#ez alapján a top10 listája (ebben az eseményszám van)

list_top10eventschat_number = []
for i in range(0,10):
    list_top10eventschat_number.append(sorted_eventsnumber[i])

#az ezekhez tartozó chat id-k listája (azonos sorrend)    

list_top10eventschat_id = []
for eventsnum in list_top10eventschat_number:
    for key in dictofthreads_events:
        if dictofthreads_events[key]['number of events'] == eventsnum:
            list_top10eventschat_id.append(key)
            
#az ezekhez tartozó küldők számának listája
            
list_top10eventschat_senders = []
for eventid in list_top10eventschat_id:
    for key in dictofthreads_events:
        if key == eventid:
            list_top10eventschat_senders.append(dictofthreads_events[key]['number of senders'])


#dictionary ezekből, key a chat id, érték a küldők számának értéke
            
zip_top10_2 = zip(list_top10eventschat_id, list_top10eventschat_senders)
                           
dicttop10_2 = dict(zip_top10_2)

#a legkisebb értékhez tartozó key kiválasztása ebből a listából

min_value_2 = min(dicttop10_2, key = dicttop10_2.get)

print(dicttop10_2)

print('A top10 legtöbb üzenetes chat közül, a legkevesebb ember ebben küldött üzenetet valaha (thread_id):', min_value_2)

    


# # A top5 legkevesebb emberes chat ezen belül: 724: 4, 710: 4, 706: 9, 465: 11, 508: 12

# In[ ]:


#Ugyanez nem kibogarászva:
sorted_dicttop10 = sorted(dicttop10.items(), key=operator.itemgetter(1))
print(sorted_dicttop10)  


# # Egy főre jutó eseményszám

# In[83]:


#a threadekhez tartozó egy főre jutó eseményszámok listája
event_capita_list = []
for threads in dictofthreads_events:
    event_capita = int(dictofthreads_events[threads]['number of events'])/int(dictofthreads_events[threads]['number of senders'])
    event_capita_list.append(event_capita)

#az egy főre jutó eseményszámok dictionary-jeinek listája (key "event per capita" string, érték ennek megfelelő)
    
list_of_dicts_event_capita = []
for event_capita in event_capita_list:
    dict_actual_feature_sender4 = {"event per capita": event_capita}
    list_of_dicts_event_capita.append(dict_actual_feature_sender4) 
    
#dictionary, amiben a key a thread id, a value az előbbi listák

zip_threadid_feautures_5 = zip(unique_threads, list_of_dicts_event_capita)

dictofthreads_eventcapita = dict(zip_threadid_feautures_5)

#sorba rendezve az eventcapita, ezalapján a top5 egyfőre jutó eseményszám listája
    
sorted_eventcapita = sorted(event_capita_list)

list_top5eventcapita = []
for i in range(0,5):
    list_top5eventcapita.append(event_capita_list[i])
    
#ezeknek az id-jainka a beazonosítása
    
list_top5eventcapita_id = []
for topevent in list_top5eventcapita:
    for key in dictofthreads_eventcapita:
        if dictofthreads_events[key]['events per capita'] == topevent:
            list_top5eventcapita_id.append(key)
            
print(list_top5eventcapita_id)
            


# In[ ]:





# In[ ]:




