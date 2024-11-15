def InputName():
    name = input('Ввведите имя: ')
    if name:
        return name
    else:
        print('Нужно указать имя')  
        return exit()
    
def InputSurname():
    surname = input('Ввведите фамилию: ')
    if surname:
        return surname
    else:
        print('Нужно указать фамилию')      
        return exit()

def InputPhone():
    try: 
        return int(input('Ввведите номер телефона: '))
    except: 
        print('Номер телефона должен состоять из цифр')
        return exit()

def InputAddress():
    address =  input('Ввведите адрес: ')
    if address:
        return address
    else:
        print('Нужно указать адрес')    
        return exit()
    