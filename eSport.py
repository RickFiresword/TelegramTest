#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys
from bs4 import BeautifulSoup
from telepot import loop
import requests
import telepot
import time
sys.setrecursionlimit(99999)

#=============TELEGRAM BOT======================#
token_i = '27503-R9VUM6NP7900Cw'

#my_telegram_chat_id = '-1001469274467' #testing
#


my_telegram_chat_id = '-1001414741135' #CYBER


token = '399177903:AAGgSX7V3G8vRyPpC_IaAWH9Q9JaHNMDJV0'
chat_id = "message.from_user.id"

bot = telepot.Bot(token)
url = 'https://api.betsapi.com/v2/events/inplay?sport_id=1&token=27503-R9VUM6NP7900Cw'

rr = 0




def executeSomething():

    try:
        r = requests.get(url).json()
        r = r['results']
        r = r[::-1]


    except (IndexError, KeyError, ValueError):
        time.sleep(5)
        executeSomething()
        print ("Errore with R ======")

    for j in r:
        get_sport_id = j['id']
        event_view = "https://api.betsapi.com/v1/event/view?token=27503-R9VUM6NP7900Cw&event_id=" + str(get_sport_id)

        r2 = requests.get(event_view).json()
        #r3 = requests.get(odds_view).json()
        time.sleep(0)

        try:
            r2 = r2['results']


        except (IndexError, KeyError, ValueError, TypeError):
            pass
            print (time.strftime("%H:%M:%S  ") + "Errore -r2-! ID: " + get_sport_id)




        try:

            for a in range(10000):
                #--------------<Settings>----------------->
                

                handle = open("all_links.txt", "r")
                data = handle.read().splitlines()

                for i in data:
                    rr = 'https://api.betsapi.com/v1/event/view?token=27503-R9VUM6NP7900Cw&event_id=' + i
                    rr = rr.replace('.text','')
                    r = requests.get(rr).text
                    soup = BeautifulSoup(r, features="html.parser")
                    handle2 = open(i +'.txt', "r")
                    data2 = handle2.read().splitlines()
                    data2 = data2[0]

                    print (data2)
                    





                    #print (soup)







        except (IndexError, KeyError, ValueError):
            pass
            print ("Passed!")
            #executeSomething()




while True:
    executeSomething()
    time.sleep(5)




