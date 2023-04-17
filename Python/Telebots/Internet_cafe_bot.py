import telebot
from telebot import types, TeleBot
import webbrowser

bot = telebot.TeleBot('TOKEN') # your token
@bot.message_handler(content_types=['text'])
def start_reservation(message): # starting method    
if message.text == "/start":
        bot.send_photo(message.from_user.id, 'http://i2.wp.com/www.fisharcadesgames.com/wp-content/uploads/2019/12/222538z4g0nrncqzeve34e.jpg', caption="Hello, this is a telegram bot of the Internet cafe 'nekita', here you can leave a reservation for the date, time, place you need. You can also request a number by which you can contact the manager of the cafe or ask a question right here, you will receive a response from the telegram account of one of our employees.")
        keyboard = types.InlineKeyboardMarkup()
        key_reservation = types.InlineKeyboardButton(text='Зарезервировать место | reservation', callback_data='reservation')
        keyboard.add(key_reservation)
        key_number = types.InlineKeyboardButton(text='Номер менеджера | Manager number', callback_data='number')
        keyboard.add(key_number)
        key_Question = types.InlineKeyboardButton(text='Задать вопрос | Ask a Question', callback_data='Question')
        keyboard.add(key_Question)
        question = "What do you want to do?"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True) # a handler method that processes requests from all buttons in the code
def processing_requests_from_buttons(call):
    global po, computer, name, second_name
    if call.data == "reservation":
        bot.send_message(call.message.chat.id, "Please, select date according to this pattern: '12 April'")
        bot.register_next_step_handler(call.message, reservation)
    elif call.data == "number":
        bot.send_message(call.message.chat.id, "+79015685698")
    elif call.data == "Question":
        bot.send_message(call.message.chat.id, "Ask a question, I will send it to our employee")
        bot.register_next_step_handler(call.message, Questions1)
    elif call.data == "1":
        computer = 1
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 1")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "2":
        computer = 2
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 2")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "3":
        computer = 3
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 3")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "4":
        computer = 4
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 4")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "5":
        computer = 5
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 5")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "6":
        computer = 6
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 6")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "7":
        computer = 7
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 7")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "8":
        computer = 8
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 8")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "9":
        computer = 9
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 9")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "10":
        computer = 10
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да | Yes', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет | No', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, f"would you like to book a seat at {date}, at {clock}, computer 10")
        question = "That's right?"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "yes":
        bot.send_message(call.message.chat.id, "what is your name?") # find out the name
        bot.register_next_step_handler(call.message, yes)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Try again: /start")

@bot.message_handler(content_types=['text', 'photo'])
def yes(message): # find out the second_name
    global po, computer, name, second_name
    name = message.text
    bot.send_message(message.from_user.id, "What is your second name?")
    bot.register_next_step_handler(message, yes1)

@bot.message_handler(content_types=['text', 'photo'])
def yes1(message): # sending a reservation request to the manager's id    
    global po, computer, name, second_name, date, clock, iid
    second_name = message.text
    iid = message.from_user.id
    bot.send_photo(1370983934, 'https://cdn.discordapp.com/attachments/801426522623836182/1096821260283035708/photo1681572735.jpeg', caption=f"Computer reservation request: {date}, {clock}, {computer} computer from {name} {second_name}. User id: {iid}")
    bot.send_message(message.from_user.id, "Succes!")
    bot.send_message(message.from_user.id, "Press: /start")
    pass

@bot.message_handler(content_types=['text', 'photo'])
def reservation(message): # getting the date
    global date, clock
    date = message.text
    bot.send_message(message.from_user.id, "Thank you, now tell me the time you want to come, for example '12:10'")
    bot.register_next_step_handler(message, reservation_1)

@bot.message_handler(content_types=['text', 'photo'])
def reservation_1(message): # getting the time and requesting the computer number     
    global date, clock
    clock = message.text
    bot.send_message(message.from_user.id, "Okay, now select the armored computer")
    keyboard = types.InlineKeyboardMarkup()
    key_1 = types.InlineKeyboardButton(text='1', callback_data='1')
    keyboard.add(key_1)
    key_2 = types.InlineKeyboardButton(text='2', callback_data='2')
    keyboard.add(key_2)
    key_3 = types.InlineKeyboardButton(text='3', callback_data='3')
    keyboard.add(key_3)
    key_4 = types.InlineKeyboardButton(text='4', callback_data='4')
    keyboard.add(key_4)
    key_5 = types.InlineKeyboardButton(text='5', callback_data='5')
    keyboard.add(key_5)
    key_6 = types.InlineKeyboardButton(text='6', callback_data='6')
    keyboard.add(key_6)
    key_7 = types.InlineKeyboardButton(text='7', callback_data='7')
    keyboard.add(key_7)
    key_8 = types.InlineKeyboardButton(text='8', callback_data='8')
    keyboard.add(key_8)
    key_9 = types.InlineKeyboardButton(text='9', callback_data='9')
    keyboard.add(key_9)
    key_10 = types.InlineKeyboardButton(text='10', callback_data='10')
    keyboard.add(key_10)
    question = "Select computer number"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.message_handler(content_types=['text', 'photo'])
def Questions(message): # getting a question from a user    
    bot.send_message(message.from_user.id, "Ask a question, I will send it to our employee")
    bot.register_next_step_handler(message, Questions1)

@bot.message_handler(content_types=['text', 'photo'])
def Questions1(message): # sending a question from a user to an employee id
    global questiono, iid
    questiono = message.text
    iid = message.from_user.id
    bot.send_photo(1370983934, 'https://cdn.discordapp.com/attachments/801426522623836182/1096821259964264628/photo1681572720.jpeg', caption=f"Received a question from a user: {questiono}; User id: {iid}")
    bot.send_message(message.from_user.id, "Your question has been delivered")
    bot.send_message(message.from_user.id, "Press: /start")
    pass
bot.polling(none_stop=True, interval=0) # looping the bot's work