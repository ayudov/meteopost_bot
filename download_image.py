import urllib.request
import delete_image
import os


def download_images_of_day(day):
    if day == 0:
        download_image("0.png", "t-006")
        download_image("1.png", "t-012")
        download_image("2.png", "t-018")
    elif day == 1:
        download_image("0.png", "t-024")
        download_image("1.png", "t-030")
        download_image("2.png", "t-036")
        download_image("3.png", "t-042")


def download_image(downloaded_image_name, web_image_name):
    if os.path.exists(downloaded_image_name):
        delete_image.removing_image()
        urllib.request.urlretrieve("https://meteopost.com/load/maps/"+web_image_name+".png", downloaded_image_name)
        print(downloaded_image_name+"downloaded")
    else:
        urllib.request.urlretrieve("https://meteopost.com/load/maps/"+web_image_name+".png", downloaded_image_name)
        print(downloaded_image_name + " downloaded")
