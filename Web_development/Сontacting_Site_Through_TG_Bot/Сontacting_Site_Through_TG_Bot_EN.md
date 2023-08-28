# The system of website interaction using bot telegrams - Contacting_Site_Through_TG_Bot

# Structure of the system

The system is an html file of a specific page, 2 python scripts for launching localhost and launching the bot's telegrams directly. They are all located in 1 directory, which also has an assets folder where all files uploaded by the user are stored.

# Telegram bot

VIDEO №1

After launching the bot, we see 2 buttons - "Загрузить файл" and "Удалить файл"

VIDEO №2

If we need to upload a file to the site, click the "Загрузить файл" button. Next, the bot asks what type of file we want to upload. We upload a photo, therefore we click the "Фото" button. Next, we send a photo to the bot, which it will directly save and add the corresponding object to the html file by editing it. After the bot wrote that the file was successfully uploaded to the site, we go to the pre-launched localhost and update the page. Voila! the photo is now on the website!

VIDEO №3

Now delete the newly downloaded file from the site, click on the "Удалить файл" button. The bot sends a list of files to the directory. We find our photo and check if it is exactly the same photo, to do this, click on the "Посмотреть файл" button. We send the name of our file copied in advance, after which the bot sends us a file with the specified file. After we are convinced that this is exactly the file, the bot immediately offers us to delete it or go back, we select "Удалить файл", after which we send the name of our file to the bot again and wait until the bot performs all the deletion procedures and informs us about their completion. After the bot sends us an end message, we go back to localhost and refresh the page. And what we see is there is no photo.