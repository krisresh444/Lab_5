import matplotlib.pyplot as plt
import numpy as np
from math import *

def f(x):
    return (x**2)*(atan(x)) #задала функцию

x = np.linspace(-3, 3, 1000) #список точек от -3 до 3 (1000 точек)
y1 = [f(i) for i in x] #список точек функции из варианта
y2 = [1 for i in x] #касательная в точке 0

plt.title('Вариант 11') #заголовок
plt.xlabel('x') #ось абцисс
plt.ylabel('y') #ось ординат
plt.grid() #включение сетки
plt.plot(x, y1, label='(x**2)*(atan(x))') #построение функции
plt.plot(x, y2, 'r', label='Касательная') #построение касательной
plt.text(0.785, 1.5, 'точка касания') #аннотация
plt.legend() #легенда
plt.show()