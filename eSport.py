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
#my_telegram_chat_id ='-1001451066908'
#


my_telegram_chat_id = '-1001414741135' #CYBER


token = '399177903:AAGgSX7V3G8vRyPpC_IaAWH9Q9JaHNMDJV0'
chat_id = "message.from_user.id"

bot = telepot.Bot(token)
url = 'https://api.betsapi.com/v2/events/inplay?sport_id=1&token=27503-R9VUM6NP7900Cw'

rr = 0



def executeSomething():


    try:


            #--------------<Settings>----------------->
            

        handle = open("all_links.txt", "r")
        data = handle.read().splitlines()
        stroki=len(data)
        stroki = str(stroki)
        print (stroki)

        for a in range(stroki):

            for i in data:
                rr = 'https://api.betsapi.com/v1/event/view?token=27503-R9VUM6NP7900Cw&event_id=' + i
                rr = rr.replace('.text','')
                r = requests.get(rr).json()
                r = r['results']
                #r = r[::-1]

                for a in r:
                    
                    time_status = a['time_status']
                    time_status = int(time_status)
                    #-Names
                    league = a['league']['name']
                    team_home = a['home']['name']
                    team_away = a['away']['name']
                    the_time = 2
                    score_home_str = int(a['scores']['2']['home'])
                    score_away_str = int(a['scores']['2']['away'])
                    score_home = int(score_home_str)
                    score_away = int(score_away_str)
                    score_total = score_away+score_home
                    league_name = ('🕹️ League: ' + league)
                    teams_text = ('Teams: ' + team_home + ' - ' + team_away)

                    the_time_text = ('⏱️ Time: ' + str(the_time) + "'")

                    score_total_text = ('⚽️ Score total: 1' )



                
                    handle2 = open(i +'.txt', "r")
                    data2 = handle2.read().splitlines()
                    data2 = data2[0]
                    data2 = int(data2)
                    new_id_get = data2+9
                    new_id_get = str(new_id_get)
                    score_total_plus = str(1.5)
                    first_time_over1 = ("❗ Wave_" + new_id_get + "  eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 15% on: ' + score_total_plus + " Over HT \nBet: 85% on 1.5 Over FT" +'\n' + "➖➖➖➖➖➖➖➖➖➖\ \n✅ Final score: " + str(score_home) + " - " + str(score_away) + " ✅")
                    first_time_over2 = ("❗ Wave_" + new_id_get + "  eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 15% on: ' + score_total_plus + " Over HT \nBet: 85% on 1.5 Over FT" +'\n' + "➖➖➖➖➖➖➖➖➖➖\ \n❌ Final score: " + str(score_home) + " - " + str(score_away) + " ❌")
                    first_time_over3 = ("❗ Wave_" + new_id_get + "  eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5' + " Over " +'\n' + "➖➖➖➖➖➖➖➖➖➖\ \n✅ Final score: " + str(score_home) + " - " + str(score_away) + " ✅")
                    first_time_over4 = ("❗ Wave_" + new_id_get + "  eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5' + " Over " +'\n' + "➖➖➖➖➖➖➖➖➖➖\ \n❌ Final score: " + str(score_home) + " - " + str(score_away) + " ❌")

                    try:
                        time.sleep(2)
                        if (time_status == 3) and ('8' in league) and score_total > 1:
                            print ("8 min games >>> Total over YES")
                            bot.editMessageText((my_telegram_chat_id, data2), first_time_over1)
                        elif (time_status == 3) and ('8' in league) and score_total < 2:
                            bot.editMessageText((my_telegram_chat_id, data2), first_time_over2)
                            print ("8 min games <<< Total over NO")


                        elif (time_status == 3) and ('1' in league) and score_total < 3:
                            bot.editMessageText((my_telegram_chat_id, data2), first_time_over4)
                            print ("10/12 min games <<< Total over NO")

                        elif (time_status == 3) and ('1' in league) and score_total > 2:
                            bot.editMessageText((my_telegram_chat_id, data2), first_time_over3)
                            print ("10/12 min games >>> Total over YES")

                        else:
                            pass

                    except:
                        pass

            handle.close()
            handle2.close()



    except (IndexError, KeyError, ValueError):
        pass
        print ("Passed!")
        #executeSomething()




while True:
    executeSomething()
    time.sleep(300)




