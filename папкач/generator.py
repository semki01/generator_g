with open('Untitled-1.txt', 'r', encoding = 'utf-8') as file:
    data = file.read()
    print(data)

while input('Хотите добавить цитату?') != "нет":

quote = input('Хотите какать?')
author = input('Введите автора цитаты:')
with open('Untitled-1.txt', 'a', encoding = 'utf-8') as file:
    file.whrite('\n(' + author + ')\n')

with open('Untitled-1.txt', 'r', encoding = 'utf-8') as file:
    data = file.read()
    print(data)