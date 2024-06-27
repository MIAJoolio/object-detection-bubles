import matplotlib.pyplot as plt
import cv2 as cv 
import numpy as np

# import image
path = 'input_images/'
image1 = cv.imread(path+'/flowers_1.jpg',-1)
image2 = cv.imread(path+'/flowers_2.jpg',-1)

# define colors to plot the histograms 
colors = ('r','g','b') 
  
# compute and plot the image histograms
hists = []
j = 0
for img in [image1, image2]: 
    plt.figure(j)
    j += 1
    for i,color in enumerate(colors):    
        # вычисление интенсивности каждого значения пикселя методом opencv
        """
        Функция показалась менее удобной для визуализации нежели методы matplolib, поэтому приведена для примера   
        images - изображения
        channels - в теории можно указать кол-во каналов и для каждого функция посчитает гистограмму интенсивности
        mask - можно считать значения интенсивности только в некоторой области/ маске
        histSize - максимальное значение 
        ranges - деление по бинам
        hist - можно указать переменную для сохранения результатов, чтобы не объявлять переменную
        # accumulative 
        """
        hist = cv.calcHist(img,[i],None,[256],[0,256]) 
        plt.plot(hist, color = color)
    plt.title('Image Histogram')
    # plt.savefig(f'C:/Users/Ilia/Work_ITMO/OpenCV/Other/res/hist_{j}.jpg')
    

fig = plt.figure(2)
plt.hist(image1[:, :, 0].ravel(), bins = 256, color = 'Red', alpha = 0.5)
plt.hist(image1[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
plt.hist(image1[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5) 
plt.legend(['Красный канал (R)', 'Зеленый канал (G)', 'Cиний канал (B)'])
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество')
plt.title('Реальное распределение img1')

fig = plt.figure(3)
plt.hist(image2[:, :, 0].ravel(), bins = 256, color = 'Red', alpha = 0.5)
plt.hist(image2[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
plt.hist(image2[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5) 
plt.legend(['Красный канал (R)', 'Зеленый канал (G)', 'Cиний канал (B)'])
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество')
plt.title('Реальное распределение img2')


# plt.savefig('MyScripts/Image_processing/1_Histogram/brightness_op2_hist.jpg')
plt.show()
