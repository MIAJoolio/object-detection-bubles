import cv2 as cv
import numpy as np


"""
file - название и местоположение файла
flags - цвета и различные варианты для загрузки изображения
cv2.IMREAD_COLOR (или 1) - цветное изображение. Значение по умолчанию.
cv2.IMREAD_GRAYSCALE (или 0) - grayscale изображение
cv2.IMREAD_UNCHANGED (или -1) - загружает изображение в его исходном виде без изменений 
Другие специфические форматы тут
https://gregorkovalcik.github.io/opencv_contrib/d4/da8/group__imgcodecs.html#gga61d9b0126a3e57d9277ac48327799c80ab6573b69300c092b61800222fe555953
"""
# загрузка изображения
image = cv.imread('input_images/rabbit1.jpg',-1)
path = 'output_images/basic_methods_out'

# Displaying the results
cv.imshow('Original Image', image)
cv.imwrite(f'{path}/Original Image.jpg', image)

"""
src - изображение
dsize - кортеж для выбора точного размера изображения
fx - множитель разрешения по оси x
fy - множитель разрешения по оси y
Если хочется использовать fx, fy необходимо до их упоминания использовать dsize = None
interpolation - 
Виды интерполяции:
cv2.INTER_NEAREST - Nearest neighbor interpolation.
cv2.INTER_LINEAR - Bilinear interpolation (default).
cv2.INTER_CUBIC - Bicubic interpolation.
cv2.INTER_LANCZOS4 - Lanczos interpolation over 8x8 neighborhood.
cv2.INTER_AREA - Resampling using pixel area relation

https://en.wikipedia.org/wiki/Multivariate_interpolation
https://gregorkovalcik.github.io/opencv_contrib/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121
"""
# изменнеие размера/ разрешени
image1 = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)
cv.imshow('Resized Image 1', image1)
cv.imwrite(f'{path}/Resized Image 1.jpg', image1)

image2 = cv.resize(image, dsize = (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized Image 2', image2)
cv.imwrite(f'{path}/Resized Image 2.jpg', image2)


# Rotations 

# переворот значений относительно оси х или y
"""
flipCode - 0 - по оси x, 1 или любое пол. число - по оси y 
"""
flip = cv.flip(image2, 3) 
cv.imshow('Flipped Image', flip)
cv.imwrite(f'{path}/Flipped Image.jpg', flip)

# переворот относительно главной диагонали
transpose = cv.transpose(image2)
cv.imshow('Transposed Image', transpose)
cv.imwrite(f'{path}/Transposed Image.jpg', transpose)

# на 45 градусов вокруг его центра
"""
getRotationMatrix2D 

center - координаты центра
angle - угол наклонка
scale - кожффициент для уменьшения размера изображения

warpAffine

M - матрица преобразования 2x3 (аффинная матрица), которая определяет преобразование
dsize,fx,fy аналогично функции resize
flags - аналогично параметру interpolations функции resize
borderMode - 
    cv2.BORDER_CONSTANT - добавляет границу постоянного цвета
    cv2.BORDER_REPLICATE - повторяет ближайшие пиксели границы
    cv2.BORDER_REFLECT - отражает пиксели границы
    cv2.BORDER_WRAP - обтекает изображение по границе
можно использовать, когда происходит объединение двух изображений

borderValue - цвет границы 0 (черный) - для одного канала (0,0,0) - для 3 каналов  
"""
# центр изображения 
rows, cols = image2.shape[:2]
rotation_matrix = cv.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)
warpAffine = cv.warpAffine(image2, rotation_matrix, (cols, rows))
cv.imshow('Rotated Image on 45 degree', warpAffine)
cv.imwrite(f'{path}/Rotated Image on 45 degree.jpg', warpAffine)


# выбор конкретной области 
cropped_image = image2[200:400, 200:500]  
cv.imshow('Cropped image', cropped_image)
cv.imwrite(f'{path}/Cropped Image.jpg', cropped_image)

# выбор цветовой палитры
gray_image = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)  
cv.imshow('Grayscale image', gray_image)
cv.imwrite(f'{path}/Grayscale image.jpg', gray_image)


cv.waitKey(0)
cv.destroyAllWindows()