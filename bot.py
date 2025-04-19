import telebot
from config import TOKEN
import time
from logic import CareerAdvisorBot
from telebot import types


bot = telebot.TeleBot(TOKEN)
TG = CareerAdvisorBot()


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("/help")
    markup.add(btn2)
    return markup

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id,'''Привет!  Добро пожаловать в "Советчик по выбору карьеры"!
Я помогу тебе найти подходящую профессию, исходя из твоих интересов, навыков и предпочтений. 
📌 Как я могу помочь?
🔹 Предложу профессии, которые подойдут тебе
🔹 Подскажу, какие навыки развивать
🔹 Дам советы по обучению и поиску работы''',reply_markup=main_menu())
    

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id,'''🎓 Команды моего бота — твоего карьерного помощника:
💬 /start – запускает нашего бота и знакомит тебя с его возможностями. Узнай, как он может помочь тебе найти путь в мире профессий!
📝 /add Имя Возраст Интересы – заполни свой профиль. Расскажи немного о себе, и я подберу направления, в которых ты сможешь реализовать себя наилучшим образом.
🔍 /prof – на основе твоего профиля я предложу тебе список профессий, которые идеально подойдут твоим интересам и навыкам.
🔑 /desc Название Профессии - расскажу тебе об интересующей тебя профессии.
✨ Не стесняйся использовать команды – я здесь, чтобы помочь тебе сделать уверенный шаг в будущее!
''',reply_markup=main_menu())
    

@bot.message_handler(commands=['add'])
def adduser(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("/prof",callback_data='btn1')
    markup.add(btn1)
    data = message.text.split('/add')[1].strip().split()
    TG.add_user(message.chat.id,data[0],data[1],data[2])
    bot.send_message(message.chat.id,'Нажми чтобы увидеть рекомендации к профессии',reply_markup=markup)



@bot.message_handler(commands=['prof'])
def profession(message):
    user = TG.get_user(message.chat.id)
    text = TG.get_career_advice(user[4])
    bot.send_message(message.chat.id,text,reply_markup=main_menu())


@bot.message_handler(commands=['desc'])
def profession(message):
    data = message.text.split('/desc')[1].strip()
    text = TG.get_prof_desc(data)
    bot.send_message(message.chat.id,text,reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "btn1":
        user = TG.get_user(call.message.chat.id)
        text = TG.get_career_advice(user[4])
        bot.send_message(call.message.chat.id,text,reply_markup=main_menu())



if __name__ == "__main__":
    bot.delete_webhook()
    bot.polling(none_stop=True)
