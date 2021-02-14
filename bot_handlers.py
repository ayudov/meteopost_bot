from bot import bot
from telebot.types import Message, InputMediaPhoto
import download_image
import delete_image
from download_image import get_update_info_from_website


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привіт, обери команду щоб отримати прогноз погоди')


@bot.message_handler(commands=['today'])
def today_images(message):
    update_info = get_update_info_from_website()
    send_images(message=message, day=0, text='Погода на сьогодні\n'+'_'+update_info+'_')


@bot.message_handler(commands=['tomorrow'])
def tomorrow_images(message):
    update_info = get_update_info_from_website()
    send_images(message=message, day=1, text='Погода на завтра\n'+'_'+update_info+'_')


@bot.message_handler(commands=['in_1_day'])
def in_1_day_images(message):
    update_info = get_update_info_from_website()
    send_images(message=message, day=2, text='Погода на післязавтра\n'+'_'+update_info+'_')


@bot.message_handler(commands=['in_2_days'])
def in_2_days_images(message):
    update_info = get_update_info_from_website()
    send_images(message=message, day=3, text='Погода на через 2 дні\n'+'_'+update_info+'_')


@bot.message_handler(commands=['in_3_days'])
def in_2_days_images(message):
    update_info = get_update_info_from_website()
    send_images(message=message, day=4, text='Погода на через 3 дні\n'+'_'+update_info+'_')


@bot.message_handler(commands=['in_4_days'])
def in_2_days_images(message):
    update_info = get_update_info_from_website()
    send_images(message=message, day=5, text='Погода на через 4 дні\n'+'_'+update_info+'_')


def send_images(message, day, text):
    weather_types = [['t', 'Температура повітря'],
                     ['gust', 'Пориви вітру'],
                     ['h', 'Вологість повітря'],
                     ['o', 'Опади'],
                     ['c', 'Хмарність']]

    day = day
    bot.send_message(message.chat.id, text, parse_mode='markdown')

    for type in weather_types:
        media = []
        pictures_to_send = []
        download_image.download_images_of_day(day, weather_type=type[0])
        for i in range(4):
            try:
                tmp_pic = open(str(i) + ".png", "rb")
                pictures_to_send.append(tmp_pic)
                if i == 0:
                    media.append(InputMediaPhoto(pictures_to_send[i], caption=type[1]))
                else:
                    media.append(InputMediaPhoto(pictures_to_send[i]))
            except:
                print(str(i) + ".png not found for adding to album ")

        bot.send_media_group(message.chat.id, media)

        for image in pictures_to_send:
            image.close()

        delete_image.removing_image()

    print('Done sending')


# if __name__ == '__main__':
#     bot.polling(none_stop=True)
