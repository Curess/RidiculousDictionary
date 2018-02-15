import re


dictionary = {}


def add():
    word = input('Enter the expression...').lower()
    meaning = input('Enter the meaning...').lower()
    dictionary[word] = meaning
    print(dictionary)


def all_expressions():
    print(dictionary)


def edit():
    while True:
        a = input('Please, enter the expression you\'d like to edit...').lower()
        if a not in dictionary:
            print('Sorry, there are no such expression yet')
            break
        b = input('Please, enter the new meaning of this expression...').lower()
        dictionary[a] = b
        break


while True:
    action = input('What would you like to do?\n'
                   'Add new expression - enter "add"\n'
                   'Look all the expressions - enter "list"\n'
                   'Edit an expression - enter "edit\n'
                   'Exit this awesome dictionary - enter "exit"'
                   ).lower()
    if action == 'add':
        add()
    elif action == 'list':
        all_expressions()
    elif action == 'edit':
        edit()
    elif action == 'exit':
        break
    else:
        print('Unknown command')

