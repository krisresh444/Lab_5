# Лабораторная работа №5
## Задание
Создайте в каталоге для данной ЛР в своём репозитории виртуальное окружение и установите в него matplotlib и numpy. Создайте файл requirements.txt.
Откройте книгу [1] и выполните уроки 1-3. Первый урок можно начинать со стр. 8.
Выберите одну из неразрывных функции своего варианта из лабораторной работы №2, постройте график этой функции и касательную к ней. Добавьте на график заголовок, подписи осей, легенду, сетку, а также аннотацию к точке касания.
Добавьте в корень своего репозитория файл .gitignore отсюда, перед тем как делать очередной коммит.
Оформите отчёт в README.md. Отчёт должен содержать:
графики, построенные во время выполнения уроков из книги
объяснения процесса решения и график по заданию 4
Склонируйте этот репозиторий НЕ в ваш репозиторий, а рядом. Изучите использование этого инструмента и создайте pdf-версию своего отчёта из README.md. Добавьте её в репозиторий.
### Описание проделанной работы
1. Cоздала “пустое” виртуальное окружение с помощью команды `python3 -m venv env`.Активировала виртуальное окружение с помощью `source env/bin/activate`.Обновила пакетный менеджер с помощью `pip install -U pip`.Устанавливила пакет с помощью `pip install mutplotlib`.А так же установила `PyQt6`.Перенесла все установленных пакетов в новое окружение с помощью `pip freeze > requirements.txt`.Обновила пакетный менеджер и затем выполнила `pip install -r requirements.txt`

2. Выполнила урок 1
<image src = 1.2.png alt="результат программы">
<image src = 1.3.png alt="результат программы">
<image src = 1.4.png alt="результат программы">
<image src = 1.5.png alt="результат программы">
<image src = 1.6.png alt="результат программы">

- Выполнила урок 2
<image src = 2.png alt="результат программы">

- Выполнила урок 3
<image src = 3.1.png alt="результат программы">
<image src = 3.2.png alt="результат программы">

3. График функции по Варианту 11
$$
f(x) = x**2*arctg(x)
$$
Написала программу
```
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
```
Построила график функции и касательную к ней. Добавила на график заголовок, подписи осей, легенду, сетку, а также аннотацию к точке касания.
<image src = 4.png alt="результат программы">

4. Добавила в корень своего репозитория файл `.gitignore`
5. Написала отчет
