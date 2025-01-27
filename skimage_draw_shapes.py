import matplotlib.pyplot as plt
import cv2 as cv 
import numpy as np

from skimage.draw import (
    line,
    polygon,
    disk,
    circle_perimeter,
    ellipse,
    ellipse_perimeter,
    bezier_curve,
)


"""
https://scikit-image.org/docs/stable/auto_examples/edges/plot_shapes.html#sphx-glr-auto-examples-edges-plot-shapes-py

Объекты в opencv

Представлены методами:

1. линия (cv2.line) 
2. прямоугольник (cv2.rectangle)
3. круг (cv2.circle)
4. эллипс (cv2.ellipse)
5. полигон (cv2.polylines)
6. заполненный полигон (cv2.fillPoly)
#-----------------------------------------------------------#
Есть общие параметры цвета и толщины линии 

image - исходное изображение 
color - цвет линии (B, G, R). 
thickness - толщина линии. Укажите cv.FILLED или -1 для заполнения цветом

#-----------------------------------------------------------#
Детали по другим параметрам представлены ниже

######################
Линия & Прямоугольник
######################

pt1 - координаты начальной точки линии (x, y).
pt2 - координаты конечной точки линии (x, y).

pt1 - координаты верхнего левого угла прямоугольника (x, y).
pt2 - координаты правого нижнего угла (x, y).
#-----------------------------------------------------------#
######
Круг
######

center -  координаты центра окружности (x, y).
radius -  радиус окружности.
#-----------------------------------------------------------#
######
Эллипс
######

center -  координаты центра эллипса (x, y).
axes - длина большой и малой осей (major_axis, minor_axis).
angle - угол поворота эллипса в градусах.
startAngle -  начальный угол эллиптической дуги.
endAngle -  конечный угол эллиптической дуги.
#-----------------------------------------------------------#
######
Полигон
######

pts -  cписок точек, определяющих полигон.
isClosed -  bool для того, чтобы полигон был закрыт.
#-----------------------------------------------------------#
######
Заполненный Полигон
######

points -  List of points defining the polygon.
#-----------------------------------------------------------#
######
Функция для добавления текста (cv2.putText)
######

text -  текстовая строка, которую нужно нарисовать.
org -  Нижний левый угол текста (x, y).
fontFace -  Тип шрифта (например, cv2.FONT_HERSHEY_SIMPLEX).
fontScale -  Коэффициент масштабирования шрифта, который умножается на базовый размер конкретного шрифта.

Сглаживание
При рисовании линии, прямоугольника, круга или текста сглаживание обеспечивает сглаживание краев этих фигур за счет смешивания цветов на границе. Это особенно важно при рисовании под неортогональными углами или при отображении текста.
"""

# Create a black image
image = np.zeros((500, 500, 3), np.uint8)

# Draw a line
cv.line(img = image
        , pt1  = (100, 0)
        , pt2 = (200, 200)
        , color = (255, 0, 0)
        , thickness = 3)

# Draw a rectangle
cv.rectangle(img = image
             , pt1 = (200, 200)
             , pt2 = (400, 400)
             , color = (0, 255, 0)
             , thickness = 3)

# Draw a circle
cv.circle(img = image
          , center = (450, 450)
          , radius = 50
          , color = (0, 0, 255)
          , thickness= cv.FILLED) 

# Draw an ellipse
cv.ellipse(img = image
           , center = (200, 100)
           , axes = (50, 100) # y,x радиусы
           , angle = 135 # для поворота элипса относительно центра
           , startAngle = 90 # степень покрытия эллипса
           , endAngle = 270 # 
           , color = (0, 0, 255)
           , thickness  = -1)

# Draw a polygon
points = np.array([[100, 50], [200, 300], [460, 200], [500, 0]], np.int32)
points = points.reshape((-1, 1, 2))
print(points)
cv.polylines(img = image
             , pts = [points]
             , isClosed = True # если False, то i-1 и i точки не будут соеденины
             , color = (0, 255, 255)
             , thickness = 2)

# Put text
cv.putText(img = image
           , text = 'Basic Shapes opencv'
           , org = (30, 450)
           , fontFace = cv.FONT_HERSHEY_SIMPLEX
           , fontScale = 1
           , color = (255, 255, 255)
           , thickness = 2
           , lineType = cv.LINE_AA)

# Display the image
cv.imshow('Image', image)
cv.waitKey(0)
