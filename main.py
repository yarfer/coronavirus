import requests
import telebot
from bs4 import BeautifulSoup as BS
from googletrans import Translator
import os
import time

chat_ids_file = 'info.txt'

Token = '964961040:AAHsjR41UEAq1P-aY7ZRCZy5d0dLvLMzTGI'
bot = telebot.TeleBot(Token)

translator = Translator()
url = "https://bnonews.com/index.php/the-latest-coronavirus-cases/"
try:
    @bot.message_handler(commands=['info'])
    def start(message):
        try:
            os.remove(chat_ids_file)
        except:
            pass
        inf = requests.get(url)
        html = BS(inf.text, 'lxml')
        infog = str(html.find("table", class_='wp-block-table aligncenter is-style-stripes').find_all("tr")[-1])
        inforg = infog.replace("<tr><td><strong>TOTAL</strong></td><td><strong>", "").replace("</strong></td><td></td><td></td></tr>", "").replace("</strong></td><td><strong>", "__").replace(",", "")
        informg = "Китай: Заражено - " + inforg.split("__")[0] + "   Умерло - " + inforg.split("__")[1]


        info = html.find_all("table", class_='wp-block-table is-style-regular')[1].find_all("tr")
        for asd in info:
            asdf = str(asd)
            asdfg = asdf.replace('</td>', '__</td>')
            htmla = BS(asdfg, 'lxml')
            sea = htmla.text
            gfjdsk = str(sea.split("__")[0])
            tra = translator.translate(gfjdsk, src='en', dest='ru')
            gfd = str(tra)
            sdf = gfd.split(' text=')[1].split(", pronunciation")[0]
            inform = sdf + ": Заражено - " + sea.split("__")[1] + "   Умерло - " + sea.split("__")[2]
            fesd = inform.replace("МЕЖДУНАРОДНЫЙ: Заражено - Cases   Умерло - Deaths", informg)
            hre = str(fesd.split('КОЛИЧЕСТВО:')[0].replace("ОБЩЕЕ ", ""))
            with open(chat_ids_file, "a+") as ids_file:
                ids_file.seek(0)
                ids_list = [line.split('\n')[0] for line in ids_file]
                num1 = hre
                if num1 not in ids_list:
                    ids_file.write(f'' + num1 + '\n')
                    ids_list.append(num1)
        doc = open(chat_ids_file)
        asder = doc.read()
        asw = asder.strip()
        bot.send_message(message.chat.id, asw)
except:
    print("Помилка")
bot.polling(none_stop=True)