#Импорт библиотек
import matplotlib.pyplot as mat
import pandas as pd
#Конвертирование из parquet в csv
table = pd.read_parquet('titanic.parquet')
table.to_csv('titanic.csv')

#Присвоение переменной данными из titanic.csv
c = pd.read_csv('titanic.csv')
k = c.groupby(['Pclass','Survived']).size().unstack(fill_value=0)
#Работа с процентами
pr = k.div(k.sum(axis=1),axis=0) * 100 
pr.plot(kind='bar',stacked=True)
print(k)
#Создание графика
mat.title('Выживаемость пассажиров Титаника') 
mat.xlabel('Классы') 
mat.legend(['Выжил','Не выжил']) 
mat.xticks(rotation = 0)
#Вывод графика
mat.show()
