
def get_shop_list_by_dishes(dishes, person_count,cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    # for shop_list_item in shop_list.values():
    #   print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек'))
    dishes = input('Введите блюда в расчете на одного человека через запятую').lower().split(',')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


def main():
    with open('Menu.txt', encoding='utf-8-sig') as f:
        cook_book = {}
        for line in f:
            name_dish = line.strip()
            cook_book[name_dish] = [] #заполняем список ключами
            for _ in range(int(f.readline().strip())):
                ingridient_name, quantity, measure = f.readline().strip().split(' | ')
                cook_book[name_dish].append({
                    'ingridient_name': ingridient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
    create_shop_list(cook_book)

if __name__ == '__main__':
    main()
