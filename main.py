import telebot, datetime, schedule

BOT_TOKEN = 'ТАЙНА, ПОКРЫТАЯ МРАКОМ'
YEAR = 2024
MONTH = 11
DAY = 17

bot = telebot.TeleBot(BOT_TOKEN)
karaoke_date = datetime.date(year=YEAR, month=MONTH, day=DAY)


@bot.message_handler(commands=['start'])
def start_timer(message):
    today = datetime.date.today()
    schedule.every().day.at("17:30").do(generic_message, message)

    while today <= karaoke_date:
        schedule.run_pending()


def generic_message(message):
    chat_id = message.chat.id
    today = datetime.date.today()
    remain = (karaoke_date - today).days

    if remain == 0:
        bot.send_message(chat_id=chat_id, text='караоке сегодня ура ура ура')
    elif remain % 10 == 1 and remain != 11:
        bot.send_message(chat_id=chat_id, text='до караоке остался %s день!!' % remain)
    elif 2 <= remain % 10 <= 4 and remain not in [12, 13, 14]:
        bot.send_message(chat_id=chat_id, text='до караоке осталось %s дня!' % remain)
    else:
        bot.send_message(chat_id=chat_id, text='до караоке осталось %s дней!' % remain)


bot.infinity_polling()
