import pandas as pd
import numpy as np

#1

employees = pd.DataFrame([
    [1, 'Баранов', 'Егор', 'Александрович', 'менеджер', 70000],
    [2, 'Волков', 'Владимир', 'Владимирович', 'мастер', 50000],
    [3, 'Гусев', 'Александр', 'Дмитриевич', 'менеджер', 70000],
    [4, 'Жуков', 'Олег', 'Григорьевич', 'рабочий', 40000],
    [5, 'Зайцев', 'Михаил', 'Егорович', 'мастер', 50000],
    [6, 'Орлов', 'Сергей', 'Олегович', 'директор', 90000],
    [7, 'Лебедев', 'Денис', 'Александрович', 'рабочий', 40000],
    [8, 'Медведев', 'Дмитрий', 'Ярославович', 'мастер', 50000],
    [9, 'Раков', 'Николай', 'Ильич', 'менеджер', 70000],
    [10, 'Щукин', 'Григорий', 'Георгиевич', 'рабочий', 40000],
    ],
    columns=['Номер', 'Фамилия', 'Имя', 'Отчество', 'Должность', 'Оклад'])

print(employees)

employees['Аванс'] = employees['Оклад']*0.4
employees['Пенсионный фонд'] = employees['Оклад']*0.01
employees['Налог'] = (employees['Оклад'] - employees['Пенсионный фонд']-12792)*0.13
employees['К выдаче'] = employees['Оклад']-employees['Аванс']-employees['Пенсионный фонд']-employees['Налог']

print(employees)

#2

df = pd.DataFrame([
    [1, '2022-11-01', 5],
    [2, '2022-11-05', 10],
    [3, '2022-11-06', 30],
    [4, '2022-11-08', 2],
    [5, '2022-11-10', 7],
    [6, '2022-11-12', 12],
    [7, '2022-11-14', 26],
    [8, '2022-11-16', 33],
    [9, '2022-11-18', 3],
    [10, '2022-11-20', 6],
    ],
    columns=['Номер', 'Дата', 'Время разговора'])

df['Дата'] = pd.to_datetime(df.Дата, format = '%Y-%m-%d')
df['День недели'] = df.Дата.dt.dayofweek
df['Час суток'] = np.random.randint(0, 24, 10)
print(df)

tarif = []
for i in range(len(df)):
    if 5 <= df['День недели'].iloc[i] <= 6:
        tarif.append(0.2)
    elif 0 <= df['День недели'].iloc[i] <=4 and 8 <= df['Час суток'].iloc[i] < 21:
        tarif.append(0.5)
    else:
        tarif.append(0.1)

df['Тариф'] = tarif
df['Стоимость разговора'] = df['Время разговора']*df['Тариф']

print(df)

#Индекс дня недели
#0 : понедельник
#1 : вторник
#2 : среда
#3 : Четверг
#4 : пятница
#5 : суббота
#6 : воскресенье