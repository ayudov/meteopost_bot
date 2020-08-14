from bot import bot
from telebot.types import Message
import download_image
import delete_image
from buttons import *
from datetime import datetime


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привіт', reply_markup=keyboard_hello)


@bot.message_handler(commands=['send_image'])
def image_sending(message):
    download_image.download_image()
    photo = open('forecast.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    delete_image.removing_image()


@bot.message_handler(content_types=["text"])
def text_answers(message: Message):
    if message.text == "Прогноз на сьогодні":
        download_image.download_images_of_day(0)
        print("Images downloaded")
        bot.send_message(message.chat.id, 'Ось погода на сьогодні:', reply_markup=keyboard_hello)
        images_sending(message)
        # for i in range(4):
        #     try:
        #         photo = open(str(i)+'.png', 'rb')
        #         bot.send_photo(message.chat.id, photo)
        #         photo.close()
        #     except:
        #         print("No such image "+str(i)+".png downloaded for sending")
        # delete_image.removing_image()
        # print("Images removed")
    elif message.text == "Прогноз на завтра":
        download_image.download_images_of_day(1)
        print("Images downloaded")
        bot.send_message(message.chat.id, 'Ось погода на завтра:', reply_markup=keyboard_hello)
        images_sending(message)





def images_sending(message: Message):
    for i in range(4):
        try:
            photo = open(str(i) + '.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
        except:
            print("No such image " + str(i) + ".png downloaded for sending")
    delete_image.removing_image()
    print("Images removed")


if __name__ == '__main__':
    bot.polling(none_stop=True)
