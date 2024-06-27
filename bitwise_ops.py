# скрипт по работе битовых операторов bitwise_and, bitwise_or, bitwise_xor 

import cv2 as cv
import numpy as np

# для сохранения результата
path = 'output_images/basic_methods_out'

"""
Bitwise операции это логические операторы для пикселей изображений 
В случае AND - пересечений двух изображений
В случае OR - объединение объектов 
В случае NOT - разность объектов 
В случае XOR -  обратное объединение двух изображений, 
т.е. в местах пересечений значения обращаются в 0, а там где не пересекаются остаются неизменными   

В случае использования маски результат bitwise операций затем обрезается по форме маски
"""
black = np.zeros((480, 480), dtype = "uint8")
rect = cv.rectangle(black.copy(), (50, 60), (400, 200), 255, -1)
circle = cv.circle(black.copy(), (240, 240), 150, 255, -1)
mask = cv.circle(black.copy(), (124, 124), 150, 255, -1)

cv.imshow('Rectangle', rect)
cv.imshow('Circle', circle)
cv.imshow('Mask', mask)

cv.imwrite(f"{path}/Circle.jpg", circle)
cv.imwrite(f"{path}/Rectangle.jpg", rect)
cv.imwrite(f"{path}/Mask.jpg", mask)

cv.waitKey(0)
cv.destroyAllWindows()

bit_and_1 = cv.bitwise_and(src1 = rect, src2 = circle, dst = None, mask = None)
cv.imshow("rect", rect)
cv.imshow("circle", circle)
cv.imshow("Bitwise op AND without mask", bit_and_1)
cv.imwrite(f"{path}/Bitwise op AND without mask.jpg", bit_and_1)

bit_and_2 = cv.bitwise_and(src1 = rect, src2 = circle, dst = None, mask = mask)
cv.imshow("Mask", mask)
cv.imshow("Bitwise op AND with mask", bit_and_2)
cv.imwrite(f"{path}/Bitwise op AND with mask.jpg", bit_and_2)

cv.waitKey(0)
cv.destroyAllWindows()

bit_or_1 = cv.bitwise_or(src1 = rect, src2 = circle, dst = None, mask = None)
cv.imshow("rect", rect)
cv.imshow("circle", circle)
cv.imshow("Bitwise op OR without mask", bit_or_1)
cv.imwrite(f"{path}/Bitwise op OR without mask.jpg", bit_or_1)

bit_or_2 = cv.bitwise_or(src1 = rect, src2 = circle, dst = None, mask = mask)
cv.imshow("Mask", mask)
cv.imshow("Bitwise op OR with mask", bit_or_2)
cv.imwrite(f"{path}/Bitwise op OR with mask.jpg", bit_or_2)

cv.waitKey(0)
cv.destroyAllWindows()

bit_not_1 = cv.bitwise_not(src = rect, mask = mask)
cv.imshow("rect", rect)
cv.imshow("circle", circle)
cv.imshow("Rectangle Bitwise op NOT with mask", bit_not_1)
cv.imwrite(f"{path}/Rectangle Bitwise op NOT with mask.jpg", bit_not_1)

bit_not_2 = cv.bitwise_not(src =circle, dst = None, mask = mask)
cv.imshow("Mask", mask)
cv.imshow("Circle Bitwise op NOT with mask", bit_not_2)
cv.imwrite(f"{path}/Circle Bitwise op NOT with mask.jpg", bit_not_2)

bit_not_3 = cv.bitwise_not(src = rect, mask = None)
cv.imshow("rect", rect)
cv.imshow("circle", circle)
cv.imshow("Rectangle Bitwise op NOT without mask", bit_not_3)
cv.imwrite(f"{path}/Rectangle Bitwise op NOT without mask.jpg", bit_not_3)

bit_not_4 = cv.bitwise_not(src =circle, dst = None, mask = None)
cv.imshow("Mask", mask)
cv.imshow("Circle Bitwise op NOT without mask", bit_not_4)
cv.imwrite(f"{path}/Circle Bitwise op NOT without mask.jpg", bit_not_4)


cv.waitKey(0)
cv.destroyAllWindows()

bit_xor_1 = cv.bitwise_xor(src1 = rect, src2 = circle, dst = None, mask = None)
cv.imshow("rect", rect)
cv.imshow("circle", circle)
cv.imshow("Bitwise op XOR without mask", bit_xor_1)
cv.imwrite(f"{path}/Bitwise op XOR without mask.jpg", bit_xor_1)

bit_xor_2 = cv.bitwise_xor(src1 = rect, src2 = circle, dst = None, mask = mask)
cv.imshow("Mask", mask)
cv.imshow("Bitwise op XOR with mask", bit_xor_2)
cv.imwrite(f"{path}/Bitwise op XOR with mask.jpg", bit_xor_2)

cv.waitKey(0)
cv.destroyAllWindows()
