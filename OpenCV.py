import cv2
import numpy as np
import datetime
import os
import Statistic

dates1 = {
            "Date": [],
            "Original Photo": [],
            "Picture": [],
            "Temperature": [],
            "Humidity": [],
            "Green Pixels": [],
            "Percantage": []
            }
dates2, dates3 = dates1, dates1
    
pic_t, t = 0, 0

class HydroEye:

    def SavePic(self, frame):
        global pic_t, dates1, dates2, dates3
        img_name1 = "plant{}.png".format(pic_t)
        img_name = "/home/pi/Desktop/Hydro/Pictures/Total/plant{}.png".format(pic_t)
        IsWritten = cv2.imwrite(img_name, frame)

        if (IsWritten):
            pic_t += 1
            now_date = str(datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
            dates1["Date"] += [now_date]
            dates1["Original Photo"] += [img_name]
            dates2["Date"] += [now_date]
            dates2["Original Photo"] += [img_name]
            dates3["Date"] += [now_date]
            dates3["Original Photo"] += [img_name]
            return True, img_name, img_name1

    def Render(self, pic_path, dict_path):
        global t, dates1, dates2, dates3
        image = cv2.imread(pic_path)
        # print(image.shape) # Width, Height, numOfColorChannels
        # TODO: add possible frames
        # frame = image
        for i in range(3):
            if (i == 0): 
                frame = image
                name = "/home/pi/Desktop/Hydro/Pictures/p1/p{}.png".format(t)
                dates1["Picture"] += [name]
            elif (i == 1): 
                frame = image
                name = "/home/pi/Desktop/Hydro/Pictures/p2/p{}.png".format(t)
                dates2["Picture"] += [name]
            elif (i == 2): 
                frame = image
                name = "/home/pi/Desktop/Hydro/Pictures/p3/p{}.png".format(t)
                dates3["Picture"] += [name]
            t += 1

            frameBGR = cv2.GaussianBlur(frame, (7, 7), 0) # blurr
            """kernel = np.ones((15, 15), np.float32)/255
            frameBGR = cv2.filter2D(frameBGR, -1, kernel)"""
            hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV) # convert to hsv

            colorLow = np.array([49, 75, 0]) # TODO: correct low & high values (done)
            colorHigh = np.array([82, 255, 255])
            mask = cv2.inRange(hsv, colorLow, colorHigh) # hsv values to define mask

            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # morphological transformation mask
            result = cv2.bitwise_and(frame, frame, mask = mask)
            IsWritten = cv2.imwrite(os.path.join(name), result)

            if (IsWritten):
                total_pix = result.size
                green_pix = np.count_nonzero(result)
                percentage = round(green_pix * 100 / total_pix, 2)
                if (i == 0):
                    dates1["Green Pixels"] += [green_pix]
                    dates1["Percantage"] += [percentage]
                elif (i == 1):
                    dates2["Green Pixels"] += [green_pix]
                    dates2["Percantage"] += [percentage]
                elif (i == 2):
                    dates3["Green Pixels"] += [green_pix]
                    dates3["Percantage"] += [percentage]
                HydroEye.Logs(1)
        stat = Statistic.Statistics()
        stat.create(dates1, dates2, dates3)

    def Logs(self):
        f = open(os.path.join("/home/pi/Desktop/Hydro/Logs/Logs.txt"), "a", encoding="UTF-8")
        date = str(datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))
        f.write(f"[{date}] Захват и анализ изображения.\n")
        f.close()

    def __init__(self):
        while (True):
            endt = datetime.datetime.now() + datetime.timedelta(seconds=5) # minutes=30 as default

            cap = cv2.VideoCapture(0)
            print("Cap started")
            if not cap.isOpened():
                raise IOError("Can not open webcam")

            while (datetime.datetime.now() <= endt):
                ret, frame = cap.read()
                # cv2.imshow('Output', frame) # Local video showing

            IsSaved, pic_path, dict_path = HydroEye.SavePic(1, frame)

            if (IsSaved):
                HydroEye.Render(1, pic_path, dict_path)

            cap.release()
            cv2.destroyAllWindows()
            
start = HydroEye()