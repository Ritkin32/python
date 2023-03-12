def print_data():
    with open ("phones.txt", "w+") as data:
        for i in data:
            print(i)

def add_info():
    with open ("phones.txt", "a") as data:
        surname = input('Укажите фамилию: ')
        name = input('Укажите имя: ')
        patronymic = input('Укажите отчество: ')
        number = input('Введите номер телефона: ')
        for i in number:
            if i not in '1234567890':
                number = input('Номер введен неверно. Повторите ввод: ')
        data.write(f'Surname: {surname}\nName: {name}\nPatronymic: {patronymic}\nPhone_number: {number}\n\n')
        return surname, name, patronymic, number

def ppp_data():
    with open("phones.txt", 'r') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
    return data_first

def put_data():
    phones = ppp_data()
    print("Какую запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal = number_journal - 1
    print(f'Данную запись хотите изменить? (если нет, нажмите Ctrl+C)\n{phones[number_journal]}')
    surname = str(input('Укажите фамилию: '))
    name = str(input('Укажите имя: '))
    patronymic = str(input('Укажите отчество: '))
    number = int(input('Введите номер телефона: '))
    phones = phones[:number_journal] + [f'Surname: {surname}\nName: {name}\nPatronymic: {patronymic}\nPhone_number: {number}\n\n'] + \
                phones[number_journal + 1:]
    with open("phones.txt", 'w', encoding='utf-8') as file:
        file.write(''.join(phones))
    print('Изменения успешно сохранены!')

def delete_data():
    phones = ppp_data()
    print("Какую запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal = number_journal - 1
    print(f'Вот эта запись будет удалена:\n{phones[number_journal]}')
    phones = phones[:number_journal] + phones[number_journal + 1:]
    with open('phones.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(phones))
    print('Изменения успешно сохранены!')

    
def interface():
    print(f'Выберите интересующий пункт меню: \n'
          '1. Показать справочник\n'
          '2. Добавить данные\n'
          '3. Изменить данные\n'
          '4. Удалить данные\n')
    command = int(input('Введите номер операции: '))
    while command < 1 or command > 4:
        print('Вы ошиблись')
        command = int(input('Введите верный номер: '))

    if command == 1:
        print_data()         
    elif command == 2:
        add_info()  
    elif command == 3:
        put_data()
    else:         
        delete_data()

interface()