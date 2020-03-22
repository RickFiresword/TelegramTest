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

    #==================24H stats /start=====================#
    handle2 = open("Day_stats.txt", "r")
    data2 = handle2.read().splitlines()
    
    qqq = datetime.now().strftime('%H:%M')
    qqq1 = datetime.now()
    qqq_day = str(qqq1.day)
    qqq_month = str(qqq1.month)
    
    ttime = requests.get(url).text
    soup2 = BeautifulSoup(ttime, features="html.parser")
    deaths_global_all = soup2.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[0].get_text()
    deaths_global_all = str("".join(deaths_global_all.split()))

    deaths_global_today = soup2.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[1].get_text()
    deaths_global_today = str("".join(deaths_global_today.split())).replace('+','')

    cases_global_today = soup2.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[2].get_text()
    cases_global_today = str("".join(cases_global_today.split())).replace('+','')

    cases_global_all = soup2.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[3].get_text()
    cases_global_all = str("".join(cases_global_all.split()))

    critial_global_all = soup2.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[4].get_text()
    critial_global_all = str("".join(critial_global_all.split()))

    affected_global_all = soup2.findAll("h3", {'style': 'color:red; font-weight:900; font-size:25px'})[5].get_text()
    affected_global_all = str("".join(affected_global_all.split()))
    
    
    if qqq == '20:47' and int(data2[2]) != int(deaths_global_today):
        print('q++++++++++++++')
        bot.sendMessage(chat_id=my_telegram_chat_id, text=('➖➖➖ Day stats: ' + qqq_day + ' / ' +qqq_month + ' / 2020➖➖➖ '+ '\n\n💀️ WORLD Deaths Today: '+ deaths_global_today + '\n🚑️ WORLD Cases Today: ' + cases_global_today + '\n\n •••\n\n☠️ Total WORLD Deaths: '+ deaths_global_all + '\n🏥 Total WORLD Cases: ' + cases_global_all + '\n⚡ Total WORLD Critical: '+ critial_global_all + '\n🌍 Affected Countries: '+ affected_global_all + "\n ➖➖➖➖🦠➖➖➖➖"))
        
    else:
        print ('nope')
    
    #==================24H stats /end=====================#
    
    
    
    #==================Main Stats====================#
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
        #==================Main Stats====================#
        
                
        # чтение файла
        handle = open(country+'.txt', "r")
        data = handle.readlines()


        if int(data[1]) == int(deaths_total):
            print(country + ' Deaths total not changed')

        else:
            print(country + ' Deaths changed ---------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('💀️' + " New deaths (+" + str((int(deaths_total) - int(data[1]))) +") in #"+ country + ". \n\n Deaths Today: " + deaths_today + "\n Total Deaths: " + deaths_total + "\n ➖➖➖➖🦠➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            #f.close()
            
            
            with open('2001-0.txt','r', encoding='utf-8') as fin:
                a = fin.readlines()[1]
            #=======5H STATS========
            #old_data = int(ff[1])
            
                h5_deaths = str((int(deaths_total) - int(data[1])))
            
                gg = int(a) + int(h5_deaths)

            
                lines[1] = str(gg) + "\n"

            # Закрываем файл
                ff.close()
            f.close()

            # Открываем файл для записи
            save_changes = open('2001-0.txt', 'w')

            # Сохраняем список строк
            save_changes.writelines(lines)

            # Закрываем файл
            save_changes.close()
            

        if int(data[3]) == int(cases_total):
            print(country + ' Infected not changed')

        else:
            print(country + ' Infected changed ---------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('🚑️' +" New cases (+" + str((int(cases_total) - int(data[3]))) +") in #"+ country + ". \n\n Cases Today: " + cases_today + "\n Total Cases: " + cases_total + "\n ➖➖➖➖🦠➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            #f.close()
            
            
            with open('2001-0.txt','r', encoding='utf-8') as fin:
                a = fin.readlines()[0]
            #=======5H STATS========
            #old_data = int(ff[1])
            
                h5_cases = str((int(cases_total) - int(data[3])))
            
                gg = int(a) + int(h5_cases)

            
                a = str(gg) + "\n"

            # Закрываем файл
                
            f.close()

            # Открываем файл для записи
            save_changes = open('2001-0.txt', 'w')

            # Сохраняем список строк
            save_changes.writelines(a)

            # Закрываем файл
            save_changes.close()

        if int(data[5]) == int(recovered_total):
            print(country + ' Recovered not changed')

        else:
            print(country + ' Recovered changed ---------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('💊️' +" New recovered (+" + str((int(recovered_total) - int(data[5]))) +") in #"+ country + ". \n\n Total Recovered: " + recovered_total + "\n ➖➖➖➖🦠➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()

        if int(data[6]) == int(critical_total):
            print(country + ' Critical not changed')

        else:
            print(country + ' Critical changed ----------------------------')

            bot.sendMessage(chat_id=my_telegram_chat_id, text=('⚡' +" New critical (+" + str((int(critical_total) - int(data[6]))) +") in #"+ country + ". \n\n Total Critical: " + critical_total + "\n ➖➖➖➖🦠➖➖➖➖"))
            # ЗАПИСЬ в файл начало
            f = open(country + '.txt', 'w')
            a = str(country + "\n" + deaths_total + "\n"  + deaths_today + "\n"  + cases_total + "\n"  + cases_today + "\n"  + recovered_total + "\n"  + critical_total)
            f.write(a)
            f.close()
            
            
        
        time.sleep(0)
        #bot.send_message(chat_id=my_telegram_chat_id, text=ttt)
        
        # tests
        
        #f = open(country + '.txt', 'w')
        
        # ЗАПИСЬ в файл начало
        #f = open(country + '.txt', 'a')
        #a = str(country + "\n" + deaths_total + "\n" + deaths_today + "\n" + cases_total + "\n" + cases_today + "\n" + recovered_total + "\n" + critical_total)
        #f.write(a)
        #f.close()
    print("ONE CIRLCE DONE=============================#")    
while True:
    executeSomething()
    time.sleep(0)
