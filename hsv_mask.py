import matplotlib.pyplot as plt
import cv2 as cv 
import numpy as np

# import image
path = 'input_images/'
image_name = ['rabbit1.jpg', 'COCO_train2014_000000006792.jpg','bubles.jpg','COCO_train2014_000000001762.jpg']
i = 0
image = cv.imread(path+image_name[i],-1)
image = cv.GaussianBlur(image, ksize = (5,5), sigmaX= 1.5, sigmaY= 1.5)
# image = cv.morphologyEx(image, cv.MORPH_OPEN, kernel=cv.getStructuringElement(1,(5,5)), iterations = 6)

if len(image.shape) == 2:
    image = cv.cvtColor(image,cv.COLOR_GRAY2BGR)

print(image.shape)


def nothing(a):
    pass

cv.namedWindow('HSV')
cv.resizeWindow('HSV', 500, 300)
cv.createTrackbar('HUE min', 'HSV',0,360,nothing)
cv.createTrackbar('HUE max', 'HSV',0,360,nothing)
cv.createTrackbar('SAT min', 'HSV',0,360,nothing)
cv.createTrackbar('SAT max', 'HSV',0,360,nothing)
cv.createTrackbar('VALUE min', 'HSV',0,255,nothing)
cv.createTrackbar('VALUE max', 'HSV',0,255,nothing)

while True:
    # выставление нужного цвета
    imgHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # получаем значения с меню 
    h_min = cv.getTrackbarPos('HUE min', 'HSV')
    s_min = cv.getTrackbarPos('SAT min', 'HSV')
    v_min = cv.getTrackbarPos('VALUE min', 'HSV')
    h_max = cv.getTrackbarPos('HUE max', 'HSV')
    s_max = cv.getTrackbarPos('SAT max', 'HSV')
    v_max = cv.getTrackbarPos('VALUE max', 'HSV')
    # формируем границы и отсекаем лишние значения 
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # созздаем маску
    mask = cv.inRange(imgHSV,lower, upper)
    # проводим логическую операция объединение
    result = cv.bitwise_and(image, image, mask = mask)
    cv.imshow('image',image)
    cv.imshow('image in HSV',imgHSV)
    cv.imshow('mask',mask)
    cv.imshow('thresholde',result)
    # остановка программы
    key = cv.waitKey(1)
    if  key == ord('q'):
        break

cv.destroyAllWindows()

image_name = image_name[i].split('.')[0]
cv.imwrite(f'output_images/basic_methods_out/{image_name}_HSV_min({lower})_max({upper}).jpg', result)
cv.imwrite(f'output_images/basic_methods_out/{image_name}_HSV_mask_min({lower})_max({upper}).jpg', mask)
cv.imwrite(f'output_images/basic_methods_out/{image_name}_HSV_image_min({lower})_max({upper}).jpg', imgHSV)
