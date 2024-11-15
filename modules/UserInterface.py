from modules.CommandsList import CommandsListGeneration, WaitingInputCommand
from modules.DatabaseManager import DatabaseAppend, DatabaseRead, DatabaseSearch, DeleteFromeDatabase, DatabaseEdit

def WelcomePhoneBook():
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
    
    command = WaitingInputCommand(CommandsListGeneration(count=6))

    if command == 1:
        DatabaseAppend()
    elif command == 2:
        DatabaseRead()
    elif command == 3:
        DatabaseSearch()
    elif command == 4:
        DatabaseEdit()
    elif command == 5:
        DeleteFromeDatabase()