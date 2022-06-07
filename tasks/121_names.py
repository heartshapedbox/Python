# Напишите программу, которая помогает пользователю легко управлять списком имен. Программа
# должна выводить меню, дающее возможность добавлять, изменять и удалять имена из списка,
# а также отображать их все. Кроме того, в меню должна присутствовать команда для завершения
# работы программы. Если пользователь выбрал несуществующую команду, программа выводит соответствующее сообщение. После того как пользователь выбрал команду добавления, изменения или
# удаления имени или просмотра всех имен, меню должно выводиться снова без необходимости перезапуска программы. Программа должна быть по возможности простой и удобной в использовании.

names_list = ['Anna','Peter','Jason','Olivia','Joel','Noah','Ellie','David','Sofia']

class Names:
    def __init__(self, names):
        self.names = names;

    def do(self, option):
        try:
            option = int(option)
            if option == 1:
                print('\nOutput:')
                print(', '.join(self.names))
            elif option == 2:
                name = input('Please, enter a new name: ').title()
                self.names.append(name)
                print('\nOutput:')
                print(', '.join(self.names))
            elif option == 3:
                print(', '.join(self.names))
                condition = False
                while condition == False:
                    focused_name = input('Please, enter a name you would like to replace: ').title()
                    if focused_name in self.names:
                        name = input('Please, enter a new name: ').title()
                        self.names[self.names.index(focused_name)] = name
                        print('\nOutput:')
                        print(', '.join(self.names))
                        condition = True
                    else:
                        print('Incorrect name. Try again!')
                        condition = False
            elif option == 4:
                print(', '.join(self.names))
                condition = False
                while condition == False:
                    focused_name = input('Please, enter a name you would like to remove: ').title()
                    if focused_name in self.names:
                        self.names.remove(focused_name)
                        print('\nOutput:')
                        print(', '.join(self.names))
                        condition = True
                    else:
                        print('Incorrect name. Try again!')
                        condition = False
            elif option == 5:
                print('Program closed.')
                quit()
            else:
                print('Error!')
                quit()
        except ValueError:
            print('Error!')
            quit()

def show_menu():
    print('\nMenu:\n--------------------\n1. Show all names\n2. Add new name\n3. Replace name\n4. Remove name\n5. Quit\n--------------------\n')

def main():
    condition = True
    while condition == True:
        show_menu()
        option = input('Please, choose an option: ')
        list = Names(names_list)
        list.do(option)
main()
