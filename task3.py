age = int(input("Возраст автомобиля: "))
volume_d = int(input("Oбъем двигателя: "))
if age < 3:
    price = int(input("Цена автомобиля (евро): "))


if age < 3: 
    if 8500 <= price < 16700:
        cost = 2.5
    elif 16700 <= price < 42300:
        cost = 5.5
    elif 42300 <= price < 84500:
        cost = 7.5
    elif 84500 <= price < 169000:
        cost = 15
    elif price >= 169000:
        cost = 20
elif 3 <= age <= 5: 
    if volume_d < 1000:
        cost = 1.5
    elif 1000 <= volume_d < 1500:
        cost = 1.7
    elif 1500 <= volume_d < 1800:
        cost = 2.5
    elif 1800 <= volume_d < 2300:
        cost = 2.7
    elif 2300 <= volume_d < 3000:
        cost = 3
    elif volume_d >= 3000:
        cost = 3.6

result_calc = cost * volume_d

print(f"Таможенные отчисления на ваш автомобиль составят {result_calc}")