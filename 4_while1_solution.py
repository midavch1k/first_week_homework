"""
Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

"""
def hello_user():
    while True:
        question = input ('Как дела? :')
        if question == "хорошо":
            print ('Рад за тебя!')
            break
        else:
            print('Еще разок! ')
"""

def hello_user():
    question = input ('Как дела? :').capitalize()
    while question != "Хорошо":
        print('я не это ждал от тебя')
        question = input ('Как дела? :').capitalize()
    print('Пока!')

             
if __name__ == "__main__":
    hello_user()
