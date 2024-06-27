import matplotlib.pyplot as plt
import cv2 as cv 
import numpy as np

"""
Скрипт по 
"""

# import image
path = 'input_images/'
image_name =  'dark_london_orig.png' #rabbit1.jpg # heads.jpg galaxy2.png
image = cv.imread(path+image_name,-1)
print(image.shape)

def nothing(a):
    pass

cv.namedWindow('Coefs')
cv.resizeWindow('Coefs', 700, 250)
# коэффициент для изменения контрастности 
cv.createTrackbar('alpha_100', 'Coefs',0,1000,nothing) # для лучшей масштабируемости единицы измерения в 100, т.е. 100 = 1 / 150 = 1.5
# коэффициент для изменения яркости
cv.createTrackbar('beta', 'Coefs',0,256,nothing)
# дополнительный параметр для изменения матрицы оператора (src2) 
cv.createTrackbar('gamma', 'Coefs',0,256,nothing)


while True:
    alpha = cv.getTrackbarPos('alpha_100', 'Coefs')/100
    beta = cv.getTrackbarPos('beta', 'Coefs')
    gamma = cv.getTrackbarPos('gamma', 'Coefs')
    
    # ссылка на документацию - https://docs.opencv.org/3.4/d2/de8/group__core__array.html#gafafb2513349db3bcff51f54ee5592a19 
    # 'src1' : image, # image, # оригинальное изображение
    # 'src2' : np.ones(image.shape,image.dtype), # матрица оператор  
    # "alpha" : 1, # коэффициент для изменения контрастности 
    # 'gamma' : -128, # дополнительный параметр для изменения матрицы оператора (src2) 
    # 'beta' : 0, # коэффициент для изменения яркости
    # 'dtype': -1 # глубина изображения вычисляемая в значениях пикселей, например, при CV_8 максимальное равно 255 


    new_image = cv.addWeighted(src1 = image, src2=np.ones(image.shape,image.dtype),
                               alpha=alpha, beta=beta, gamma=gamma)
    
    cv.imshow('image',image)
    cv.imshow('image changed',new_image)

    # если нужно можно добавить гистограмму, но тогда нужно дважды нажимать q для обновления результатов 
    # fig = plt.figure()
    # fig.add_subplot(211)
    # # гистограмма распределения значений пикселей до и после изменения 
    # plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'Red', alpha = 0.5)
    # plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    # plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.1) 
    # plt.legend(['Красный канал (R)', 'Зеленый канал (G)', 'Cиний канал (B)'])
    # plt.xlabel('Интенсивность $n$')
    # plt.ylabel('Количество')
    # plt.title('Распределение значений пикселей на оригинальном изображении')

    # fig.add_subplot(212)
    # plt.hist(new_image[:, :, 0].ravel(), bins = 256, color = 'Red', alpha = 0.5)
    # plt.hist(new_image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    # plt.hist(new_image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5) 
    # plt.legend(['Красный канал (R)', 'Зеленый канал (G)', 'Cиний канал (B)'])
    # plt.xlabel('Интенсивность $n$')
    # plt.ylabel('Количество')
    # plt.title('Распределение значений пикселей на обработанном изображении')
    # plt.show()

    # в этом примере нужен двойное надатие q
    key = cv.waitKey(1)
    if  key == ord('q'):
        break




# cap.release()
cv.destroyAllWindows()

cv.imwrite(f'output_images/basic_methods_out/{image_name}_{alpha},{beta},{gamma}_brightness_2.jpg', new_image)
