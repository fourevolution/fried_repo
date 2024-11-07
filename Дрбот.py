import telebot

# Вставьте ваш токен
TOKEN = '7848406588:AAHgVwvrP0V0WN1V1UmtCHHZq1al2LUFIAo'
bot = telebot.TeleBot(TOKEN)

# Команда /start


@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "👋 Добро пожаловать в бот ДРУГ | ушасто-хвостатое пространство! Мы — познавательно-развлекательное пространство для владельцев и любителей животных в г. Севастополе.\n"
        "Наша миссия — создать инклюзивное сообщество!\n\n"
        "Вот список доступных команд:\n"
        "/info - Узнать больше о нашем проекте\n"
        "/courses - Информация о платных и бесплатных курсах\n"
        "/events - Запланированные мероприятия\n"
        "/volunteer - Как стать волонтером\n"
        "/feedback - Оставить отзыв\n"
        "/contact - Связаться с нами\n"
        "/developer - Связаться с разработчиком\n"
        "/salutariness - Получить полезные материалы"
    )
    bot.reply_to(message, welcome_text)

# Команда /info


@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message,
                 "🏠 Наша идея заключается в создании пространства, которое предлагает курсы и мероприятия для владельцев домашних животных и людей с ограниченными возможностями здоровья.\n"
                 "🌱 Принципы: доступность, практикоориентированность, инклюзивность."
                 )

# Команда /courses


@bot.message_handler(commands=['courses'])
def courses(message):
    bot.reply_to(message,
                 "📚 Образовательные курсы:\n"
                 "1. Платные курсы для владельцев животных:\n"
                 "- Здоровье и питание\n"
                 "- Поведение и воспитание\n"
                 "- Уход за животными и прочее\n"
                 "- Индивидуальные и групповые тренировки\n"
                 "- Проведение зоотерапии, мастер-классов, лекций и др.\n\n"
                 "2. Бесплатные курсы для людей с ОВЗ:\n"
                 "- Регулярные выездные мероприятия в приюты\n"
                 "- Мероприятия для людей с ОВЗ\n"
                 "- Поддержка и помощь людям с ОВЗ\n"
                 "- Мероприятия с лекцией"
                 )

# Команда /events


@bot.message_handler(commands=['events'])
def events(message):
    bot.reply_to(message,
                 "🎉 Запланированные мероприятия:\n"
                 "- 8 ноября — Мероприятие с лекцией от зоопсихолога"
                 )

# Команда /volunteer


@bot.message_handler(commands=['volunteer'])
def volunteer(message):
    bot.reply_to(message,
                 "🤝 Хотите стать волонтером? Мы всегда рады помощи!\n"
                 "Участвуйте в наших мероприятиях и помогайте животным в приютах.\n"
                 "Свяжитесь с нами, чтобы узнать, как вы можете помочь!"
                 )

# Команда /feedback


@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.reply_to(message,
                 "💬 Мы будем рады вашему отзыву! Пожалуйста, оставьте свои мысли о нашем проекте или предложениях по улучшению."
                 )

# Команда /contact


@bot.message_handler(commands=['contact'])
def contact(message):
    bot.reply_to(message,
                 "📞 Связаться с нами:\n"
                 "- Email: contact.drug.sev@gmail.com\n"
                 "- Телефон: +79785622599"
                 )

# Команда /developer


@bot.message_handler(commands=['developer'])
def developer(message):
    bot.reply_to(message,
                 "👨‍💻 Связаться с разработчиком:\n"
                 "- Email: andfewam0507@gmail.com\n"
                 "- Telegram: @Chmil53"
                 )

# Команда /salutariness


@bot.message_handler(commands=['salutariness'])
def salutariness(message):
    # Подпись для файлов
    caption = (
        "Благодарим Вас за участие в лекции! Вот обещанные чек-листы о неочевидных признаках болезней у собак и котов.\n"
        "Надеемся, что Ваши мокроносы проиграют в этом бинго 🐶🐱\n\n"
        "Также, наша команда будет очень рада, если Вы оставите отзыв о прошедшей лекции. "
        "Сделать это можно, воспользовавшись командой /feedback\n"
        "До новых встреч!"
    )
#e_qbLmSR6VuYw+
e_qbLmSR6VuYw+
    # Отправка документов
    with open('2.jpg', 'rb') as dog_file, open('1.jpg', 'rb') as cat_file:
        bot.send_document(message.chat.id, dog_file,
                          caption="Чек-лист: неочевидные признаки болезней у собак")
        bot.send_document(message.chat.id, cat_file,
                          caption="Чек-лист: неочевидные признаки болезней у котов")

    # Отправка общей подписи
    bot.send_message(message.chat.id, caption)

# Обработчик всех остальных сообщений (ответ по умолчанию)


@bot.message_handler(func=lambda message: True)
def default_response(message):
    bot.reply_to(message,
                 "🌟Спасибо, что вы с нами! Давайте вместе создавать дружное и заботливое сообщество!"
                 )


# Запуск бота
if __name__ == '__main__':
    print("Бот запущен!")
    bot.polling(none_stop=True)
