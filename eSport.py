#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys

from telepot import loop

reload(sys)

import requests

import telebot
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials



sys.setdefaultencoding('utf8')

#=============TELEGRAM BOT======================#
token_i = '27503-R9VUM6NP7900Cw'

#my_telegram_chat_id = '-1001469274467' #testing
#my_telegram_chat_ft = '-1001469274467' #testing


my_telegram_chat_id = '-1001403893518'
my_telegram_chat_ft = '-1001219317029'
my_telegram_chat_corners = '-1001249261381'

token = '399177903:AAGgSX7V3G8vRyPpC_IaAWH9Q9JaHNMDJV0'
chat_id = "message.from_user.id"

bot = telebot.TeleBot(token)
url = 'https://api.betsapi.com/v2/events/inplay?sport_id=1&token=27503-R9VUM6NP7900Cw'


def executeSomething():

    try:
        r = requests.get(url).json()
        r = r['results']
        r = r[::-1]


    except (IndexError, KeyError, ValueError):
        pass
        r = 0
        print (time.strftime("%H:%M:%S  ") + "Была ошибка -r-!")

    for j in r:
        get_sport_id = j['id']
        event_view = "https://api.betsapi.com/v1/event/view?token=27503-R9VUM6NP7900Cw&event_id=" + get_sport_id

        r2 = requests.get(event_view).json()
        time.sleep(0)

        try:
            r2 = r2['results']


        except (IndexError, KeyError, ValueError):
            pass
            print (time.strftime("%H:%M:%S  ") + "Была ошибка -r2-! ID: " + get_sport_id)


        try:

            for a in r2:
                #--------------<Settings>----------------->
                try:
                    #-Names
                    league = a['league']['name']
                    team_home = a['home']['name']
                    team_away = a['away']['name']
                except (IndexError, KeyError, ValueError):
                    league = int(1)
                    team_home = 1
                    team_away = 1
                    print ("%H:%M:%S  Была ошибка league")

                try:
                    #-Scores
                    score_home_str = str(a['scores']['2']['home'])
                    score_away_str = str(a['scores']['2']['away'])
                    score_home = int(score_home_str)
                    score_away = int(score_away_str)
                    score_total = score_away+score_home


                except (IndexError, KeyError, ValueError):
                    score_home_str = 0
                    score_away_str = 0
                    score_home = 0
                    score_away = 0
                    score_total = 0
                    print ("%H:%M:%S  Была ошибка -Scores-!")

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

                #-Time
                try:
                    the_time = a['timer']['tm'] + 1
                except (IndexError, KeyError, ValueError):
                    the_time = 0

                if the_time > 6:
                    print ("Не входит в диапозон времени. Стопаем")
                    time.sleep(1)
                    executeSomething()



                #--------------</Settings>----------------->

                #--------------<Text Messages>------------->

                league_name = ('🏆 League: ' + league)
                teams_text = ('Teams: ' + team_home + ' - ' + team_away)

                the_time_text = ('⏱️ Time: ' + str(the_time) + "'")

                score_total_text = ('⚽️ Score: ' + str(score_home) + " - " + str(score_away) + '  ( Total = ' + str(score_total) + ' )' )

                s_attacks_total_text = ('🗡Attacks: ' + str(s_attacks_home) + " - " + str(s_attacks_away) + '  ( Total = ' + str(s_attacks_total) + ' )' )
                d_attacks_total_text = ('  Danger attacks: ' + str(d_attacks_home) + " - " + str(d_attacks_away) + '  ( Total = ' + str(d_attacks_total) + ' )' )

                onTarget_total_text = ('⚔️ On target: ' + str(onTarget_home) + " - " + str(onTarget_away) + '  ( Total = ' + str(onTarget_total) + ' )' )
                offTarget_total_text = ('  Off target: ' + str(offTarget_home) + " - " + str(offTarget_away) + '  ( Total = ' + str(offTarget_total) + ' )' )

                corner_total_text = ('⛳ Corners: ' + str(corner_home) + ' - ' + str(corner_away) + '  ( Total = ' + str(corner_total) + ' )' )

                yellow_total_text = ('Yellow cards: ' + str(yellow_home) + ' - ' + str(yellow_away) + '  ( Total = ' + str(yellow_total) + ' )' )
                red_total_text = ('Red cards: ' + str(red_home) + ' - ' + str(red_away) + '  ( Total = ' + str(red_total) + ' )' )



                # ===============Алгоритм 0 - первый тайм ======================#

                if (the_time >= 1 and the_time <= 5) and (s_attacks_total >= 15) and (d_attacks_total >= 7) and (s_attacks_home >= 6 and s_attacks_away >= 6) and (d_attacks_home >= 2 and d_attacks_away >= 5) and score_total == 1 and corner_total <= 2:
                        score_total_plus = str(score_total + 0.5)
                        first_time_over = ("‼️ TEST 🌊 eSport ‼️" + "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5'+ " Over\n" + "➖➖➖➖➖➖➖➖➖➖\ ")
                        # чтение файла
                        handle = open("text.text", "r")
                        data = handle.read()
                        if teams_text in data:
                            print ('ДУБЛЬ ЕБАНЫЙ!!!!!!')
                            pass
                        else:
                            # ЗАПИСЬ в файл начало
                            f = open('text.text', 'a')
                            a = str(teams_text)
                            f.write(a)
                            f.close()

                            this_message = (bot.send_message(chat_id=my_telegram_chat_id, text=first_time_over))
                            id_get = this_message.message_id
                            new_id_get = id_get-304
                            new_id_get = str(new_id_get)
                            str_id_get = str(id_get)
                            print (time.strftime("%H:%M:%S  ") + 'ID последнего сообщения: ' + str_id_get)
                            first_time_over2 = ("❗ Wave_" + new_id_get + "   TEST eSport ❗"+ "\n" + "\n" + league_name + "\n" + teams_text + "\n" + "•" + "\n" + score_total_text + "\n" + the_time_text + "\n" + "••••" + "\n" + '💵 ADVICE:\n' 'Bet: 2,5' + " Over " +'\n' + "➖➖➖➖➖➖➖➖➖➖\ ")
                            bot.edit_message_text(chat_id=my_telegram_chat_id, message_id=id_get, text=first_time_over2)


                else:
                    print ((time.strftime("%H:%M:%S  ") + get_sport_id + " Не подходит условиям 1й тайм"))
                    pass
                    time.sleep(1)




        except (IndexError, KeyError, ValueError):
            pass
            print ("Пропускаем!")
            executeSomething()




while True:
    executeSomething()
    time.sleep(1)




