# -*- coding: utf-8 -*-

# tested with win 7 x64
# project created 22.11.2017
# by f883

import subprocess
import re  # обработка строк
import os

programAdress = r"pixelsort.py"          # путь к программе
originalPictureAdress = "pics_for_sorting\\"    # путь к изображениям для обработки
sortedPictureAdress = "sorted\\"                # пусть к папке для сохранения отсортированных изображений


lst = os.walk(originalPictureAdress)
for i in lst:
    nameList = i[2]

print("Found images:")
for i in nameList:
    print(i)


for originalPictureName in nameList:
    print("now sorting: "+ originalPictureName)

    for i in range(0, 23):
        lowerThreshold = " -t " + str(0.10)   # нижний порог сортировки
        upperThreshold = " -u " + str(0.20 + i*0.04)    # верхний порог сортировки
        angle = " -a " + str(90)          # угол поворота изображения

        # sortedPictureName = re.sub(" ", "_", sortedPictureAdress + originalPictureName.split(".")[0] + angle + lowerThreshold + upperThreshold + ".png") # имя отсортированных содержит параметры
        sortedPictureName = re.sub(" ", "_", sortedPictureAdress + str(i + 1) + ".png")  # отсортированные называются 1, 2, ...
        # имя отсортированной картинки

        joinedPixelsortCmd = programAdress + " " + originalPictureAdress + originalPictureName + angle + lowerThreshold + upperThreshold + " " + " -o " + sortedPictureName
        # объединённая строка с параметрами

        print("Parameters: " + angle + lowerThreshold + upperThreshold)

        PIPE = subprocess.PIPE
        p = subprocess.Popen(joinedPixelsortCmd, shell = True)
        p.wait()
        print() # разделение между запусками
        #print("### "+joinedPixelsortCmd)
print("end of script.")
