import matplotlib.pyplot as plt
import cv2 as cv 
import numpy as np


## 1 Построение диаграммы 3-х канального изображения ##

# import image
path = 'input_images/statues.jpg'
image = cv.imread(path,-1)
image = cv.resize(image, dsize= (700,700), interpolation=cv.INTER_AREA)
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

plt.figure(1)
plt.imshow(image)
plt.title('исходное Изображение')
cv.imwrite('output_images/basic_methods_out/rgb_hist_1_pic.jpg', image)

plt.figure(2)
plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'Red', alpha = 0.3)
plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.3)
plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.3)
plt.legend(['Красный канал (R)', 'Зеленый канал (G)', 'Cиний канал (B)'])
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество')
plt.savefig('output_images/basic_methods_out/rgb_hist_1_hist.jpg')

plt.show()

## 2 Построение диаграммы 1-х канального изображения ##

image1 = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

plt.figure(1)
plt.imshow(image1, cmap = 'gray')
plt.title('original image grayscale')
cv.imwrite('output_images/basic_methods_out/grayscale_orig_pic.jpg', image1)

plt.figure(2)
plt.hist(image1.ravel(), bins = 256, alpha = 0.3)
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество $h(n)$')
plt.title('Grayscale гистограмма')
plt.savefig('output_images/basic_methods_out/grayscale_hist.jpg')
plt.show()


## 3 ## 
"""
Эквализация гистограммы изображения это преобразование гистограммы цвета в однородную функцию плотности (значение пикселей стремятся имеют одинаковый уровень частот) 
"""

dst = cv.equalizeHist(image1)
cv.imshow('original',image1)
cv.imwrite(f'output_images/basic_methods_out/orig_pic_before_equalize.jpg', image1) 
cv.imshow('equalized with histogram',dst)
cv.imwrite(f'output_images/basic_methods_out/orig_pic_after_equalize.jpg', dst) 

plt.figure(1)
counts, bins, bars = plt.hist(image1.ravel(), bins = 256)
plt.hist(counts, bins = bins)
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество $h(n)$')
plt.title('Гистограмма до эквализации')

plt.figure(2)
counts, bins, bars = plt.hist(dst.ravel(), bins = 256)
plt.hist(counts, bins = bins)
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество $h(n)$')
plt.title('Гистограмма после эквализации')
plt.savefig('output_images/basic_methods_out/grayscale_hist_equalized.jpg')

plt.show()
cv.destroyAllWindows()

## 4 ## 

"""
Однако, для пикселей/ объектов переднего плана эффект приводит к размытию и потере (затемнению/высветлению) деталей.
Поэтому используется метод адаптивного HE (adaptive histogram equalization) представленный в opencv функцией CLAHE


createCLAHE 
clipLimit - устанавливает пороговое значение для ограничения контрастности. Более высокие значения обеспечивают большую контрастность. 
Ограничение клипа помогает предотвратить усиление шума, ограничивая контрастность каждой области.
По умолчанию равен 40.0
tileGridSize - определяет размер сетки для выравнивания гистограммы или
кол-во областей на которые будет поделено изображение. Затем происходит выравнивание гистограммы по каждому фрагменту в отдельности.
По умолчанию равен (8, 8)
"""

cv.imshow('equalized with histogram',dst)

sizes = [5,15,50,100]
cliplimits = [3,5,10,15,30]
for i,j in zip(cliplimits,sizes):
    clahe = cv.createCLAHE(clipLimit= j, tileGridSize=(i,i))
    cl = clahe.apply(image1)


    cv.imshow(f'equalized with CLAHE {i,j}',cl)
    cv.imwrite(f'output_images/basic_methods_out/orig_pic_after_clahe_size_{i,i}_clip_{j}.jpg', cl) 


plt.figure(1)
counts, bins, bars = plt.hist(cl.ravel(), bins = 256)
plt.hist(counts, bins = bins)
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество')
plt.savefig('output_images/basic_methods_out/hist_after_clahe.jpg')

plt.figure(2)
counts, bins, bars = plt.hist(dst.ravel(), bins = 256)
plt.hist(counts, bins = bins)
plt.xlabel('Интенсивность $n$')
plt.ylabel('Количество $h(n)$')
plt.title('Гистограмма после эквализации')
plt.savefig('output_images/basic_methods_out/grayscale_hist_equalized.jpg')

plt.show()
cv.destroyAllWindows()

cv.imshow('equalized with histogram',dst)


cv.destroyAllWindows()
