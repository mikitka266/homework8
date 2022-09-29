import random

def print_result(list_1):
    with open ('journal.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'Оценки Хакера{list_1}')

def journal_print(list_1):
    list_1 = []
    size=int(input("Введите количество оценок Василия: "))
    for i in range(size):
        i=random.randint(1,5)
        list_1.append(i)
    print(f'Журнал оценок хакера {list_1}')

def journal_sort(list_1):
    max_number=max(list_1)
    print(f'Количество максимальных оценок{list_1.count(max_number)}')
    for i in range (len(list_1)):
        if i == max_number:
            i==1
        print(f'Журнал после изменений хакера {list_1}')
