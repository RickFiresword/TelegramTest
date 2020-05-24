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

            for a in r2:
                #--------------<Settings>----------------->
                try:
                    #-Names
                    league = a['league']['name']
                    team_home = a['home']['name']
                    team_away = a['away']['name']
                except (IndexError, KeyError, ValueError, TypeError):
                    league = str('errore')
                    team_home = str('errore')
                    team_away = 'errore'
                    print ("%H:%M:%S  Errore league")


                try:
                    #-Scores
                    score_home_str = int(a['scores']['2']['home'])
                    score_away_str = int(a['scores']['2']['away'])
                    score_home = int(score_home_str)
                    score_away = int(score_away_str)
                    score_total = score_away+score_home


                except (IndexError, KeyError, ValueError):
                    score_home_str = 0
                    score_away_str = 0
                    score_home = 0
                    score_away = 0
                    score_total = 0
                    print ("%H:%M:%S  Errore -Scores-!")

                try:
                    #-Attacks
                    s_attacks_home = a['stats']['attacks'][0]
                    s_attacks_away = a['stats']['attacks'][1]
                    s_attacks_total = int(s_attacks_home)+int(s_attacks_away)
                    d_attacks_home = a['stats']['dangerous_attacks'][0]
                    d_attacks_away = a['stats']['dangerous_attacks'][1]
                    d_attacks_total = int(d_attacks_home)+int(d_attacks_away)

                except (IndexError, KeyError, ValueError):
                    s_attacks_home = 0
                    s_attacks_away = 0
                    s_attacks_total = 0
                    d_attacks_home = 0
                    d_attacks_away = 0
                    d_attacks_total = 0
                    print ("%H:%M:%S  Была ошибка -Atacks-!")

                #-Corners
                corner_home = a['stats']['corners'][0]
                corner_away = a['stats']['corners'][1]
                corner_total = int(corner_home)+int(corner_away)

                #-Targets
                onTarget_home = a['stats']['on_target'][0]
                onTarget_away = a['stats']['on_target'][1]
                onTarget_total = int(onTarget_away)+int(onTarget_home)
                offTarget_home = a['stats']['off_target'][0]
                offTarget_away = a['stats']['off_target'][1]
                offTarget_total = int(offTarget_away)+int(offTarget_home)


                #Cards
                red_home = a['stats']['redcards'][0]
                red_away = a['stats']['redcards'][1]
                red_total = int(red_home)+int(red_away)
                #<
                yellow_home = a['stats']['yellowcards'][0]
                yellow_away = a['stats']['yellowcards'][1]
                yellow_total = int(yellow_home)+int(yellow_away)

                time_status = a['time_status']





                #--------------</Settings>----------------->

                #--------------<Text Messages>------------->

                league_name = ('🕹️ League: ' + league)
                teams_text = ('Teams: ' + team_home + ' - ' + team_away)

                the_time_text = ('⏱️ Time: ' + str(the_time) + "'")

                score_total_text = ('⚽️ Score: ' + str(score_home) + " - " + str(score_away) + '  ( Total = ' + str(score_total) + ' )' )
  


                handle = open("all_links.txt", "r")
                data = handle.read().splitlines()

                for i in data:
                    rr = 'https://api.betsapi.com/v1/event/view?token=27503-R9VUM6NP7900Cw&event_id=' + i
                    rr = rr.replace('.text','')
                    r = requests.get(rr).text
                    soup = BeautifulSoup(r, features="html.parser")
                    handle2 = open(i +'.txt', "r")
                    data2 = handle2.read().splitlines()
                    data2 = data[0]

                    print (data2)
                    





                    #print (soup)







        except (IndexError, KeyError, ValueError):
            pass
            print ("Passed!")
            #executeSomething()




while True:
    executeSomething()
    time.sleep(5)




