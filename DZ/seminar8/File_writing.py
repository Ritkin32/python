from User_interface import get_info as gi

def writing_scv_txt():
    info = gi()
    with open ('Phonebook.csv', 'a', encoding = 'utf-8') as data:
        data.write(f'| {info[0]} | {info[1]} | {info[2]} | {info[3]} | {info[4]} |\n')
    with open ('Phonebook.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nОтчество: {info[2]}\nНомер телефона: {info[3]}\nОписание: {info[4]}\n\n')