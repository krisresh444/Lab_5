import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,50) #создание независиммых перемнных
y = x

plt.title('Линейная зависимость y = x') #заголовок
plt.xlabel('x') #ось абцисс
plt.ylabel('y') #ось ординат
plt.grid() #включение сетки
plt.plot(x, y, 'r--') #построение графика
plt.show()