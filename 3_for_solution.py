"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phones =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_total(items_scores):
    scores_sum = 0
    for score in items_scores:
        scores_sum += score
    #scores_sum = items_scores
    return scores_sum

for one_phone in phones:
    phone_items_scores = count_total (one_phone['items_sold'])
    print(f"Количество проданных телефонов модели: {one_phone ['product']}: {phone_items_scores}") 
  
if __name__ == "__count_total__":
    count_total()

print ('*' *20) 

def count_avg (items_scores_avg):
    scores_sum = 0
    for score in items_scores_avg:
        scores_sum += score
    items_scores_avg = scores_sum / len (items_scores_avg)
    return items_scores_avg

for one_phone in phones:
    phone_items_score_avg = int(count_avg (one_phone['items_sold']))
    print(f"Среднее количество проданных телефонов: {one_phone ['product']}: {phone_items_score_avg}")   

if __name__ == "__count_avg__":
    count_avg()

print ('*' *20) 

scores_sum = 0

for phone in phones:
    scores_sum += count_total(phone['items_sold'])

all_phones = scores_sum
print(f"Всего продано телефонов: {all_phones}")   

print ('*' *20) 

scores_sum_avg = 0

for phone in phones:
    scores_sum_avg += count_avg(phone['items_sold'])

avg_phones = int(scores_sum_avg / len(phones))
print(f"Всего продано телефонов в среднем за период: {avg_phones}")   

print ('*' *20) 