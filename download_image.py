import urllib.request
import delete_image
import os
from datetime import datetime


def download_images_of_day(day):

    number_of_pics_today = number_of_today_pics()

    if day == 0:
        for i in range(1, number_of_pics_today+1):
            download_image(str(i-1)+".png", "t-00"+str(i*6))
    elif day == 1:
        for i in range(1, 5):
            download_image(str(i-1)+".png", "t-0"+str(number_of_pics_today*(i+1)*6))
    elif day == 2:
        for i in range(1, 5):
            download_image(str(i-1)+".png", "t-0"+str(24+number_of_pics_today*(i+1)*6))
    elif day == 3:
        for i in range(1, 5):
            download_image(str(i-1)+".png", "t-"+pic_name_formatting(48+number_of_pics_today*(i+1)*6))
    elif day == 4:
        for i in range(1, 5):
            download_image(str(i-1)+".png", "t-"+pic_name_formatting(72+number_of_pics_today*(i+1)*6))
    elif day == 5:
        for i in range(1, 5):
            download_image(str(i-1)+".png", "t-"+pic_name_formatting(96+number_of_pics_today*(i+1)*6))


def pic_name_formatting(number: int):
    if number < 100:
        return '0'+str(number)
    else:
        return str(number)


def number_of_today_pics():
    current_h = datetime.utcnow().hour+2
    if 5 <= current_h <= 11:
        return 3
    elif 11 <= current_h <= 17:
        return 2
    elif 15 <= current_h <= 23:
        return 1
    elif 14 <= current_h <= 20:
        return 4


    # if day == 0:
    #     download_image("0.png", "t-006")
    #     download_image("1.png", "t-012")
    #     download_image("2.png", "t-018")
    # elif day == 1:
    #     download_image("0.png", "t-024")
    #     download_image("1.png", "t-030")
    #     download_image("2.png", "t-036")
    #     download_image("3.png", "t-042")


def download_image(downloaded_image_name, web_image_name):
    if os.path.exists(downloaded_image_name):
        delete_image.removing_image()
        urllib.request.urlretrieve("https://meteopost.com/load/maps/"+web_image_name+".png", downloaded_image_name)
        print(downloaded_image_name + "downloaded")
    else:
        urllib.request.urlretrieve("https://meteopost.com/load/maps/"+web_image_name+".png", downloaded_image_name)
        print(downloaded_image_name + " downloaded")
