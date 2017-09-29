import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from vk_clients import *

get_user = GettingID('id18530051')
user = get_user.execute()
user_id = user.get('id')

get_friends = GettingFriends(user_id)
friends = get_friends.execute()

age_list = [0 for i in range(200)]
today = datetime.now()
a = []
c = []
print(user.get('last_name'), user.get('first_name'), sep=' ')

for f in friends:
    bdate_str = f.get('bdate')
    try:
        bdate = datetime.strptime(bdate_str, '%d.%m.%Y')
        days = (today-bdate).days

        age = days // 365

        age_list[age] += 1

    except:
         pass
for i in range(200):
    if age_list[i]>0:
        print(i,': ','#'*age_list[i])
        a.append(i) ;
        c.append(age_list[i]) ;





import pylab


if __name__ == '__main__':
    xdata = a
    ydata = c

    pylab.bar (xdata, ydata)
    pylab.show()





import pylab
# !!! Импортируем пакет со вспомогательными функциями
from matplotlib import mlab

# Интервал изменения переменной по оси X
xmin = 0
xmax = 120

# Шаг между точками
dx = 1

# !!! Создадим список координат по оиси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange (xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [a for c in xlist]

# !!! Нарисуем одномерный график
pylab.plot (ylist)

# !!! Покажем окно с нарисованным графиком
pylab.show()