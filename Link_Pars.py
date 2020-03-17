#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys

from telepot import loop
from importlib import reload
reload(sys)

import requests
from bs4 import BeautifulSoup
import telebot
import time
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials


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


        virus = "🦠"
        virus1 = virus.encode('utf-8')
        virus2 = virus1.decode('ISO-8859-1')
        #virus2
        
        skull = "💀️"
        skull1 = skull.encode('utf-8')
        skull2 = skull1.decode('ISO-8859-1')
        #skull2
        
        emerg = "🚑️"
        emerg1 = emerg.encode('utf-8')
        emerg2 = emerg1.decode('ISO-8859-1')
        #Emerg
        
        drug = "💊️"
        drug1 = drug.encode('utf-8')
        drug2 = drug1.decode('ISO-8859-1')
        #Drug2
        
        light = "⚡"
        light1 = light.encode('utf-8')
        light2 = light1.decode('ISO-8859-1')
        #light2 
        
        point = "•"
        point1 = point.encode('utf-8')
        point2 = point1.decode('ISO-8859-1')
        #point2
        
        line = "➖"
        line1 = line.encode('utf-8')
        line2 = line1.decode('ISO-8859-1')
        #line2
        
        
        
        
        #ttt = (virus2 + "Country: #" + country + "\n"+point2+"\n"+skull2+" Total Deaths: " + deaths_total + "\nDeaths Today: " + deaths_today + "\n"+point2+point2+"\n"+emerg2+" Total Cases: " + cases_total + "\nCases Today: " + cases_today + "\n"+point2+point2+point2+"\n"+drug2+" Total Recovered: " + recovered_total + "\n"+light2+" Total Critical: " + critical_total + "\n "+line2+line2+line2+line2+line2")

        
        # чтение файла
        handle = open(country + '.txt', "r")
        data = handle.readlines()

        if str(data[0]) == str(country):
            print('Country not changed')
        else:
            print('Country changed ---------------------------')    


        if int(data[1]) == int(deaths_total):
            print('Deaths total not changed')
            
        else:
            print('Deaths changed ---------------------------')

            bot.send_message(chat_id=my_telegram_chat_id, text=(skull2+" New death (+" + str((int(deaths_total) - int(data[1]))) +") in #"+ country + ". \n Deaths Today: " + deaths_today + "\n Total Deaths: " + deaths_total))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[3]) == int(cases_total):
            print('Infected not changed')
            
        else:
            print('Infected changed ---------------------------')

            bot.send_message(chat_id=my_telegram_chat_id, text=(emerg2+" New case (+" + str((int(cases_total) - int(data[3]))) +") in #"+ country + ". \n Cases Today: " + cases_today + "\n Total Cases: " + cases_total))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[5]) == int(recovered_total):
            print('Recovered not changed')
            
        else:
            print('Recovered changed ---------------------------')

            bot.send_message(chat_id=my_telegram_chat_id, text=(drug2+" New recovered (+" + str((int(recovered_total) - int(data[5]))) +") in #"+ country + ". \n Total Recovered: " + recovered_total))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[6]) == int(critical_total):
            print('Critical not changed')
            
        else:
            print('Critical changed ----------------------------')

            bot.send_message(chat_id=my_telegram_chat_id, text=(light2+" New critical (+" + str((int(critical_total) - int(data[6]))) +") in #"+ country + ". \n Total Critical: " + critical_total))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()



        time.sleep(0)
        #bot.send_message(chat_id=my_telegram_chat_id, text=ttt)

        
        # tests
        '''
        f = open(country + '.txt', 'w')
    
        # ЗАПИСЬ в файл начало
        f = open(country + '.txt', 'a')
        a = str(country + "\n" + deaths_total + "\n" + deaths_today + "\n" + cases_total + "\n" + cases_today + "\n" + recovered_total + "\n" + critical_total)
        f.write(a)
        f.close()
        '''
executeSomething()

#while True:
#    executeSomething()
#    time.sleep(0)
