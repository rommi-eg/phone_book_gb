def CommandsListGeneration(count):
    command_list = list()
    for num in range(1, count+1):
        command_list.append(num)
    return command_list

def WaitingInputCommand(list):
    command = 0
    while command not in list:
        try:
            command = int(input('Выберите команду: '))
            if command > len(list):
                print('Вы ввели некорректную команду')
        except:
            print('Вы ввели некорректную команду')
    return command