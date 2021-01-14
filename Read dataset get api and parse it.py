# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
#
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
#
# Пример входного файла:
# 31
# 999
# 1024
# 502
#
# Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring

import requests

with open("dataset_24476_3.txt", "r") as f:
    for line in f:
        number = int(line)
        url = "http://numbersapi.com/" + str(number) + "/math?json=true"
        res = requests.get(url)
        #  print(res.json())
        if res.json()['found'] is False:
            print("Boring")
        else:
            print("Interesting")

# import requests
#
# api_url = "http://numbersapi.com/"
# params = {
#      'json': 'True'
# }
#
# with open('input.txt') as f:
#     for line in f:
#         number = line.strip()
#         res = requests.get(api_url + number + '/math', params)
#         print('Interesting' if res.json()['found'] == True else 'Boring')