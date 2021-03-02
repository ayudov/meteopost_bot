import os


def removing_image(path: str):
    for i in range(4):
        if os.path.exists(path + '/' + str(i)+".png"):
            os.remove(path + '/' + str(i)+".png")
            print(path + '/' + str(i)+".png removed")
        else:
            print(path + '/' + str(i)+".png does not exist for deleting")

