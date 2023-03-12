from os.path import exists
from CSV_creating import creating
from interfase import show_main_menu


valid = exists('Phonebook.csv')
if not valid:
    creating()

show_main_menu()