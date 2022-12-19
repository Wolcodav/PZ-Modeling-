import numpy as py
import matplotlib.pyplot as plt
import math as mh
import numpy as np
import csv 


#Заданные заданием пределы. Шаг выбран произвольно
x_min = -5
x_max = 5
dx = 0.1

#Создание массива точек с заданным шагом и их подстановка в функцию y
x = py.arange(x_min , x_max + 1, dx)
y = -20*py.exp(-0.2*py.power(0.5*x*x, 0.5))-py.exp(0.5*(py.cos(2*mh.pi*x)+1))+mh.e+20

#Подсчет количества точек
num_max = int(((abs(x_max)+abs(x_min))/dx)+1)
num = py.arange(1, num_max + 1)

#Заталкивание всех точек в один массив
n = 0
out = []
while n < num_max:
  out.append((num[n], x[n], y[n]))
  n += 1

#out += [[num[n]] + [x[n]] + [y[n]]]

#Процесс записи значений в файл
#file = open(r"results\data.cvs", "w", encoding = "ISO-8859-5") 
with open(r"results/data.cvs", "w", encoding = "ISO-8859-5") as INFs:
  
    writer = csv.writer(INFs)
    
    writer.writerows(
      out
    )    

#Построение графика
plt.plot(x,y)   
plt.title("Line graph")   
plt.ylabel('Y axis')

plt.xlabel('X axis')
plt.xlim(x_min, x_max)

plt.show()

#Вывод итоговых значений
print(np.array(out))
print("\nПрограмма завершила свою работу - повезло")











































