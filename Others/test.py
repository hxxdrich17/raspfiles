# # # # import time
# # # # import datetime

# # # # # t = 0

# # # # # start = time.time()
# # # # # time.sleep(5)
# # # # # end = time.time()
# # # # # while (t <= 5):
# # # # #     t = end - start
# # # # #     print(t)
# # # # # t = 0
# # # # # t = time.sleep(3)

# # # # # if (t == 0):
# # # # #     print(0)
# # # # # elif (t == None):
# # # # #     print("Success")


# # # # # now = datetime.datetime.now()
# # # # # # current_time = now.strftime("%H%M%S")
# # # # # # sec_after = now + datetime.timedelta(seconds=3)
# # # # # now = now.strftime("%d.%m.%y %H:%M:%S")
# # # # print(datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"))


# # # # # while True:
# # # # #     now1 = datetime.datetime.now()
# # # # #     if (now1 >= sec_after):
# # # # #         print(now1)
# # # # #         print("Time is over")
# # # # #         break

# # # # https://russianblogs.com/article/41781040604/
# # # # https://www.machinelearningmastery.ru/color-identification-in-images-machine-learning-application-b26e770c4c71/

# # # import cv2
# # # import numpy as np

# # # # image = cv2.imread("Pictures\plant0.png")
# # # # cropped = image[65:340, 245:520]
# # # # cv2.imshow('Color all',cropped)
# # # # cv2.imshow('Color blue',cropped[:,:,0])
# # # # cv2.imshow('Color green',cropped[:,:,1])
# # # # cv2.imshow('Color red',cropped[:,:,2])
# # # # cv2.waitKey(0)

# # # image = cv2.imread("Pictures\e00e362fb2dc15d0dc4b74c575a6f641.jpg")
# # # print(image.shape) # Width, Height, numOfColorChannels of
# # # # possible_frames = [[65:340, 245:520], [30:130, 150:300], [30:130, 150:300]]
# # # while True:
# # #     frame = image # Height, Width
# # #     frameBGR = cv2.GaussianBlur(frame, (7, 7), 0) # blurr
# # #     """kernal = np.ones((15, 15), np.float32)/255
# # #     frameBGR = cv2.filter2D(frameBGR, -1, kernal)"""
# # #     hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV) # convert to hsv
# # #     colorLow = np.array([35, 46, 63])
# # #     colorHigh = np.array([80, 255, 255])
# # #     mask = cv2.inRange(hsv, colorLow, colorHigh) # hsv values to define mask
# # #     kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
# # #     mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# # #     mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # morphological transformation mask
# # #     result = cv2.bitwise_and(frame, frame, mask = mask)
# # #     cv2.imshow('colorTest', result)
# # #     print("Start: ", result, " :End")
# # #     break
# # #     k = cv2.waitKey(5) & 0xFF
# # #     if k == 27:
# # #         break

# # # cv2.destroyAllWindows()
# # # import cv2
# # # import numpy as np
# # # import matplotlib.pyplot as plt

# # # nemo = cv2.imread('Pictures\e00e362fb2dc15d0dc4b74c575a6f641.jpg')
# # # nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
# # # plt.imshow(nemo)
# # # plt.show()

# # # hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
# # # light_orange = (1, 190, 200)
# # # dark_orange = (18, 255, 255)
# # # mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
# # # result = cv2.bitwise_and(nemo, nemo, mask=mask)
# # # plt.subplot(1, 2, 1)
# # # plt.imshow(mask, cmap="gray")
# # # plt.subplot(1, 2, 2)
# # # plt.imshow(result)
# # # plt.show()

# # # light_white = (0, 0, 200)
# # # dark_white = (145, 60, 255)

# # # mask_white = cv2.inRange(hsv_nemo, light_white, dark_white)
# # # result_white = cv2.bitwise_and(nemo, nemo, mask=mask_white)

# # # plt.subplot(1, 2, 1)
# # # plt.imshow(mask_white, cmap="gray")
# # # plt.subplot(1, 2, 2)
# # # plt.imshow(result_white)
# # # plt.show()

# # # final_mask = mask + mask_white

# # # final_result = cv2.bitwise_and(nemo, nemo, mask=final_mask)
# # # plt.subplot(1, 2, 1)
# # # plt.imshow(final_mask, cmap="gray")
# # # plt.subplot(1, 2, 2)
# # # plt.imshow(final_result)
# # # plt.show()

# # # blur = cv2.GaussianBlur(final_result, (7, 7), 0)
# # # plt.imshow(blur)
# # # plt.show()

