from utils import *

#Сначала определяем последние 5 дат
operations = "operations.json"
dict_of_dates = make_dict_of_dates(operations)
the_last_5 = nlargest(5, dict_to_list(dict_of_dates))


#Переводим числа обратно в даты, чтобы потом
#можно было искать операции по датам.
#Важно сохранить последовательность
for key, value in dict_of_dates.items():
    if value in the_last_5:
        index = the_last_5.index(value)
        the_last_5.remove(value)
        the_last_5.insert(index, key)


#Находим нужные операции по датам
for item in the_last_5:
    operation = find_operation(item, operations)
    index = the_last_5.index(item)
    the_last_5.remove(item)
    the_last_5.insert(index, operation)


#Отображаем операции
for operation in the_last_5:
    print(display_operation(operation))

