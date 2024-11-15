from modules.InputData import InputName, InputSurname, InputPhone, InputAddress
from modules.DatabaseProcessing import SearchDatabase, SelectionDatabase, EditDatabase, ReadingDataFromFile


def DatabaseAppend():
    name = InputName()
    surname = InputSurname()
    phone = InputPhone()
    address = InputAddress()
    base = SelectionDatabase()
    if 'FirstData.csv' in base:
        variant = f'{name}\n{surname}\n{phone}\n{address}\n\n'          
    elif 'SecondData.csv' in base:
        variant = f'{name};{surname};{phone};{address}\n\n'
    with open(file=base, mode='a', encoding='utf-8') as f:
        f.write(variant)
    print('База данных дополнена!')


def DatabaseRead():
    base = SelectionDatabase()
    with open(file=base, mode='r', encoding='utf-8') as f:
        data = f.readlines()
    print('\n',*data)
        

def DatabaseSearch():
    base =  SelectionDatabase()
    _list = ReadingDataFromFile(base)
    SearchDatabase(_list)


def DeleteFromeDatabase():
    base =  SelectionDatabase()
    _list = ReadingDataFromFile(base)
    users = SearchDatabase(_list)
    n = int(input('Выберите номер: '))
    new = []
    for user in _list:
        if users[n-1] not in user:
            new.append(user)
    with open(file=base, mode='w', encoding='utf-8') as f:
        for line in new:
            f.write('{}\n'.format(line))
    print('Запись удалена')


def DatabaseEdit():
    base =  SelectionDatabase()
    _list = ReadingDataFromFile(base)
    users = SearchDatabase(_list)
    n = int(input('Выберите номер: '))
    new = []
    for user in _list:
        if users[n-1] not in user:
            new.append(user)
    if 'FirstData.csv' in base:
        edit = EditDatabase(users[n-1].split())
        variant = f'{edit[0]}\n{edit[1]}\n{edit[2]}\n{edit[3]}\n\n'  
    elif 'SecondData.csv' in base:
        edit = EditDatabase(users[n-1].split(';'))
        variant = f'{edit[0]};{edit[1]};{edit[2]};{edit[3]}\n\n'
    new.append(variant)
    with open(file=base, mode='w', encoding='utf-8') as f:
        for line in new:
            f.write('{}\n'.format(line))
    print('База данных изменена')
    
    
    
