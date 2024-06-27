import matplotlib.pyplot as plt
import cv2 as cv 
import numpy as np



# import image
path = 'input_images/'
image_name = ['COCO_train2014_000000006792.jpg', 'bubles.jpg']
i = 0
image = cv.imread(path+image_name[i],-1)

image = cv.GaussianBlur(image, ksize = (5,5), sigmaX= 1.5, sigmaY= 1.5)

if len(image.shape) == 2:
    image = cv.cvtColor(image,cv.COLOR_GRAY2BGR)


def nothing(a):
    pass

cv.namedWindow('HLS')
cv.resizeWindow('HLS', 500, 260)
cv.createTrackbar('HUE min', 'HLS',0,360,nothing)
cv.createTrackbar('HUE max', 'HLS',0,360,nothing)
cv.createTrackbar('SAT min', 'HLS',0,256,nothing)
cv.createTrackbar('SAT max', 'HLS',0,256,nothing)
cv.createTrackbar('lightness min', 'HLS',0,256,nothing)
cv.createTrackbar('lightness max', 'HLS',0,256,nothing)

while True:
    # выставление нужного цвета
    imgHLS = cv.cvtColor(image, cv.COLOR_BGR2HLS)
    # получаем значения с меню 
    h_min = cv.getTrackbarPos('HUE min', 'HLS')
    s_min = cv.getTrackbarPos('SAT min', 'HLS')
    l_min = cv.getTrackbarPos('lightness min', 'HLS')
    h_max = cv.getTrackbarPos('HUE max', 'HLS')
    s_max = cv.getTrackbarPos('SAT max', 'HLS')
    l_max = cv.getTrackbarPos('lightness max', 'HLS')
    # формируем границы и отсекаем лишние значения 
    lower = np.array([h_min, s_min, l_min])
    upper = np.array([h_max, s_max, l_max])
    # созздаем маску
    mask = cv.inRange(imgHLS,lower, upper)
    # проводим логическую операция объединение
    result = cv.bitwise_and(image, image, mask = mask)
    cv.imshow('image',image)
    cv.imshow('image in HLS',imgHLS)
    cv.imshow('mask',mask)
    cv.imshow('thresholded',result)
    # остановка программы
    key = cv.waitKey(1)
    if  key == ord('q'):
        break

cv.destroyAllWindows()

image_name = image_name[i].split('.')[0]
cv.imwrite(f'output_images/basic_methods_out/{image_name}_HLS_min({lower})_max({upper}).jpg', result)
cv.imwrite(f'output_images/basic_methods_out/{image_name}_HLS_mask_min({lower})_max({upper}).jpg', mask)
cv.imwrite(f'output_images/basic_methods_out/{image_name}_HLS_image_min({lower})_max({upper}).jpg', imgHLS)
