from PyQt5.QtGui import * 

def image(src):
    imageMain = QPixmap(src)

    if(int(imageMain.width()) > int(imageMain.height())):
        imageMain = imageMain.scaledToWidth(1400)
    else:
        imageMain = imageMain.scaledToHeight(900)
    return imageMain