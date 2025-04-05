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
    bot.send_message(message.chat.id,'''🎓 Команды моего бота — твоего карьерного помощника:
💬 /start – запускает нашего бота и знакомит тебя с его возможностями. Узнай, как он может помочь тебе найти путь в мире профессий!
📝 /add Имя Возраст Интересы – заполни свой профиль. Расскажи немного о себе, и я подберу направления, в которых ты сможешь реализовать себя наилучшим образом.
🔍 /prof – на основе твоего профиля я предложу тебе список профессий, которые идеально подойдут твоим интересам и навыкам.
✨ Не стесняйся использовать команды – я здесь, чтобы помочь тебе сделать уверенный шаг в будущее!
''')
@bot.message_handler(commands=['add'])
def adduser(message):
    data = message.text.split('/add')[1].strip().split()
    TG.add_user(message.chat.id,data[0],data[1],data[2])
@bot.message_handler(commands=['prof'])
def profession(message):
    user = TG.get_user(message.chat.id)
    text = TG.get_career_advice(user[4])
    
    bot.send_message(message.chat.id,f'Тебе подходят эти профессии:{text}')

if __name__ == "__main__":
    
    bot.polling(none_stop=True)
