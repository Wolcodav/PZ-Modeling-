import wget
import os.path
import numpy as py
import scipy as sy
import json
import pathlib
import matplotlib.pyplot as plt
import math as mh
import scipy.constants as sycon
import scipy.special as sycp

url = 'https://jenyay.net/uploads/Student/Modelling/task_02_02.txt'

"Шаг дискретизации частоты, выбирается исходя из свободного времени для расчетов"
dx = 100000 

"Процесс проверки наличия файла и его загрузки, в также присвоение значений моего варианта в список a"
if (os.path.exists('test.txt')==0):
    wget.download(url, r'test.txt')
var = 2
with open('test.txt', 'r') as file:
    for i in range (0, var, 1):
        next(file)
    
    line = next(file)
    a = (list(map(float, line.split())))
    a.pop(0)
print(a)
    

"Присвоение значений диаметру сферы, а также минимальной и максимальной частоте соответсвенно"
D = a[0]    
fmin = a[1]
fmax = a[2]

"Создание массива частот с заданным шагом дискретизации"
f = py.arange(fmin, fmax, dx)

"Определение необходимых для расчета значений"
R = D / 2
lmbd = sycon.c / f 
k = 2 * mh.pi / lmbd

"Определение a_n. b_n. h_n с помощью сферических ф-й Бесселя из библиотеки scipy"
def hn(n, x): return sycp.spherical_jn(n, x) + 1j * sycp.spherical_yn(n, x)
def bn(n, x): return (x * sycp.spherical_jn(n - 1, x) - n * sycp.spherical_jn(n, x)) / (x * hn(n - 1, x) - n * hn(n, x))
def an(n, x): return sycp.spherical_jn(n, x) / hn(n, x)

"Определение ЭПР, записанного как RCS"
arr_sum = [((-1) ** n) * (n+0.5) * (bn(n, k * R) - an(n, k * R)) for n in range(1, 30)]
summa = py.sum(arr_sum, axis=0)
rcs = (lmbd ** 2) / py.pi * (py.abs(summa) ** 2)

print(arr_sum)

"Процесс записи требуемых значений в файл"
res = {
"data": [
{"freq": float(f1), "lambd": float(lmbd1),"rcs": float(rcs1)} for f1, lmbd1, rcs1 in zip(f, lmbd, rcs)
]
}

path = pathlib.Path("results")
path.mkdir(exist_ok = True)
file = path / "result_2.json"
out = file.open("w")
json.dump(res, out, indent=2)
out.close()

"Построение графика ЭПР от частоты"
plt.plot(f / 10e6, rcs)
plt.xlabel("$f, МГц$")
plt.ylabel(r"$\sigma, м^2$")
plt.grid()
plt.show()
