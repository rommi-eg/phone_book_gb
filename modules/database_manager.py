from modules.input_data import input_name, input_surname, input_phone, input_address
from modules.database_processing import search_database, selection_database, edit_database, reading_data_from_file


def database_append():
    name = input_name()
    surname = input_surname()
    phone = input_phone()
    address = input_address()
    base = selection_database()
    if 'FirstData.csv' in base:
        variant = f'{name}\n{surname}\n{phone}\n{address}\n\n'          
    elif 'SecondData.csv' in base:
        variant = f'{name};{surname};{phone};{address}\n\n'
    with open(file=base, mode='a', encoding='utf-8') as f:
        f.write(variant)
    print('База данных дополнена!')


def database_read():
    base = selection_database()
    with open(file=base, mode='r', encoding='utf-8') as f:
        data = f.readlines()
    print('\n',*data)
        

def database_search():
    base =  selection_database()
    _list = reading_data_from_file(base)
    selection_database(_list)


def delete_from_database():
    base =  selection_database()
    _list = reading_data_from_file(base)
    users = search_database(_list)
    n = int(input('Выберите номер: '))
    new = []
    for user in _list:
        if users[n-1] not in user:
            new.append(user)
    with open(file=base, mode='w', encoding='utf-8') as f:
        for line in new:
            f.write('{}\n'.format(line))
    print('Запись удалена')


def database_edit():
    base = search_database()
    _list = reading_data_from_file(base)
    users = search_database(_list)
    n = int(input('Выберите номер: '))
    new = []
    for user in _list:
        if users[n-1] not in user:
            new.append(user)
    if 'FirstData.csv' in base:
        edit = edit_database(users[n-1].split())
        variant = f'{edit[0]}\n{edit[1]}\n{edit[2]}\n{edit[3]}\n\n'  
    elif 'SecondData.csv' in base:
        edit = edit_database(users[n-1].split(';'))
        variant = f'{edit[0]};{edit[1]};{edit[2]};{edit[3]}\n\n'
    new.append(variant)
    with open(file=base, mode='w', encoding='utf-8') as f:
        for line in new:
            f.write('{}\n'.format(line))
    print('База данных изменена')
    
    
    
