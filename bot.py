import telebot
from config import TOKEN
import time
from logic import CareerAdvisorBot


bot = telebot.TeleBot(TOKEN)
TG = CareerAdvisorBot()

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id,'''Привет!  Добро пожаловать в "Советчик по выбору карьеры"!
Я помогу тебе найти подходящую профессию, исходя из твоих интересов, навыков и предпочтений. 
📌 Как я могу помочь?
🔹 Предложу профессии, которые подойдут тебе
🔹 Подскажу, какие навыки развивать
🔹 Дам советы по обучению и поиску работы''')
@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id,'ТУТ НУЖНО НАПИСАТЬ КОМАНДЫ КОТОРЫЕ У БОТА БУДУТ')
@bot.message_handler(commands=['add'])
def adduser(message):
    data = message.text.split('/add')[1].strip().split()
    TG.add_user(message.chat.id,data[0],data[1],data[2])




if __name__ == "__main__":
    
    bot.polling(none_stop=True)
