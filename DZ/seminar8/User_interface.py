def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    second_name = input('Введите отчество: ')
    info.append(second_name)
    phone_number = input('Введите номер телефона: ')
    while len(phone_number) < 11:
        phone_number = input('Количествво символов не верное. Повторите ввод: ')
    for i in phone_number:
        if i not in '-()0123456789 ':
            phone_number = input(f'Номер введен не верно (символ ({i})). Повторите ввод: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info