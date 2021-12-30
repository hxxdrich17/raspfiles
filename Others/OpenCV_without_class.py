# pip install opencv-python
# pip install opencv-contrib-python
# pip install matplotlib

import cv2
import numpy as np
import matplotlib
import time
import os
import datetime

dates = {}
pic_t, t = 0, 0

def SavePic(frame):
    global pic_t, dates
    img_name1 = "plant{}.png".format(pic_t)
    img_name = "Pictures\Total\plant{}.png".format(pic_t)
    IsWritten = cv2.imwrite(img_name, frame)

    if (IsWritten):
        pic_t += 1
        dates[img_name1] = [str(datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))]
        return True, img_name, img_name1


def Render(pic_path, dict_path):
    global dates, t
    image = cv2.imread(pic_path)
    # print(image.shape) # Width, Height, numOfColorChannels
    # TODO: add possible frames
    # frame = image
    for i in range(3):
        if (i == 0): 
            frame = image[0:0, 0:0]
            name = "Pictures\p1\p{}.png".format(t)
        elif (i == 1): 
            frame = image[0:0, 0:0]
            name = "Pictures\p2\p{}.png".format(t)
        elif (i == 2): 
            frame = image[0:0, 0:0]
            name = "Pictures\p3\p{}.png".format(t)
        t += 1

        frameBGR = cv2.GaussianBlur(frame, (7, 7), 0) # blurr
        """kernal = np.ones((15, 15), np.float32)/255
        frameBGR = cv2.filter2D(frameBGR, -1, kernal)"""
        hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV) # convert to hsv

        colorLow = np.array([35, 46, 63])
        colorHigh = np.array([80, 255, 255])
        mask = cv2.inRange(hsv, colorLow, colorHigh) # hsv values to define mask

        kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # morphological transformation mask
        result = cv2.bitwise_and(frame, frame, mask = mask)
        IsWritten = cv2.imwrite(name, result)
        if (IsWritten):
            total_pix = result.size
            green_pix = np.count_nonzero(result)
            percentage = round(green_pix * 100 / total_pix, 2)
            # print(total_pix, green_pix, percentage)
            dates[dict_path] += [green_pix, percentage]
            Statistics(dict_path)


def Statistics(dict_path):
    global dates
    pass


while (True):
    endt = datetime.datetime.now() + datetime.timedelta(seconds=5) # minutes=30 as default

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise IOError("Can not open webcam")

    while (datetime.datetime.now() <= endt):
        ret, frame = cap.read()

    IsSaved, pic_path, dict_path = SavePic(frame)

    if (IsSaved):
        Render(pic_path, dict_path)

    cap.release()
    cv2.destroyAllWindows()