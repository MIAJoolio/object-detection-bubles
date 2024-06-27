import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

from skimage.exposure import (
    adjust_log,
    adjust_gamma,
    adjust_sigmoid,

)


fmt = 'jpg'
filename = 'rabbit1'
path = f'input_images/{filename}.{fmt}'

mat1 = cv.imread(path, 0)
mat2 = cv.imread(path, -1)
# cv.imwrite("output_images/basic_methods_out/orig_img_grayscale.jpg", mat1)

add = cv.add(mat1, 100)
cv.imshow("Addition", add)
cv.imwrite("output_images/basic_methods_out/Addition.jpg", add)
# Subtract the matrices
subtract = cv.subtract(mat1, 100)
cv.imshow("Subtraction", subtract)
cv.imwrite("output_images/basic_methods_out/Subtraction.jpg", subtract)
# Multiply the matrices element-wise
multiply = cv.multiply(mat1, 2)
cv.imshow("Multiplication", multiply)
cv.imwrite("output_images/basic_methods_out/Multiplication.jpg", multiply)
# Divide the matrices element-wise
divide = cv.divide(mat1, 2)
cv.imshow("Division", divide)
cv.imwrite("output_images/basic_methods_out/Division.jpg", divide)

cv.waitKey(0)

"""
src - входное изображение
dst - результирующее изображение
alpha - нижняя граница диапазона
beta - верхняя граница диапазона
norm_type - тип применяемой нормализации. Это может быть один из следующих вариантов:
    cv2.NORM_MINMAX - нормализует по заданному диапазону [альфа, бета].
    cv2.NORM_INF - нормализует, масштабируя его по максимальному абсолютному значению.
    cv2.NORM_L1 - нормализует по сумме абсолютных значений.
    cv2.NORM_L2 - Нормализует по евклидовой норме.
dtype - Желаемый тип выходного массива. Если -1, то выходной массив будет иметь тот же тип, что и src.
маска - Необязательная маска операции. Она должна иметь тот же размер, что и src.
"""

normalize = cv.normalize(mat1, None, 0, 1, cv.NORM_MINMAX)
cv.imshow("Normalize", normalize)
cv.imwrite("output_images/basic_methods_out/Normalize.jpg", normalize)
normalize2 = cv.normalize(mat2, None, 100, 255, cv.NORM_MINMAX)
cv.imshow("Normalize", normalize2)
cv.imwrite("output_images/basic_methods_out/Normalize2.jpg", normalize2)
# Convert scale and absolute
"""
alpha - коэффициент умножения
beta - значения для добавление/вычитания
"""
convert = cv.convertScaleAbs(mat1, alpha=2, beta=0)
cv.imshow("ConvertScaleAbs", convert)

"""
Для возведения в степень необходимо 
1. перевести изображение в глубину 32 или 64, т.к. возведение в степень для значений 0-255 не имеет смысла
В глубине 32 значения могут изменяться в большем диапазоне.
2. произвести возведение в степень методом cv.pow
3. нормализовать изображение в формате 0-255 и перевести в 8-битное представление
""" 
mat_1_32 = mat1.astype(np.float32)
power = cv.pow(mat_1_32, 2)
power_norm = cv.normalize(power, None, 0, 255, cv.NORM_MINMAX).astype(np.uint8)
cv.imshow("Power_of_2 to image", power_norm)
cv.imwrite("output_images/basic_methods_out/Power_of_2.jpg", power_norm)

log = cv.log(mat_1_32)
log_norm = cv.normalize(log, None, 0, 255, cv.NORM_MINMAX).astype(np.uint8)
cv.imshow("Logarithm", log_norm)
cv.imwrite("output_images/basic_methods_out/Logarithm.jpg", log_norm)

# log трансформация skimage 
# https://scikit-image.org/docs/stable/api/skimage.exposure.html#skimage.exposure.match_histograms
"""
gain - множитель для логарифма
inv - bool для расчета преобразования 
"""
log_ski = adjust_log(normalize, gain = 1, inv = True)
# cv.imshow("Logarithm ski", log_ski)
plt.imshow(log_ski, cmap = 'gray')
plt.show()
cv.imwrite("output_images/basic_methods_out/Skimage_log_transf.jpg", log_ski)


cv.waitKey(0)

# from skimage.exposure import (
#     adjust_log,
#     adjust_gamma,
#     adjust_sigmoid,

# )

# # Apply log transformation
# log = adjust_log(mat1)
# print("Log:\n", log)
# # Apply exp transformation
# exp = cv.exp(np.uint8(mat1))
# print("Exp:\n", exp)
# # 7. Element-wise Operations
# # Apply power transformation
# pow = cv.pow(np.uint8(mat1), 2)
# print("Power:\n", pow)
# # Apply sqrt transformation
# sqrt = cv.sqrt(np.uint8(mat1))
# print("Sqrt:\n", sqrt)







# # Get the perspective transformation matrix
# matrix = cv.getPerspectiveTransform(mat1, add)
# cv.imshow("getPerspectiveTransform", matrix)

# cv.waitKey(0)


# # Create binary matrices
# compare = cv.compare(mat1, mat1, cv.CMP_EQ)
# cv.imshow("Comparsion add & substract", compare)

# cv.waitKey(0)
