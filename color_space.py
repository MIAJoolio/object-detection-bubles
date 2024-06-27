import matplotlib.pyplot as plt
import cv2 as cv 
import numpy as np


# import image
path = 'input_images/'
image_name = ['rabbit1.jpg', 'dark_london_orig.png', 'heads.jpg', 'galaxy2.png','mrt_3.jpg', 'bubles.jpg']
i = 0
image = cv.imread(path+image_name[i],-1)

colors = {
    'HSV':cv.COLOR_RGB2HSV,
    'HLS':cv.COLOR_RGB2HLS,
    'BGR':cv.COLOR_RGB2BGR,
    'GRAY':cv.COLOR_RGB2GRAY,
    'Lab':cv.COLOR_BGR2Lab,
    'LAB': cv.COLOR_BGR2LAB,
    'LUV':cv.COLOR_RGB2LUV,
    'XYZ':cv.COLOR_BGR2XYZ,
    'YUV': cv.COLOR_RGB2YUV
}

"""
cvtColor функция для выбора цветовой ппалитры
src - исходное изображение
code - флаг цвета выше представлены наиболее распространенные палитры
"""

for color_pallette in colors.keys():
    image = cv.imread(path+image_name[i],-1)
    image = cv.resize(image, dsize = (400,400), interpolation=cv.INTER_AREA)
    image = cv.cvtColor(image, colors[color_pallette])

    cv.imshow(f'{color_pallette}', image)
    cv.imwrite(f'output_images/basic_methods_out/{image_name[i]}_{color_pallette}.jpg', image)

cv.waitKey(0)
