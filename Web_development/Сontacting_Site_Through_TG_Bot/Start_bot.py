import telebot, os
from telebot import types

bot = telebot.TeleBot('TOKEN')
sp_files = os.listdir("MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/")

@bot.message_handler(content_types=['text'])
def start(message):
    global keyboard
    if message.text == "/start":
        bot.send_message(message.from_user.id, 'Здаравствуйте, вы можете выбрать одну из кнопок в меню:')
        keyboard = types.InlineKeyboardMarkup()
        key_Upload = types.InlineKeyboardButton(text='Добавить файл', callback_data='Upload')
        keyboard.add(key_Upload)
        key_Delete = types.InlineKeyboardButton(text='Удалить файл', callback_data='Delete')
        keyboard.add(key_Delete)
        question = "Выберите кнопку"
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def processing_requests_from_buttons(call):
    if call.data == "Upload":
        bot.send_message(call.message.chat.id, "выберите тип файла:")
        keyboard = types.InlineKeyboardMarkup()
        key_Video = types.InlineKeyboardButton(text='Видео', callback_data='Video')
        keyboard.add(key_Video)
        key_Photo = types.InlineKeyboardButton(text='Фото', callback_data='Photo')
        keyboard.add(key_Photo)
        key_Audio = types.InlineKeyboardButton(text='Аудио', callback_data='Audio')
        keyboard.add(key_Audio)
        question = "Выберите кнопку"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    if call.data == "Video":
        bot.send_message(call.message.chat.id, "Отправьте видео")
        bot.register_next_step_handler(call.message, Video)
    if call.data == "Photo":
        bot.send_message(call.message.chat.id, "Отправьте фото")
        bot.register_next_step_handler(call.message, Photo)
    if call.data == "Audio":
        bot.send_message(call.message.chat.id, "Отправьте аудио файлом")
        bot.register_next_step_handler(call.message, Audio)
    if call.data == "Delete":
        l = os.listdir("E:/Рабочий стол/Проекты _Python/WEB/PublFromTeleg")
        bot.send_message(call.message.chat.id, f"Полный список фалов: {l}")
        bot.send_message(call.message.chat.id, "Вы можете сразу удалить нужный вам файл или сначала его просмотреть")
        keyboard = types.InlineKeyboardMarkup()
        key_Delete_t = types.InlineKeyboardButton(text='Удалить файл', callback_data='Delete_t')
        keyboard.add(key_Delete_t)
        key_Delete_p = types.InlineKeyboardButton(text='Просмотреть файл', callback_data='Delete_p')
        keyboard.add(key_Delete_p)
        question = "Выберите кнопку"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    if call.data == "Delete_t":
        bot.send_message(call.message.chat.id, "Отправьте имя файла")
        bot.register_next_step_handler(call.message, Delete_t)
    if call.data == "Delete_p":
        bot.send_message(call.message.chat.id, "Отправьте имя файла")
        bot.register_next_step_handler(call.message, Delete_p)



