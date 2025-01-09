def input_name():
    name = input('Ввведите имя: ')
    if name:
        return name
    else:
        print('Нужно указать имя')  
        return exit()
    
def input_surname():
    surname = input('Ввведите фамилию: ')
    if surname:
        return surname
    else:
        print('Нужно указать фамилию')      
        return exit()

def input_phone():
    try: 
        return int(input('Ввведите номер телефона: '))
    except: 
        print('Номер телефона должен состоять из цифр')
        return exit()

def input_address():
    address =  input('Ввведите адрес: ')
    if address:
        return address
    else:
        print('Нужно указать адрес')    
        return exit()
    