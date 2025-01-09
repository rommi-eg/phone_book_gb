from modules.commands_list import commands_list_generation, waiting_input_command
from modules.database_manager import database_append, database_read, database_search, delete_from_database, database_edit

def welcome_phone_book():
    print('\nДобро пожаловать! в телефонный справочник.\n'
          '     --------------------------------\n'
          '     | Выберете команду:            |\n'
          '     |   1 - для записи данных      |\n'
          '     |   2 - для вывода данных      |\n'
          '     |   3 - для поиска данных      |\n'
          '     |   4 - для изменения двнных   |\n'
          '     |   5 - для удаления данных    |\n'
          '     |   6 - выход                  |\n'
          '     --------------------------------\n')
    
    command = waiting_input_command(commands_list_generation(count=6))

    if command == 1:
        database_append()
    elif command == 2:
        database_read()
    elif command == 3:
        database_search()
    elif command == 4:
        database_edit()
    elif command == 5:
        delete_from_database()