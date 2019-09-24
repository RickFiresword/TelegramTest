#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import telebot
# import constant
import urllib
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException



token_i = '27503-8p5YVDjl6dBrY7'

my_telegram_chat_id = '-328568838'

url = 'http://m.scorebing.com/live'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'
}

token = '399177903:AAGgSX7V3G8vRyPpC_IaAWH9Q9JaHNMDJV0'
sndmsg = '/sendMessage?'
chat_id = "message.from_user.id"
chat_text = "&text="

bot = telebot.TeleBot(token)

links = []

def executeSomething():
    #====
    links = []

    chromedriver = '/Users/rick_firesword/Downloads/chromedriver'

    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    time.sleep(3)

    get_links = driver.find_elements_by_xpath('/html/body/div/div/div[1]/main/div/div/div/div/div/a')
    # code here
    for i in get_links:
        a = (i.get_attribute('href'))
        a = a.replace('http://m.scorebing.com/match/', 'http://m.scorebing.com/match_live/')
        link = {
            'href': a
        }
        links.append(link)
        # print link

    for j in links:
        driver.get(j['href'])

        try:
            # =======================/CORNERS/============================
            driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[2]/a[1]").click()
            corner_home = driver.find_element_by_xpath(
                "/html/body/div/div/div[1]/main/div[1]/div/div[1]/h5/span[2]").text
            corner_away = driver.find_element_by_xpath(
                "/html/body/div/div/div[1]/main/div[1]/div/div[3]/h5/span[1]").text
            if ':' not in corner_home:
                corner_home = corner_home
            else:
                corner_home = 0

            if ':' not in corner_away:
                corner_away = corner_away
            else:
                corner_away = 0
            corner_total = int(corner_home) + int(corner_away)
            corner_home = str(corner_home)
            corner_away = str(corner_away)
            corner_total = str(corner_total)
            corner_total_text = "Corners: " + corner_home + ' - ' + corner_away + '  ( Total = ' + corner_total + ' )'

            # =======================/onTarget/============================

            onTarget_home = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[1]/div/div[1]").text
            onTarget_away = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[1]/div/div[3]").text
            onTarget_total = int(onTarget_home) + int(onTarget_away)
            onTarget_home = str(onTarget_home)
            onTarget_away = str(onTarget_away)
            onTarget_total = str(onTarget_total)
            onTarget_total_text = 'On Target: ' + onTarget_home + " - " + onTarget_away + '  ( Total = ' + onTarget_total + ' )'

            # =======================/offTarget/============================

            offTarget_home = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[2]/div/div[1]").text
            offTarget_away = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[2]/div/div[3]").text
            offTarget_total = int(offTarget_home) + int(offTarget_away)
            offTarget_home = str(offTarget_home)
            offTarget_away = str(offTarget_away)
            offTarget_total = str(offTarget_total)
            offTarget_total_text = 'Off Target: ' + offTarget_home + " - " + offTarget_away + '  ( Total = ' + offTarget_total + ' )'

            # =======================/Attacks/============================

            attacks_home = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[3]/div/div[1]").text
            attacks_away = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[3]/div/div[3]").text
            attacks_total = int(attacks_home) + int(attacks_away)
            attacks_home = str(attacks_home)
            attacks_away = str(attacks_away)
            attacks_total = str(attacks_total)
            attacks_total_text = 'Simple Attacks: ' + attacks_home + " - " + attacks_away + '  ( Total = ' + attacks_total + ' )'

            # =======================/Dang Attack/============================

            dang_attacks_home = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[4]/div/div[1]").text
            dang_attacks_away = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[3]/div[4]/div/div[3]").text
            dang_attacks_total = int(dang_attacks_home) + int(dang_attacks_away)
            dang_attacks_home = str(dang_attacks_home)
            dang_attacks_away = str(dang_attacks_away)
            dang_attacks_total = str(dang_attacks_total)
            dang_attacks_total_text = 'Dangerous Attacks: ' + dang_attacks_home + " - " + dang_attacks_away + '  ( Total = ' + dang_attacks_total + ' )'


            # =======================/The Time/============================
            the_time = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[1]/div/div[2]/div/h4").text
            the_time = the_time.replace("'", "")
            the_time = str(the_time)
            the_time_text = "Time: " + the_time + "'"

            # =======================/Scrore/============================
            score_home = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[1]/div/div[2]/div/h2").text
            score_away = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[1]/div/div[2]/div/h2").text
            score = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[1]/div/div[2]/div/h2").text
            score_home = re.sub(' .*', '', score_home, flags=re.DOTALL)
            score_away = "".join([char for num, char in enumerate(score_away) if num != 2])
            score_away = "".join([char for num, char in enumerate(score_away) if num != 0])
            score_away = "".join([char for num, char in enumerate(score_away) if num != 1])
            score_away = "".join([char for num, char in enumerate(score_away) if num != 2])
            score_total = int(score_home) + int(score_away)

            score_teams = "Score: " + score_home + " - " + score_away

            if score_total == 0:
                bet_tip = "Bet 0,5 OVER --->"
            elif score_total == 1:
                bet_tip = "Bet 1,5 OVER --->"
            elif score_total == 2:
                bet_tip = "Bet 2,5 OVER --->"
            elif score_total == 3:
                bet_tip = "Bet 3,5 OVER --->"
            else:
                bet_tip = "No bet. Too much goals... --->"

            # =======================/Name TEAMS/============================
            team_home = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[1]/div/div[1]/h3/a").text
            team_away = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/div[1]/div/div[3]/h3/a").text
            league_name = driver.find_element_by_xpath("/html/body/div/div/div[1]/main/h3/a[3]").text
            league_name = 'Legue: ' + str(league_name)
            team_text = 'Teams: ' + str(team_home) + ' - ' + str(team_away)
            team_text = str(team_text)


            #======================/ BETA CHANCE / ======================

            q_time = the_time
            q_time = (q_time)
            if q_time > '13' and q_time < '16':
                q_time = 1.3
            elif q_time > '0' and q_time < '13':
                q_time = 1.8
            elif q_time > '15' and q_time < '19':
                q_time = 1.2
            elif q_time > '18' and q_time < '23':
                q_time = 1.1
            elif q_time > '23' and q_time < '26':
                q_time = 1
            elif q_time > '25' and q_time < '33':
                q_time = 0.8
            elif q_time > '32' and q_time < '37':
                q_time = 0.5
            elif q_time > '36' and q_time < '45':
                q_time = 0.1
            else:
                q_time = 1

            print q_time
            chance_bet = ((int(dang_attacks_total)*1.4) + (int(attacks_total)*0.05) + (int(onTarget_total)*8) + (int(offTarget_total)*2) + (int(corner_total)*1.2))*q_time

            if chance_bet > 85:
                chance_bet = '85+ %'
            chance_bet = str(chance_bet)


            total_stats_chat = " /----------------------------" + "\n" + league_name + "\n" + team_text + "\n" + "-" + "\n" + score_teams + "\n" + the_time_text + "\n" + "-" + "\n" + attacks_total_text + "\n" + dang_attacks_total_text + "\n" + onTarget_total_text + "\n" + offTarget_total_text + "\n" + corner_total_text + "\n" + '=' + "\n" + bet_tip + "\n" + '(Beta) Chance: >' + chance_bet + "\n" "----------------------------\ "

            if '-' in the_time:
                pass

            if (the_time >= '13' and the_time <= '24') and (dang_attacks_total > '15') and (onTarget_total > '1'):
                bot.send_message(chat_id=my_telegram_chat_id, text=total_stats_chat)

            else:
                print ('___ не удовлетворяет условиям! ___' + '\n' + '---------------------')

        except NoSuchElementException:
            pass
            print ('!!! Некоторые данные отсутствуют !!!' + '\n' + '---------------------')


    driver.close()
    time.sleep(1)

while True:
    executeSomething()

