my_string = "22!%34!!@44!572!!(667!__!99{{}{"

#1.надо вывести на экран все "!" восклицательные знаки
new_string = ""
for i in range(len(my_string)):
    if my_string[i] == "!":
        new_string += "!"
print(new_string)
print('-----------------------------------------------')

##############################################################################

#2.надо получить самую большую и самую маленькую цифру
string_without_symbols = [i for i in my_string if i.isdigit()]
max_number = max(string_without_symbols)
min_number = min(string_without_symbols)
print("Наибольшее число:", max_number, "\nНаименьшее число:", min_number)
print('-----------------------------------------------')

##############################################################################

#3.вывести все элементы между первыми двумя восклицательными знаками
part_of_string = ""
for i in range(len(my_string)):
    if my_string[i] == "!":
        while my_string[i + 1] != "!":
            part_of_string += my_string[i + 1]
            i += 1
        break
print(part_of_string)
print('-----------------------------------------------')

##############################################################################

#4.вывести на экран только цифры, поочередно и одной строкой
string_without_symbols = [i for i in my_string if i.isdigit()]
print(",".join(string_without_symbols))
print('-----------------------------------------------')

##############################################################################

#5.вывести на экран только чётные цифры
string_without_symbols = [i for i in my_string if i.isdigit()]
string_with_even_numbers = ""
for i in range(len(string_without_symbols)):
    if int(string_without_symbols[i]) % 2 == 0:
        string_with_even_numbers += str(string_without_symbols[i])
print("Чётные цифры:", string_with_even_numbers)
print('-----------------------------------------------')

##############################################################################

#6.вывести на экран элементы которые находятся между восклицательных знаков
my_string = "22!%34!!@44!572!!(667!__!99{{}{"
another_string = my_string[3:6] + ',' + my_string[8:11] + ',' + my_string[12:15] + ',' + my_string[17:21] + ',' + my_string[22:24]
print('Элементы которые находятся между восклицательных знаков:', another_string)
print('-----------------------------------------------')

##############################################################################

#7.Найти сумму всех чисел
string_without_symbols = [i for i in my_string if i.isdigit()]
summ_numbers = 0
for i in range(len(string_without_symbols)):
    summ_numbers += int(string_without_symbols[i])
print('Сумма всех чисел:', summ_numbers)
print('-----------------------------------------------')

##############################################################################

#8.найти все попарно одинаковые элементы строки, например:22
same_numbers = ""
for i in range(len(my_string) - 1):
    if my_string[i] == my_string[i + 1]:
        same_numbers += my_string[i] + my_string[i]
print('Попарно одинаковые элементы строки:', same_numbers)
print('-----------------------------------------------')

##############################################################################

#9.Убрать из этой строки восклицательные знаки
delete = '!'
clean_string = ''.join([i for i in my_string if i not in delete])
print('Строка без восклицательных знаков:', clean_string)

