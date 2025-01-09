from modules.commands_list import commands_list_generation, waiting_input_command
from modules.input_data import input_name, input_surname, input_phone, input_address
import os

def rename(name):
    name = name.replace('\n', ' ')
    name = name.replace(';', ' ')
    return name

def selection_database():
    path = os.path.join(os.getcwd(), 'base/')
    print('---------------------------------\n'
          'В какой базе будем работать?\n'
          '---------------------------------\n') 
    print('1 - в первой:\n'
          '2 - во второй:\n'
          '3 - выход\n'
          '---------------------------------\n')  
    command = waiting_input_command(commands_list_generation(3))
    if command == 1: 
        base = f'{path}FirstData.csv'
    elif command == 2: 
        base = f'{path}SecondData.csv'
    return base


def reading_data_from_file(base):
    users = list()
    with open(file=base, mode='r', encoding='utf=8') as f:
        line = f.readlines()
        start = 0 
        for finish in range(len(line)):
             if line[finish] == '\n':
                users.append(''.join(line[start:finish]))
                start = finish+1  
    return users


def search_database(users):
    print('---------------------------------\n'
          'По каким параметрам будем искать?\n'
          '---------------------------------\n')
    print('1 - по имени и фамилии:\n'
          '2 - по номеру телефона:\n'
          '3 - по ардесу:\n'
          '4 - выход\n'
          '---------------------------------\n') 
    command = waiting_input_command(commands_list_generation(4))
    if command == 1: 
        name = input_name()
        surname = input_surname()
        filter = f'{name} {surname}'
    elif command == 2: 
        filter = str(input_phone())
    elif command == 3: 
        filter = input_address()
    entries = list()
    for user in users:
        if filter.lower() in rename(user).lower():
            entries.append(user)
    if entries:
        if len(entries) > 1:
            print('\n----------------------------------------------\n'
                  '| Найдено несколько записей, соответствующих |\n'
                  '| заданным критериям поиска                  |'
                  '\n----------------------------------------------\n')
        for i in range(len(entries)):
            print(f'{i+1} - {rename(entries[i])}')
        return entries
    else:
        print('\n-----------------------------------------\n'
              '| По вашему запросу, ничего не найдено. |'
              '\n-----------------------------------------\n')
        return 0

    
def edit_database(list):
    print('---------------------------------\n'
          'Какие данные будем редактировать?\n'
          '---------------------------------\n')
    print('1 - имя:\n'
          '2 - фамилию:\n'
          '3 - номер телефона:\n'
          '3 - ардес:\n'
          '4 - выход\n'
          '---------------------------------\n') 
    command = waiting_input_command(commands_list_generation(4))
    if command == 1:
        list[0] = input_name()
    elif command == 2:
        list[1] = input_surname()
    elif command == 3:
        list[2] = input_phone()
    elif command == 4:
        list[3] = input_address()
    return list
