###########################################################################################################

# Author: zackary Shen
# Email: szbltyy@hotmail.com
# Date: 2019/6/20 00:28 Thur

###########################################################################################################

# This is a class that recognize the characters from a photo
# The license plate will get from a object from class PhotoPro
# And then this class will recognize the number and color
# of the license plate, and store it in a String object

# tips: Comments annotated with # are comments for explanation
# tips: Comments annotated with ## are testing codes


import pytesseract
from Process import PhotoPro
import cv2

class Recognize:
    """
    This is a class that recognize the characters from a photo
    """

    # init the class
    def __init__(self, image_path):
        self.image_path = image_path

    # using a PhotoPro object to get plate
    def Get_Plate(self):
        # get the license plate, the color one need to recognize color
        photopro = PhotoPro(self.image_path)
        color_plate = photopro.Get_Image()

        # change the license to grey image, use it to recognize characters
        grey_palte = cv2.cvtColor(color_plate, cv2.COLOR_BGR2RGB)





if __name__ == '__main__':
    pp = Recognize('./Images/1.jpg')
    pp.Get_Plate()