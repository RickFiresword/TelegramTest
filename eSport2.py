#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys

from telepot import loop


import requests

import telepot
import time
sys.setrecursionlimit(99999)

#=============TELEGRAM BOT======================#
token_i = '27503-R9VUM6NP7900Cw'

#my_telegram_chat_id = '-1001469274467' #testing
#my_telegram_chat_id ='-1001451066908'


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
    #except:
        #print (r)

    except (IndexError, KeyError, ValueError):
        time.sleep(5)
        executeSomething()
        print ("Errore with R ======")

    for j in r:
        get_sport_id = j['id']
        event_view = "https://api.betsapi.com/v1/event/view?token=27503-R9VUM6NP7900Cw&event_id=" + str(get_sport_id)
        #odds_view = "https://api.betsapi.com/v2/event/odds?token=27503-R9VUM6NP7900Cw&event_id=" + str(get_sport_id)

        r2 = requests.get(event_view).json()
        #r3 = requests.get(odds_view).json()
        time.sleep(0)

        try:
            r2 = r2['results']


        except (IndexError, KeyError, ValueError, TypeError):
            pass
            print (time.strftime("%H:%M:%S  ") + "Errore -r2-! ID: " + get_sport_id)

        # try:
        #     odd_home = r3['results']['odds']['1_1'][0]['home_od']
        #     odd_away = r3['results']['odds']['1_1'][0]['away_od']
        # except (IndexError, KeyError, ValueError):
        #     odd_home = str(1)
        #     odd_away = str(1)
        #     print (time.strftime("%H:%M:%S  ") + "Errore -r3-! odd_home ID: " + get_sport_id)
        #     print (time.strftime("%H:%M:%S  ") + "Errore -r3-! odd_away ID: " + get_sport_id)
        #     #pass






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
                    s_attacks_total = str(s_attacks_total)
                    d_attacks_home = a['stats']['dangerous_attacks'][0]
                    d_attacks_away = a['stats']['dangerous_attacks'][1]
                    d_attacks_total = int(d_attacks_home)+int(d_attacks_away)
                    d_attacks_total = str(d_attacks_total)

                except (IndexError, KeyError, ValueError):
                    s_attacks_home = '0'
                    s_attacks_away = '0'
                    s_attacks_total = '0'
                    d_attacks_home = '0'
                    d_attacks_away = '0'
                    d_attacks_total = '0'
                    print ("%H:%M:%S  Была ошибка -Atacks-!")

                #-Corners
                corner_home = a['stats']['corners'][0]
                corner_away = a['stats']['corners'][1]
                corner_total = int(corner_home)+int(corner_away)
                corner_total = str(corner_total)

                #-Targets
                onTarget_home = a['stats']['on_target'][0]
                onTarget_away = a['stats']['on_target'][1]
                onTarget_total = int(onTarget_away)+int(onTarget_home)
                onTarget_total = str(onTarget_total)
                offTarget_home = a['stats']['off_target'][0]
                offTarget_away = a['stats']['off_target'][1]
                offTarget_total = int(offTarget_away)+int(offTarget_home)
                offTarget_total = str(offTarget_total)


                #Cards
                red_home = a['stats']['redcards'][0]
                red_away = a['stats']['redcards'][1]
                red_total = int(red_home)+int(red_away)
                red_total = str(red_total)
                #<
                yellow_home = a['stats']['yellowcards'][0]
                yellow_away = a['stats']['yellowcards'][1]
                yellow_total = int(yellow_home)+int(yellow_away)
                yellow_total = str(yellow_total)

                time_status = a['time_status']

                #-Time
                try:
                    the_time = a['timer']['tm'] + 1
                    #the_time = str(the_time)
                except (IndexError, KeyError, ValueError):
                    the_time = 0

                if the_time > 10:
                    print ("Time to high. Stoped")
                    time.sleep(1)
                    executeSomething()



                # if int(odd_home) > int(odd_away):
                #     under_team = team_away
                #     under_s_attacks = int(s_attacks_away)
                #     under_d_attacks = int(d_attacks_away)
                #     under_onTarget = int(onTarget_away)
                #     under_offTarget = int(offTarget_away)
                #     under_score = int(score_away)
                # elif int(odd_home) == int(odd_away):
                #     under_team = 'No underdog'
                # else:
                #     under_team = team_home
                #     under_s_attacks = int(s_attacks_home)
                #     under_d_attacks = int(d_attacks_home)
                #     under_onTarget = int(onTarget_home)
                #     under_offTarget = int(offTarget_home)
                #     under_score = int(score_home)





                #--------------</Settings>----------------->

                #--------------<Text Messages>------------->
                league = str(league)
                league_name = ('🕹️ League: ' + league)
                league_name = str(league_name)
                teams_text = ('Teams: ' + team_home + ' - ' + team_away)
                teams_text = str(teams_text)

                the_time_text = ('⏱️ Time: ' + str(the_time) + "'")
                the_time_text = str(the_time_text)

                score_total_text = ('⚽️ Score: ' + str(score_home) + " - " + str(score_away) + '  ( Total = ' + str(score_total) + ' )' )
                score_total_text = str(score_total_text)

                # # =============== КИБЕР ФУТБОЛ 2,5 OVER ======================#

                # if (int(the_time) >= 4 and int(the_time) <= 6) and (int(s_attacks_total) >= 15) and (int(d_attacks_total) >= 7) and (int(s_attacks_home) >= 6 and int(s_attacks_away) >= 6) and (int(d_attacks_home) >= 2 and int(d_attacks_away) >= 5) and int(score_total) == 1 and int(corner_total) <= 2 and int(red_total) == 0:
                # #if the_time > 0:
                #         score_total_plus = str(score_total + 0.5)
                #         first_time_over = ("‼️ NEW 🌊 WAVE ‼️" + "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5'+ " Over\n" + "➖➖➖➖➖➖➖➖➖➖\ ")
                #         # чтение файла
                #         handle = open("text.text", "r")
                        
                #         data = handle.read()
                #         if str(get_sport_id) in data:
                #             print ('FUCKING INFO !!!')
                #             pass
                #         else:
                #             # ЗАПИСЬ в файл начало
                #             f = open('text.text', 'a')
                #             a = str('\n' + get_sport_id + "="+ "[" + get_sport_id + "," + teams_text + "]" )
                #             f.write(a)
                #             f.close()

                #             this_message = (bot.sendMessage(chat_id=my_telegram_chat_id, text=first_time_over))
                #             #print (this_message[message_id])
                #             id_get = this_message['message_id']
                #             #id_get = this_message.message_id
                #             new_id_get = id_get-9
                #             new_id_get = str(new_id_get)
                #             str_id_get = str(id_get)
                #             print (time.strftime("%H:%M:%S  ") + 'last message ID: ' + str_id_get)
                #             first_time_over2 = ("❗ Wave_" + new_id_get + "  eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5' + " Over " +'\n' + "➖➖➖➖➖➖➖➖➖➖\ ")
                #             #first_time_over2 = (str_id_get + "\n" + str(get_sport_id) + "\n" + time_status + "\n" )
                #             ff = open('all_links.txt', 'a')
                #             f = open(get_sport_id + '.txt', 'a')

                #             a = str_id_get
                #             a = (a)
                #             b = get_sport_id 
                #             b = str("\n" + b)
                            
                #             f.write(a)
                #             ff.write(b)

                #             f.close()
                #             ff.close()
                #             #bot.editMessageText(chat_id=my_telegram_chat_id, message_id=id_get, text=first_time_over2)
                #             bot.editMessageText(telepot.message_identifier(this_message), text=first_time_over2)

                # else:
                #     print (str(get_sport_id) + " Bad conditions for 10-12 Min GAMES (1st str)")
                #     #print ("Odd Away: " + odd_away + "\nOdd Home: " + odd_home)
                #     pass
                #     time.sleep(0.3)




                # # =============== КИБЕР ФУТБОЛ 2,5 OVER (2nd)======================#

                # if int(the_time) < 8 and (int(s_attacks_total) >= 25) and (int(d_attacks_total) >= 20) and int(score_total) == 2 and int(corner_total) == 2 and int(red_total) == 0 and int(yellow_total) == 0 and (int(onTarget_total)+int(offTarget_total) == 2):
                # #if the_time > 0:
                #         score_total_plus = str(score_total + 0.5)
                #         first_time_over = ("‼️ NEW 🌊 WAVE ‼️" + "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5'+ " Over\n" + "➖➖➖➖➖➖➖➖➖➖\ ")
                #         # чтение файла
                #         handle = open("text.text", "r")
                #         data = handle.read()
                #         if str(get_sport_id) in data:
                #             print ('FUCKING INFO !!!')
                #             pass
                #         else:
                #             # ЗАПИСЬ в файл начало
                #             f = open('text.text', 'a')
                #             a = str('\n' + get_sport_id + "="+ "[" + get_sport_id + "," + teams_text + "]" )
                #             f.write(a)
                #             f.close()

                #             this_message = (bot.sendMessage(chat_id=my_telegram_chat_id, text=first_time_over))
                #             #print (this_message[message_id])
                #             id_get = this_message['message_id']
                #             #id_get = this_message.message_id
                #             new_id_get = id_get-9
                #             new_id_get = str(new_id_get)
                #             str_id_get = str(id_get)
                #             print (time.strftime("%H:%M:%S  ") + 'last message ID: ' + str_id_get)
                #             first_time_over2 = ("❗ Wave_" + new_id_get + "  eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5' + " Over " +'\n' + "➖➖➖➖➖➖➖➖➖➖\ ")
                #             #first_time_over2 = (str_id_get + "\n" + str(get_sport_id) + "\n" + time_status + "\n" )
                #             ff = open('all_links.txt', 'a')
                #             f = open(get_sport_id + '.txt', 'a')

                #             a = str_id_get
                #             a = (a)
                #             b = get_sport_id 
                #             b = str("\n" + b)
                            
                #             f.write(a)
                #             ff.write(b)

                #             f.close()
                #             ff.close()
                #             #bot.editMessageText(chat_id=my_telegram_chat_id, message_id=id_get, text=first_time_over2)
                #             bot.editMessageText(telepot.message_identifier(this_message), text=first_time_over2)

                # else:
                #     print (str(get_sport_id) + " Bad conditions for 10-12 Min GAMES (2nd str)")
                #     #print ("Odd Away: " + odd_away + "\nOdd Home: " + odd_home)
                #     pass
                #     time.sleep(0.3)    



                                #=============== КИБЕР ФУТБОЛ 8 min games ======================#
                if int(the_time) >= 0 and int(the_time) < 2 and '8 mins' in league_name and int(score_total) == 1:
                #if the_time > 0:
                        score_total_plus = str(score_total + 0.5)
                        first_time_over = ("‼️ NEW 🌊 WAVE ‼️" + "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n••••" + "\n" + '💵 ADVICE:\n' + 'Bet: ' + score_total_plus + " Over\n" + "➖➖➖➖➖➖➖➖➖➖\ ")
                        # чтение файла
                        handle = open("text.text", "r")
                        data = handle.read()
                        if str(get_sport_id) in data:
                            print ('FUCKING INFO !!!')
                            pass
                        else:
                            # ЗАПИСЬ в файл начало
                            f = open('text.text', 'a')
                            a = str('\n' + get_sport_id + "="+ "[" + get_sport_id + "," + teams_text + "]" )
                            f.write(a)
                            f.close()

                            this_message = (bot.sendMessage(chat_id=my_telegram_chat_id, text=first_time_over))
                            id_get = this_message['message_id']
                            new_id_get = id_get-9
                            new_id_get = str(new_id_get)
                            str_id_get = str(id_get)
                            print (time.strftime("%H:%M:%S  ") + 'last message ID: ' + str_id_get)
                            first_time_over2 = ("❗ Wave_" + new_id_get + "  eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 15% on: ' + score_total_plus + " Over HT \nBet: 85% on 1.5 Over FT" +'\n' + "➖➖➖➖➖➖➖➖➖➖\ ")

                            ff = open('all_links.txt', 'a')
                            f = open(get_sport_id + '.txt', 'a')

                            a = str_id_get
                            a = (a)
                            b = get_sport_id 
                            b = str("\n" + b)
                            
                            f.write(a)
                            ff.write(b)

                            f.close()
                            ff.close()



                            #bot.editMessageText(chat_id=my_telegram_chat_id, message_id=id_get, text=first_time_over2)
                            bot.editMessageText(telepot.message_identifier(this_message), text=first_time_over2)



                else:
                    print (str(get_sport_id) + " Bad conditions for 8 Min GAMES")
                    #print ("Odd Away: " + odd_away + "\nOdd Home: " + odd_home + "\nUnderdog: " + under_team)
                    pass
                    time.sleep(1)




        except (IndexError, KeyError, ValueError):
            #pass
            print ("Passed!")
            #executeSomething()




while True:
    executeSomething()
    time.sleep(7)




