"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
first_string = input ('введите первую строку: ')
second_string = input ('введите вторую строку: ')
#print (second_string.lower())

def main():
        
    if type(first_string) != str or type(second_string) != str:
        return 0
    elif first_string == second_string:
        return 1
    elif len(first_string) > len(second_string):
        return 2
    elif second_string.lower() == 'learn':
        return 3
    else:
        return 'условие неприменимо'
    
    
if __name__ == "__main__":
    print(main())
