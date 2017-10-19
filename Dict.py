# -*- coding: utf8 -*-
from pprint import pprint


def main():
    with open('E:/Python/Задание_2.1/Menu.txt', encoding='utf-8-sig') as f:
        cook_book = {}
        for line in f:
            name_dish = line.strip()
            cook_book[name_dish] = [] #заполняем список ключами
            for _ in range(int(f.readline().strip())):
                ingridient_name, quantity, measure = f.readline().strip().split(' | ')
                cook_book[name_dish].append({
                    'ingridient_name': ingridient_name,
                    'quantity': quantity,
                    'measure': measure
                })
    print('cook_book = ')
    pprint(cook_book)

if __name__ == '__main__':
    main()
