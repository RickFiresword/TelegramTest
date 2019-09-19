#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import telebot
# import constant
import urllib
import time




token_i = '27503-8p5YVDjl6dBrY7'

#my_telegram_chat_id = 297439048
my_telegram_chat_id = '-328568838'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'
}

token = '399177903:AAGgSX7V3G8vRyPpC_IaAWH9Q9JaHNMDJV0'
sndmsg = '/sendMessage?'
chat_id = "message.from_user.id"
chat_text = "&text="

bot = telebot.TeleBot(token)

url = 'https://bsportsfan.com/ci/soccer'
page = requests.get(url, headers=headers)

time.sleep(5)
soup = BeautifulSoup(page.text, 'html.parser')
main_page = soup.prettify()

# ====/Create valid link======

http_add = 'http://betsapi.com/'
match_id = 'r/234234234234'


def valid_link(x, y):
    return x + y


# =====/Find all match links ======

get_links = soup.findAll('a', attrs={'href': re.compile("^/r/")})
time.sleep(5)
def executeSomething():
    # code here
    def parse_link(link):
        print(link)
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        time.sleep(4)
        try:
            score = soup.find('span', {'class': 'text-danger'})
            the_time = soup.findAll(class_='race-time')[0]
            the_time_text = str(the_time.text).replace("'", '').replace(" ", '').replace("\n", '')

            #====
            name_home = soup.find_all(class_="breadcrumb-item active")[0]

            simple_attack_home = soup.find_all(class_='sr-only')[0]
            simple_attack_away = soup.find_all(class_="sr-only")[1]
            dang_attack_home = soup.find_all(class_="sr-only")[2]
            dang_attack_away = soup.find_all(class_="sr-only")[3]
            onTarget_attack_home = soup.find_all(class_="sr-only")[4]
            onTarget_attack_away = soup.find_all(class_="sr-only")[5]
            offTarget_attack_home = soup.find_all(class_="sr-only")[6]
            offTarget_attack_away = soup.find_all(class_="sr-only")[7]

            #====

            dang_attack_home_score_text = dang_attack_home.text
            dang_attack_away_score_text = dang_attack_away.text
            simple_attack_home_score_text = simple_attack_home.text
            simple_attack_away_score_text = simple_attack_away.text
            onTarget_attack_home_score_text = onTarget_attack_home.text
            onTarget_attack_away_score_text = onTarget_attack_away.text
            offTarget_attack_home_score_text = offTarget_attack_home.text
            offTarget_attack_away_score_text = offTarget_attack_away.text

            name_home_text = name_home.text.replace('     ', '').replace('\n', '').replace('  ', '').replace('   ', '')
            score_text = score.text.replace('     ', '').replace('\n', '').replace('  ', '').replace('   ', '')

            dang_attack_total = int(dang_attack_home_score_text) + int(dang_attack_away_score_text)
            simple_attack_total = int(simple_attack_home_score_text) + int(simple_attack_away_score_text)
            onTarget_attack_total = int(onTarget_attack_home_score_text) + int(onTarget_attack_away_score_text)
            offTarget_attack_total = int(offTarget_attack_home_score_text) + int(offTarget_attack_away_score_text)
            chance_bet = (dang_attack_total*0.2 + simple_attack_total*7.8 + onTarget_attack_total*15 + offTarget_attack_total*70)/10
            if chance_bet > 85:
                chance_bet = '85+'
            chance_bet = str(chance_bet)


            if (the_time_text > '14' and the_time_text < '24') and (dang_attack_total > 20 ) and (onTarget_attack_total > 1 ):

                dang_attack_total_score = 'Dangerous Attacks: ' + dang_attack_home.text + " - " + dang_attack_away.text + '  ( Total = ' + str(dang_attack_total) + ' )'
                simple_attack_total_score = "Simple Attacks: " + simple_attack_home.text + " - " + simple_attack_away.text + '  ( Total = ' + str(simple_attack_total) + ' )'
                onTarget_attack_total_score = "On Target: " + onTarget_attack_home.text + " - " + onTarget_attack_away.text + '  ( Total = ' + str(onTarget_attack_total) + ' )'
                offTarget_attack_total_score = "OFF Target: " + offTarget_attack_home.text + " - " + offTarget_attack_away.text + '  ( Total = ' + str(offTarget_attack_total) + ' )'

                name_teams = "Teams: " + name_home_text.replace(' v ', ' - ')
                score_teams = "Score: " + score_text
                time_now = 'Time: ' + the_time_text + " '"

                if score_text[0] == '0' and score_text[2] == '0':
                    bet_tip = "Bet 0,5 OVER --->"
                elif score_text[0] == '1' and score_text[2] == '0':
                    bet_tip = "Bet 1,5 OVER --->"
                elif score_text[0] == '0' and score_text[2] == '1':
                    bet_tip = "Bet 1,5 OVER --->"
                elif score_text[0] == '2' and score_text[2] == '0':
                    bet_tip = "Bet 2,5 OVER --->"
                elif score_text[0] == '0' and score_text[2] == '2':
                    bet_tip = "Bet 2,5 OVER --->"
                elif score_text[0] == '1' and score_text[2] == '1':
                    bet_tip = "Bet 2,5 OVER --->"
                elif score_text[0] == '2' and score_text[2] == '1':
                    bet_tip = "Bet 3,5 OVER --->"
                elif score_text[0] == '1' and score_text[2] == '2':
                    bet_tip = "Bet 3,5 OVER --->"
                else:
                    bet_tip = "No bet. Too much goals... --->"

                total_stats_chat = " /----------------------------" + "\n" + link + "\n" + "-" + "\n" + name_teams + "\n" + score_teams + '\n' + time_now + "\n" + '-' + "\n" + simple_attack_total_score + "\n" + dang_attack_total_score + "\n" + onTarget_attack_total_score + "\n" + offTarget_attack_total_score + "\n" + "=====" + "\n" + bet_tip + "\n" + "(Beta) Chance  > " + chance_bet + "%" + "\n" + "----------------------------\ "
                bot.send_message(chat_id=my_telegram_chat_id, text=total_stats_chat)


            else:
                print ('___ не удовлетворяет условиям! ___' + '\n' + '---------------------')
        except:
            pass
            print ('!!! Некоторые данные отсутствуют !!!' + '\n' + '---------------------')
        # print(link)


    count = 0
    for link in get_links:
        count += 1
        link = str(link)
        link = link.replace('<a href="/', http_add)
        link = re.sub('" id=".*', '', link, flags=re.DOTALL)
        link = "".join(map(str, link))
        parse_link(link)
        time.sleep(2)

        if count == 500:
            break

    time.sleep(450)

while True:
    executeSomething()

