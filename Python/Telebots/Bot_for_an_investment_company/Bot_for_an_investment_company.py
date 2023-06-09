import telebot, os, sys
from telebot import types
import pymysql

bot = telebot.TeleBot('TOKEN')

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="NiK_26052008",
    db="telegramm",
    autocommit=True
)

cursor = conn.cursor()

@bot.message_handler(content_types=['text'])
def start(message):
    global keyboard
    if message.text == "/start":
        bot.send_message(message.from_user.id, 'Здаравствуйте, вы можете выбрать одну из кнопок в меню:')
        keyboard = types.InlineKeyboardMarkup()
        key_Objects = types.InlineKeyboardButton(text='Действующие объекты', callback_data='Objects')
        keyboard.add(key_Objects)
        key_Over_Objects = types.InlineKeyboardButton(text='Завершенные объекты', callback_data='Over_Objects')
        keyboard.add(key_Over_Objects)
        key_Types = types.InlineKeyboardButton(text='Варианты инвестирования', callback_data='Types')
        keyboard.add(key_Types)
        key_Call = types.InlineKeyboardButton(text='Связаться с менеджером', url='https://t.me/NerouN_Bro')
        keyboard.add(key_Call)
        key_My_Objects = types.InlineKeyboardButton(text='Мои объекты', callback_data='My_Objects')
        keyboard.add(key_My_Objects)
        question = "Выберите кнопку"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def processing_requests_from_buttons(call):
    global ob, o
    if call.data == "Objects":
        cursor.execute("SELECT area FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob = []
        ob.append(row2)
        cursor.execute("SELECT position FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT full_price FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT current_price FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT resale_price FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT projected_price_no_repair FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT projected_price_whith_repair FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT planned_profitability FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT yearly FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT implementation_period FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT amount_of_attraction FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        o = ob[7]
        bot.send_photo(call.message.chat.id, 'https://cdn.discordapp.com/attachments/801426522623836182/1121115222397177986/Object.png', u"\U0001F534 ПОИСК ИНВЕСТОРОВ \n \n \uE036 нежилое помещение площадью " + f"{ob[0]}" + u" на первом этаже жилого дома.\n \U0001F4CD Местоположение: " + f"{ob[1]}" + u"\n \n \uE12F Цена выкупа лота " + f"{ob[2]}" + u"\nЗатраты на продажу объекта в состоянии как есть составит приблизительно " + f"{3}" + "\nЗатраты на перепродажу с учетом ремонта оцениваются - " + f"{ob[4]}" + "\nПрогназируемая цена перепродажи без ремонта на текущий момент по нашим оценкам составляет " + f"{ob[5]}," + f" c ремонтом {ob[6]}" + u"\n \n\U0001F4A5 Планируемая доходность " + f"{ob[7]} ({ob[8]} Годовых)" + u"\n\u231B Ожидаемый срок реализации проекта " + f"{ob[9]}" + u"\n\u2705 Сумма привлечения от инвесторов до 50% общей суммы проекта: " + f"{ob[10]}" + u"\n\n\n\nЖдем информацию о вашем решении. Подробная презентация объекта \uE233\n\n\uE23A Написать менеджеру:@NerouN_Bro")
        keyboard = types.InlineKeyboardMarkup()
        key_vozmozh = types.InlineKeyboardButton(text='РАССЧИТАТЬ МОЙ ВОЗМОЖНЫЙ ДОХОД', callback_data='vozmozh')
        keyboard.add(key_vozmozh)
        question = "Выберите кнопку"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    if call.data == 'vozmozh':
        bot.send_message(call.message.chat.id, "Какую сумму вы хотите инвестировать?\n(отправьте только саму сумму без указаний типа 'руб.')")
        bot.register_next_step_handler(call.message, calc_doh)
    if call.data == 'Over_Objects':
        cursor.execute("SELECT area FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob = []
        ob.append(row2)
        cursor.execute("SELECT position FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT full_price FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT current_price FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT resale_price FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT projected_price_no_repair FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT projected_price_whith_repair FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT planned_profitability FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT yearly FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT implementation_period FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT amount_of_attraction FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        cursor.execute("SELECT iden FROM Invest_comp")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        ob.append(row2)
        o = ob[7]
        bot.send_photo(call.message.chat.id, 'https://cdn.discordapp.com/attachments/801426522623836182/1121115222397177986/Object.png', u"\U0001F534 ПОИСК ИНВЕСТОРОВ \n \n \uE036 нежилое помещение площадью " + f"{ob[0]}" + u" на первом этаже жилого дома.\n \U0001F4CD Местоположение: " + f"{ob[1]}" + u"\n \n \uE12F Цена выкупа лота " + f"{ob[2]}" + u"\nЗатраты на продажу объекта в состоянии как есть составит приблизительно " + f"{3}" + "\nЗатраты на перепродажу с учетом ремонта оцениваются - " + f"{ob[4]}" + "\nПрогназируемая цена перепродажи без ремонта на текущий момент по нашим оценкам составляет " + f"{ob[5]}," + f" c ремонтом {ob[6]}" + u"\n \n\U0001F4A5 Планируемая доходность " + f"{ob[7]} ({ob[8]} Годовых)" + u"\n\u231B Ожидаемый срок реализации проекта " + f"{ob[9]}" + u"\n\u2705 Сумма привлечения от инвесторов до 50% общей суммы проекта: " + f"{ob[10]}" + u"\n\n\n\nЖдем информацию о вашем решении. Подробная презентация объекта \uE233\n\n\uE23A Написать менеджеру:@NerouN_Bro")
        keyboard = types.InlineKeyboardMarkup()
        key_vozmozh = types.InlineKeyboardButton(text='РАССЧИТАТЬ МОЙ ВОЗМОЖНЫЙ ДОХОД', callback_data='vozmozh')
        keyboard.add(key_vozmozh)
        question = "Выберите кнопку"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    if call.data == 'Types':
        bot.send_message(call.message.chat.id, "Доверительное управление (ДУ)\n\nВы инвестируете деньги, а мы вкладываем их в выгодные сделки с теми объектами недвижимости, которые выберем сами\n\nПреимущества ДУ\n- низкий порог входа (от 300 000 рублей)\n- минимальные временные затраты на оформление — в течение 1 дня\n- не нужно ждать подходящую сделку, можно инвестировать в любой момент при появлении денежных средств\n- стабильная доходность — отсутствуют риски затягивания сроков реализации объекта\n\nОграничения ДУ\n- инвестор не является держателем залога\n- уровень доходности ниже, чем при инвестиционном займе или приобретении объекта на инвестора\n\nИнвестор получает:\n- 16 % годовых при сумме займа от 300 т.р. до 1 млн. рублей\n- 17 % годовых при сумме займа от 1 до 2,5 млн. рублей\n- 18 % годовых при сумме займа от 2,5 млн. рублей\n\nСредний доход инвестора 17% годовых")
        keyboard = types.InlineKeyboardMarkup()
        key_dogov = types.InlineKeyboardButton(text='ПОКАЗАТЬ ДОГОВОР', callback_data='dogov')
        keyboard.add(key_dogov)
        key_call = types.InlineKeyboardButton(text='СВЯЗАТЬСЯ С МЕНЕДЖЕРОМ',url='https://t.me/NerouN_Bro')
        keyboard.add(key_call)
        question = "Выберите кнопку"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
        bot.send_message(call.message.chat.id, "Инвестиционный займ\n\nМы занимаем у вас деньги. Мы привлекаем инвестиции для выкупа конкретного объекта недвижимости. Инвестор получает прибыль пропорционально вложенным средствам. Мы можем взять деньги в долг,если инвестор хочет получить гарантированную прибыль.\nУсловия:\nИнвестор получает 50% от чистой прибыли после реализации объекта ( = цена продажи объекта недвижимости – цена покупки – понесенные затраты на ремонт, ком. услуги, налоги и пр.)\n\nПример:\n1. Цена объекта 2 млн. рублей\n2. Инвестор вносит 1 млн. рублей\n3. Group Investing вносит 1 млн. рублей\n4. Цена продажи 3 млн. рублей\n5. Прибыль 1 млн. рублей делится пропорционально вложенным средствам - по 500 тыс. рублей\n6. Вычет комиссии Group Investing 50%\n7. Инвестор получает 250 тыс. рублей с вложенного 1 млн. рублей\n\nВложенный капитал приносит прибыль от 30% годовых. Мы берем себе часть прибыли за управление средствами, а наши инвесторы получают в cреднем 40% годовой доходности при их пассивном участии")
        keyboard = types.InlineKeyboardMarkup()
        key_dogov = types.InlineKeyboardButton(text='ПОКАЗАТЬ ДОГОВОР', callback_data='dogov')
        keyboard.add(key_dogov)
        key_call = types.InlineKeyboardButton(text='СВЯЗАТЬСЯ С МЕНЕДЖЕРОМ', url='https://t.me/NerouN_Bro')
        keyboard.add(key_call)
        question = "Выберите кнопку"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
        bot.send_message(call.message.chat.id, "Приобретение объекта на инвестора\nОбъект недвижимости оформляется на инвестора\n\nВ этом случае Инвестор получает право собственности на объект недвижимости, а его «доведением до ума» и реализацией занимаемся мы\n\nПреимущества:\n- риски минимальны, поскольку право собственности на недвижимость зарегистрировано за Инвестором, объект приобретен по цене, нижерыночной\n- более высокая гарантия в сравнении с 'доверительным управлением', 'инвестиционным займом'\n\nОграничения\n- вопросы налогообложения (уплата НДФЛ) – зависит от того, зарегистрирован ли Инвестор в качестве ИП, возможно ли уменьшение уплачиваемых налогов\n- большая цена входа в сделку (от 2,5 млн рублей)\n\n\nВложенный капитал приносит прибыль от 30% годовых. Мы берем себе часть прибыли за управление средствами, а наши инвесторы получают в среднем 40% годовой доходности при их пассивном участии")
        keyboard = types.InlineKeyboardMarkup()
        key_dogov = types.InlineKeyboardButton(text='ПОКАЗАТЬ ДОГОВОР', callback_data='dogov')
        keyboard.add(key_dogov)
        key_call = types.InlineKeyboardButton(text='СВЯЗАТЬСЯ С МЕНЕДЖЕРОМ', url='https://t.me/NerouN_Bro')
        keyboard.add(key_call)
        question = "Выберите кнопку"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    if call.data == 'dogov':
        bot.send_photo(call.message.chat.id, 'https://cdn.discordapp.com/attachments/801426522623836182/1121119345033097227/invest_dogovor.jpg')
        bot.send_message(call.message.chat.id, "Вернуться в меню: /start")
    if call.data == 'My_Objects':
        bot.send_message(call.message.chat.id, "Ведите идентификатор пользователя")
        bot.register_next_step_handler(call.message, My_object)


@bot.message_handler(content_types=['text', 'photo'])
def calc_doh(message):
    summ = int(message.text)
    pro = o.replace('%', "")
    pro1 = pro.split('-')
    pro2 = summ * (int(pro1[0]) / 100)
    pro3 = summ * (int(pro1[1]) / 100)
    bot.send_message(message.from_user.id, f"Сумма инвистиций: {summ}\n\nПланируемая доходность составит: {pro2} - {pro3}\nВ натуральном выражении: {summ + pro2} - {summ + pro3}\nВ годовых {ob[8]}\n\nСрок реализации: {ob[9]}\n\nВернуться в меню: /start")
    keyboard = types.InlineKeyboardMarkup()
    key_call = types.InlineKeyboardButton(text='СВЯЗАТЬСЯ С МЕНЕДЖЕРОМ',url='https://t.me/NerouN_Bro')
    keyboard.add(key_call)
    question = "Выберите кнопку"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.message_handler(content_types=['text', 'photo'])
def My_object(message):
    log = message.text
    my = []
    try:
        cursor.execute(f"SELECT summa FROM Invest_comp where iden = '{log}'")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        if row2 == '()':
            i = 'dwa' + 6
        my.append(row2)
        cursor.execute(f"SELECT position FROM Invest_comp where iden = '{log}'")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        my.append(row2)
        cursor.execute(f"SELECT opisanie FROM Invest_comp where iden = '{log}'")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        my.append(row2)
        cursor.execute(f"SELECT status FROM Invest_comp where iden = '{log}'")
        rows = str(cursor.fetchall())
        row = rows.replace("(('", "")
        row2 = row.replace("',),)", "")
        my.append(row2)
        bot.send_photo(message.from_user.id, 'https://cdn.discordapp.com/attachments/801426522623836182/1121115222397177986/Object.png', f"Инвестированная сумма: {my[0]}\nОбъект: {my[1]}\nОписание: {my[2]}\nСтатус объекта: {my[3]}\n\nВернуться в меню: /start")
    except:
        bot.send_message(message.from_user.id, "Такого пользователя не существует, проверьте правильность идентификатора и попробуйте снова: /start")

bot.polling(none_stop=True, interval=0)