# # import numpy as np
# # import cv2
# # import matplotlib.pyplot as plt

# # # # Open image and make into numpy array
# # # im=cv2.imread('Pictures\e00e362fb2dc15d0dc4b74c575a6f641.jpg')
# # # # plt.imshow(im)
# # # # plt.show()

# # # # Work out what we are looking for
# # # sought = [59, 200, 49]

# # # # Find all pixels where the 3 RGB values match "sought", and count
# # # result = np.count_nonzero(np.all(im==sought,axis=2))
# # # print(result)

# # # image = cv2.imread("Pictures\e00e362fb2dc15d0dc4b74c575a6f641.jpg")
# # # print(image.shape) # Width, Height, numOfColorChannels of
# # # # possible_frames = [[65:340, 245:520], [30:130, 150:300], [30:130, 150:300]]
# # # # for i in range(1): # 3
# # # # frame = image[possible_frames[i]] # Height, Width
# # # frame = image
# # # frameBGR = cv2.GaussianBlur(frame, (7, 7), 0) # blurr
# # # """kernal = np.ones((15, 15), np.float32)/255
# # # frameBGR = cv2.filter2D(frameBGR, -1, kernal)"""
# # # hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV) # convert to hsv
# # # colorLow = np.array([35, 46, 63])
# # # colorHigh = np.array([80, 255, 255])
# # # mask = cv2.inRange(hsv, colorLow, colorHigh) # hsv values to define mask
# # # kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
# # # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# # # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) # morphological transformation mask
# # # result = cv2.bitwise_and(frame, frame, mask = mask)

# # # total_pix = result.size
# # # green_pix = np.count_nonzero(result)
# # # percentage = round(green_pix * 100 / total_pix, 2)

# # # print(total_pix, green_pix, percentage)

# # class Test:

# #     def truly(self):
# #         # print("wha")
# #         Test.lol(self)

# #     def lol(self):
# #         print("Success!")

# #     def __init__(self):
# #         print("Start.")
# #         for i in range(10):
# #             # print(i)
# #             Test.truly(self)

# # abc = Test()
# # # abc.lol()


# # pip install openpyxl xlsxwriter xlrd

# import pandas as pd

# dates1 = {
#             "Date": ["1232.12349.8123", "jshfad"],
#             "Original Photo": ["Pictures\lol.png", "sadhfo"],
#             "Picture": ["Pictures\p1", "uahdshf"],
#             "Green Pixels": [1354234, 72817],
#             "Percentage": [12, 1]
#             }
# dates2 = {
#             "Date": ["1232.12349.8123", "jshfad"],
#             "Original Photo": ["Pictures\lol.png", "sadhfo"],
#             "Picture": ["Pictures\p1", "uahdshf"],
#             "Green Pixels": [1354234, 72817],
#             "Percentage": [12, 2]
#             }
# dates3 = {
#             "Date": ["1232.12349.8123", "jshfad"],
#             "Original Photo": ["Pictures\lol.png", "sadhfo"],
#             "Picture": ["Pictures\p1", "uahdshf"],
#             "Green Pixels": [1354234, 72817],
#             "Percentage": [12, 3]
#             }

# df1 = pd.DataFrame(dates1)
# df2 = pd.DataFrame(dates2)
# df3 = pd.DataFrame(dates3)

# sheets = {"Plant 1": df1, "Plant 2": df2, "Plant 3": df3}

# writer = pd.ExcelWriter('Statistics/Plants.xlsx', engine='xlsxwriter')

# for sheet_name in sheets.keys():
#     sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

# writer.save()

# # dates2, dates3 = dates1, dates1
# # print(dates1, dates2, dates3)

# t = 1
#
# class Test:
#
#         def lol(self):
#             print(type(sec), t)
#
#         def __init__(self):
#             global sec
#             f = open("Settings\Config.txt", "r", encoding="UTF-8")
#             sec = int(f.readlines()[3].split("Seconds for filling = ")[1].split("\n")[0])
#             f.close()
#
#
# a = Test()
# a.lol()

from threading import Thread
# from Others import Test1 as t
# from Others import Test2 as t1
#
#
# def main():
#     while True:
#         t.test()
#         t1.test1()


# th_1, th_2 = Thread(target=t.test), Thread(target=t1.test1)
#
# if __name__ == '__main__':
#     th_1.start(), th_2.start()
#     th_1.join(), th_2.join()

# main()

class Test:

    def log(self):
        print(123)

    def __init__(self):
        print("Hey")


Test.log(1)
