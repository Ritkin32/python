def creating ():
    with open ('Phonebook.csv', 'w', encoding = 'utf-8') as data:
        data.write(f'| Фамилия | Имя | Отчество | Номер телефона | Описание |\n')