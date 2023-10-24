all_products = {'Весь склад': {}}

while True:
    admin = input('Что вы хотите сделать?(1.Добавить 2.Все продукты 3.Удалить 4.Выход): ')

    if admin == '4':
        break
    elif admin == '1':
        product_name = input('Введите названия продукта: ')
        product_count = input('Введите количество: ')
        all_products['Весь склад'][product_name] = int(product_count)
        print(f'Продукт "{product_name}" добавлен в список')
    elif admin == '2':
        print('Список продуктов и их кол-во')
        for product, count in all_products['Весь склад'].items():
            print(f'{product}: {count}')
    elif admin == '3':
        deleted = input('Выберите название продукта, который хотите удалить, или хотите удалить ВСЕ: ')
        if deleted == 'ВСЕ':
            all_products['Весь склад'].clear()
            print('Все продукты удалены')
        elif deleted in all_products['Весь склад']:
            removed_count = all_products['Весь склад'].pop(deleted)
            print(f'Продукт "{deleted}" удален из списка. Было {removed_count} штук.')
        else:
            print(f'Продукт {deleted} не найден')
    else:
        print('Неверная команда')
print('Программа завершена')
