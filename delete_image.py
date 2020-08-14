import os


def removing_image():
    for i in range(4):
        if os.path.exists(str(i)+".png"):
            os.remove(str(i)+".png")
            print(str(i)+".png removed")
        else:
            print("The "+str(i)+".png does not exist")

