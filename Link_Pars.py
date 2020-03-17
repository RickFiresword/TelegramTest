#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys

from telepot import loop

reload(sys)

import requests
from bs4 import BeautifulSoup
import telebot
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#test


sys.setdefaultencoding('utf8')

mylist = []

my_telegram_chat_id = '-1001196904283'

token = '399177903:AAGgSX7V3G8vRyPpC_IaAWH9Q9JaHNMDJV0'
chat_id = "message.from_user.id"

bot = telebot.TeleBot(token)
url = 'https://coronavirusupdate.me'


def executeSomething():
    handle = open("link_country.txt", "r")
    data = handle.read().splitlines()

    for i in data:

        r = requests.get(i).text

        soup = BeautifulSoup(r, features="html.parser")

        country = soup.find("h1").get_text() #total deaths
        country = str("".join(country.split())).replace('CoronavirusLiveUpdate','')
        #print country



        deaths_total = soup.findAll("h2", {'style':'color:red'})[0].get_text() #total deaths
        deaths_total = str("".join(deaths_total.split()))

        deaths_today = soup.findAll("h2", {'style':'color:red'})[1].get_text() #total deaths today
        deaths_today = str("".join(deaths_today.split())).replace('+','')

        cases_today = soup.findAll("h2", {'style':'color:red'})[2].get_text() #total deaths today
        cases_today = str("".join(cases_today.split())).replace('+','')

        cases_total = soup.findAll("h2", {'style':'color:red'})[3].get_text() #total deaths today
        cases_total = str("".join(cases_total.split()))

        recovered_total = soup.findAll("h2", {'style':'color:red'})[4].get_text() #total deaths today
        recovered_total = str("".join(recovered_total.split()))

        critical_total = soup.findAll("h2", {'style':'color:red'})[5].get_text() #total deaths today
        critical_total = str("".join(critical_total.split()))



        ttt = ("🦠 Country: #" + country + "\n•\n💀 Total Deaths: " + deaths_total + "\nDeaths Today: " + deaths_today + "\n••\n🚑 Total Cases: " + cases_total + "\nCases Today: " + cases_today + "\n•••\n💊 Total Recovered: " + recovered_total + "\n⚡ Total Critical: " + critical_total + "\n ➖➖➖➖➖➖")
        #print(ttt)

        # чтение файла
        handle = open(country + '.txt', "r")
        data = handle.readlines()

        if str(data[0]) == str(country):
            pass
            #print('Название страны не изменилось!')


        if int(data[1]) == int(deaths_total):
            pass
            #print('Общие смерти не изменились!')
        else:
            #print('Данные общих смертей поменялись!')

            bot.send_message(chat_id=my_telegram_chat_id, text="💀️ New death (+" + str((int(deaths_total) - int(data[1]))) +") in #"+ country + ". \n Deaths Today: " + deaths_today + "\n Total Deaths: " + deaths_total)
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[3]) == int(cases_total):
            pass
            #print('Общие зараженные не изменились!')
        else:
            #print('Данные общих зараженных поменялись!')

            bot.send_message(chat_id=my_telegram_chat_id, text="🚑️ New case (+" + str((int(cases_total) - int(data[3]))) +") in #"+ country + ". \n Cases Today: " + cases_today + "\n Total Cases: " + cases_total)
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[5]) == int(recovered_total):
            pass
            #print('Общие вылеченые не изменились!')
        else:
            #print('Данные общих вылеченных поменялись!')

            bot.send_message(chat_id=my_telegram_chat_id, text="💊️ New recovered (+" + str((int(recovered_total) - int(data[5]))) +") in #"+ country + ". \n Total Recovered: " + recovered_total)
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[6]) == int(critical_total):
            pass
            #print('Общие критических не изменились!')
        else:
            #print('Данные общих критических поменялись!')

            bot.send_message(chat_id=my_telegram_chat_id, text="⚡ New critical (+" + str((int(critical_total) - int(data[6]))) +") in #"+ country + ". \n Total Critical: " + critical_total)
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()



        time.sleep(0)
        #bot.send_message(chat_id=my_telegram_chat_id, text=ttt)




        '''
        f = open(country + '.txt')
    
        # ЗАПИСЬ в файл начало
        f = open(country + '.txt', 'a')
        a = str(country + "\n" + deaths_total + "\n" + deaths_today + "\n" + cases_total + "\n" + cases_today + "\n" + recovered_total + "\n" + critical_total)
        f.write(a)
        f.close()
        '''

while True:
    executeSomething()