@bot.message_handler(content_types=['video'])
def Video(message):
    global new, type_file, newoe, src, src_2, sp_files_pr, sp_files
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = file_info.file_path
    src_2 = src.replace("videos/", "")
    with open(src_2, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Файл загружен...")
    sp_files_pr = os.listdir("MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/")
    h = 0
    for i in sp_files_pr:
        if i == sp_files[h]:
            h = h + 1
        else:
            new = str(sp_files_pr[h])
            sp_files = os.listdir("MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/")
            break
    if new.find(" ") != -1:
        newoe = new.replace(" ", "-")
        type_file = newoe[-3::]
    else:
        newoe = new
        type_file = newoe[-3::]
    try:
        with open('index.html', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'    </div>\n  </body>\n</html>', f'      <video controls="controls">\n        <source src="{newoe}" type="video/{type_file}" />\n      </video>\n    </div>\n  </body>\n</html>')
        with open('index.html', 'w') as f:
            f.write(new_data)
        bot.send_message(message.from_user.id, "Видео добавлено на сайт! /start")
        src = None
        src_2 = None
        newoe = None
        new = None
        sp_files_pr = None
    except Exception as suka:
        bot.send_message(message.from_user.id, f"Произошла ошибка, повторите попытку. имя ошибки:{suka}")

@bot.message_handler(content_types=['photo'])
def Photo(message):
    global sp_files_pr, sp_files, new
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = file_info.file_path
    src_2 = src.replace("photos/", "")
    with open(src_2, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Файл загружен...")
    sp_files_pr = os.listdir("MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/")
    h = 0
    for i in sp_files_pr:
        if i == sp_files[h]:
            h = h + 1
        else:
            new = str(sp_files_pr[h])
            sp_files = os.listdir("MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/")
            break
    if new.find(" ") != -1:
        newoe = new.replace(" ", "-")
    else:
        newoe = new
    try:
        with open('index.html', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'    </div>\n  </body>\n</html>',
                                    f'      <img src="{newoe}" alt="alt text" class="image" />\n    </div>\n  </body>\n</html>')
        with open('index.html', 'w') as f:
            f.write(new_data)
        bot.send_message(message.from_user.id, "Фото добавлено на сайт! /start")
    except Exception as suka:
        bot.send_message(message.from_user.id, f"Произошла ошибка, повторите попытку. имя ошибки:{suka}")

@bot.message_handler(content_types=['file'])
def Audio(message):
    global sp_files_pr, sp_files, new
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/assets' + message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Файл загружен...")
    sp_files_pr = os.listdir("MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/")
    h = 0
    for i in sp_files_pr:
        if i == sp_files[h]:
            h = h + 1
        else:
            new = str(sp_files_pr[h])
            sp_files = os.listdir("MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/")
            break
    if new.find(" ") != -1:
        newoe = new.replace(" ", "-")
        type_file = newoe[-3::]
    else:
        newoe = new
        type_file = newoe[-3::]
    try:
        with open('index.html', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'    </div>\n  </body>\n</html>',
                                    f'      <audio controls>\n        <source src="{newoe}" type="audio/{type_file}" />\n      </audio>\n    </div>\n  </body>\n</html>')
        with open('index.html', 'w') as f:
            f.write(new_data)
        bot.send_message(message.from_user.id, "Аудио добавлено на сайт! /start")
    except Exception as suka:
        bot.send_message(message.from_user.id, f"Произошла ошибка, повторите попытку. имя ошибки:{suka}")

@bot.message_handler(content_types=['text'])
def Delete_t(message):
    foy = str(message.text)
    type_file = foy[-3::]
    if type_file == "mp4" or type_file == "mkv" or type_file == "avi":
        with open('index.html', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'      <video controls="controls">\n        <source src="{foy}" type="video/{type_file}" />\n      </video>', '')
        with open('index.html', 'w') as f:
            f.write(new_data)
        os.remove(f"MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/assets/{foy}")
        bot.send_message(message.from_user.id, "Видео удалено с сайта! /start")
        foy = None
        type_file = None
    if type_file == "png" or type_file == "jpg" or type_file == "peg" or type_file == "fif":
        with open('index.html', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'      <img src="{foy}" alt="alt text" class="image" />', '')
        with open('index.html', 'w') as f:
            f.write(new_data)
        os.remove(f"MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/assets/{foy}")
        bot.send_message(message.from_user.id, "Фото удалено с сайта! /start")
        foy = None
        type_file = None
    if type_file == "mp3" or type_file == "wav" or type_file == "ogg" or type_file == "wma":
        with open('index.html', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(f'      <audio controls>\n        <source src="{foy}" type="audio/{type_file}" />\n      </audio>', '')
        with open('index.html', 'w') as f:
            f.write(new_data)
        os.remove(f"MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/assets/{foy}")
        bot.send_message(message.from_user.id, "Аудио удалено с сайта! /start")
        foy = None
        type_file = None

@bot.message_handler(content_types=['text'])
def Delete_p(message):
    foy = str(message.text)
    f = open(f"MyProjects/Web_development/Сontacting_Site_Through_TG_Bot/assets/{foy}", "rb")
    bot.send_document(message.chat.id, f)
    keyboard = types.InlineKeyboardMarkup()
    key_Delete_t = types.InlineKeyboardButton(text='Удалить файл', callback_data='Delete_t')
    keyboard.add(key_Delete_t)
    question = "Назад: /start"
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)