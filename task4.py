incident_type = ['ложное срабатывание', 'событие', 'инцидент', 'ложное срабатывание', 'инцидент', 'ложное срабатывание', 'ложное срабатывание', 'событие', 'ложное срабатывание', 'инцидент', 'ложное срабатывание', 'инцидент', 'ложное срабатывание', 'ложное срабатывание', 'инцидент', 'событие', 'событие', 'событие', 'ложное срабатывание', 'ложное срабатывание', 'ложное срабатывание', 'ложное срабатывание', 'инцидент']
owner = ['ivanov', 'petrov', 'meshkov','alexandrova', 'potanina', 'druyan', 'alexandrova', 'meshkov', 'petrov', 'potanina', 'ivanov', 'potanina', 'meshkov', 'meshkov', 'potanina', 'ivanov', 'druyan', 'druyan', 'potanina', 'ivanov', 'meshkov', 'meshkov', 'petrov']
minutes = [5, 7, 19, 8, 7, 4, 4, 19, 6, 12, 4, 17, 4, 6, 4, 5, 2, 18, 14, 13, 3, 17, 2]

#  1. Рассчитать сумму времени в часах, затраченное диспетчером Александром на инциденты.
total_minutes_incident = sum(minutes)
if total_minutes_incident>59:
    print('Общая сумма времени, которое потребовалось диспетчеру Александру, на работу с инцидентами, составила', total_minutes_incident//60,'ч.', int((total_minutes_incident/60-total_minutes_incident//60)*60), 'мин. '  )
else:
    print('Общая сумма времени, которое потребовалось диспетчеру Александру, на работу с инцидентами, составила', int((total_minutes_incident/60-total_minutes_incident//60)*60), 'мин. '  )
    
# 2. Рассчитать среднее время, затраченное Александром на инцидент
average_minutes_incident = sum(minutes)/len(minutes)
if average_minutes_incident>59:
    print('Cреднее время, затраченное Александром на каждый инцидент ', average_minutes_incident//60,'ч.', int((average_minutes_incident/60-average_minutes_incident//60)*60), 'мин. '  )
else:
    print('Cреднее время, затраченное Александром на каждый инцидент', int((average_minutes_incident/60-average_minutes_incident//60)*60), 'мин. '  )
    
# 3. Рассчитать максимальное время, потраченное на инцидент и выявить его тип
all_minutes_incident = [minutes[index] for index in range(len(incident_type))]
max_all_minutes_incident = max (all_minutes_incident)
max_minutes_type_incident = incident_type [all_minutes_incident.index(max_all_minutes_incident)]
print('''
Максимальное время, на обработку одного инциндента составило {} минут, данный ициндент соответствует классификационному типу '{}'. 
      '''.format(round(max_all_minutes_incident,2), max_minutes_type_incident)) 
 
# 4. Вывести в консоль, сколько всего ложных срабатываний было среди инцидентов
count_incident =0
for item in range( len(incident_type)):
 	if incident_type[item] == '':
 		count_incident+=1 
print('Среди всех событий, классифицированно ициндентов типа "ложное срабатование" всего:', int(incident_type.count('ложное срабатывание')), 'шт. ')

# 5. Вывести в консоль, сколько всего событий было среди инцидентов
print('Среди всех событий, классифицированно ициндентов типа "событие" всего:', int(incident_type.count('событие')), 'шт. ')

# 6. Вывести в консоль, сколько всего инцидентов было среди инцидентов
print('Среди всех событий, классифицированно ициндентов типа "инциндент" всего:', int(incident_type.count('инцидент')), 'шт. ')


# 7. Объединить 3 списка в новый и вывести в консоль для удобства отображения
summary_incident = sorted(list(zip(incident_type, owner, minutes)))
index = 0 
print('Тотал список тип/фамилия/время:')
while index < len(summary_incident):
    print(*summary_incident[index], sep=', ') 
    index += 1
  
# 8. Рассчитать, сколько времени в сумме диспетчер потратил на события
# ДАННОЕ ЗАДАНИЕ АНАЛОГИЧНО ЗАДАНИЮ 1 (только там требуется в "часах" время перевести)
total_minutes_incident = sum(minutes)
print('Общая сумма времени, которое потребовалось диспетчеру, на работу с инцидентами, составила всего:', int(total_minutes_incident), 'мин.') 

# 9. Вывести последние 10 инцидентов и поместить их в отдельный список
# Учитывая что с оригинальным списком 'incident_type' манипуляции по заданию не проводятся:
last_ten_incident_type=incident_type[-10:]
print('Спмсок 10 последних инцидентов, зафиксированных диспечером:')
print(*last_ten_incident_type, sep=', \n')

# 10. Вывести ответственных за инциденты, на которые было потрачено больше 15 минут
over_minutes_15=[owner[index] for index in range(len(minutes)) if  minutes[index]>15]
print('Список виновников по инциндентам, обработка которых производилась диспечером больше 15 минут:')
print(*over_minutes_15, sep=', ')

# 11.Пришла информация еще о 4-х инцидентах в виде списков. Добавить в соответствующие списки информацию о новых инцидентах
incident_type_new = ['событие', 'событие', 'ложное срабатывание']
owner_new = ['petrov', 'potanina', 'ivanov']
minutes_new= [3, 5, 6]

incident_type.extend(incident_type_new)
print('Актуализированный список зафиксированных типов инциндентов:')
print(*incident_type , sep=',\n')
owner.extend(owner_new)
print('Актуализированный список фамилий виновников инциндентов:')
print(*owner , sep=', ')

minutes.extend(minutes_new)
print('Актуализированный список орезков времени (мин.), затраченных диспетчером на обработку каждого соответствующего инциндента:')
print(*minutes , sep=', ')


