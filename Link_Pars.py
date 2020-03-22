#! /usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import sys
from telepot import loop
from importlib import reload
reload(sys)
import requests
from bs4 import BeautifulSoup
import telepot
import time
from datetime import datetime


my_telegram_chat_id = '-1001196904283'
token = '399177903:AAGgSX7V3G8vRyPpC_IaAWH9Q9JaHNMDJV0'
chat_id = "message.from_user.id"
bot = telepot.Bot(token)

url = 'https://coronavirusupdate.me'




def executeSomething():

    handle = open("link_country.txt", "r")
    data = handle.read().splitlines()
    
   
    
    for i in data:
        r = requests.get(i).text
        soup = BeautifulSoup(r, features="html.parser")
        country = soup.find("h1").get_text() #total deaths
        country = str("".join(country.split())).replace(' ','').replace('Coronavirus','').replace('Update','')
        #print country
        deaths_total = soup.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[0].get_text()  # total deaths today
        deaths_total = str("".join(deaths_total.split()))
        deaths_today = soup.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[1].get_text() #total deaths today
        deaths_today = str("".join(deaths_today.split())).replace('+','')
        cases_today = soup.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[2].get_text() #total deaths today
        cases_today = str("".join(cases_today.split())).replace('+','')
        cases_total = soup.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[3].get_text() #total deaths today
        cases_total = str("".join(cases_total.split()))
        recovered_total = soup.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[4].get_text() #total deaths today
        recovered_total = str("".join(recovered_total.split()))
        critical_total = soup.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[5].get_text() #total deaths today
        critical_total = str("".join(critical_total.split()))
        
        
                
        # чтение файла
        #handle2 = open('Day_stats.txt', "r")
        #data2 = handle2.readlines()


        if int(data[1]) == int(deaths_total):
            print(country + ' Deaths total not changed')

        else:
            print(country + ' Deaths changed ---------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('💀️' + " New deaths (+" + str((int(deaths_total) - int(data[1]))) +") in #"+ country + ". \n\n Deaths Today: " + deaths_today + "\n Total Deaths: " + deaths_total + "\n ➖➖➖➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[3]) == int(cases_total):
            print(country + ' Infected not changed')

        else:
            print(country + ' Infected changed ---------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('🚑️' +" New cases (+" + str((int(cases_total) - int(data[3]))) +") in #"+ country + ". \n\n Cases Today: " + cases_today + "\n Total Cases: " + cases_total + "\n ➖➖➖➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[5]) == int(recovered_total):
            print(country + ' Recovered not changed')

        else:
            print(country + ' Recovered changed ---------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('💊️' +" New recovered (+" + str((int(recovered_total) - int(data[5]))) +") in #"+ country + ". \n\n Total Recovered: " + recovered_total + "\n ➖➖➖➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[6]) == int(critical_total):
            print(country + ' Critical not changed')

        else:
            print(country + ' Critical changed ----------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('⚡' +" New critical (+" + str((int(critical_total) - int(data[6]))) +") in #"+ country + ". \n\n Total Critical: " + critical_total + "\n ➖➖➖➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()
            
            
        if q_data == '15:53':
            if int(data2[2]) != int(cases_global_today):
                print('NOOOOOOOOOOOOW')
        else:
            print('Now is 23:59  ---------------------------')

            #bot.sendMessage(chat_id=my_telegram_chat_id, text=('Its time!'))
            f = open('Day_stats.txt', 'w')
            a = str(deaths_global_all + "\n" + deaths_global_today + "\n"  + cases_global_today + "\n"  + cases_global_all + "\n"  + critial_global_all + "\n"  + affected_global_all)
            f.write(a)
            f.close()
            # ЗАПИСЬ в файл начало
        time.sleep(0)
        #bot.send_message(chat_id=my_telegram_chat_id, text=ttt)
        
        # tests
        
        #f = open(country + '.txt', 'w')
        
        # ЗАПИСЬ в файл начало
        #f = open(country + '.txt', 'a')
        #a = str(country + "\n" + deaths_total + "\n" + deaths_today + "\n" + cases_total + "\n" + cases_today + "\n" + recovered_total + "\n" + critical_total)
        #f.write(a)
        #f.close()
        
while True:
    executeSomething()
    time.sleep(0)
