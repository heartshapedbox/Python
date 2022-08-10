# Напишите программу, которая выводит следующее меню:
# 1) Make a code
# 2) Decode a message
# 3) Quit
# Enter your selection: Если пользователь выбирает вариант 1, он получает возможность ввести сообщение, а затем число. Python выводит закодированное сообщение, полученное с применением заданного сдвига. Если пользователь выбирает вариант 2, он вводит закодированное сообщение и правильное число, а программа выводит декодированное сообщение (то есть смещается на нужное количество букв в обратном направлении по алфавиту). При выборе варианта 3 программа завершает работу. После того как пользователь закодирует или декодирует сообщение, меню выводится снова, пока пользователь не завершит работу с программой.


class App():
    def __init__(self):
        self.ch_list = ['a','Z','b','Y','c','X','d','W','e','V','f','U','g','T','h','S','i','R','j','Q','k','P','l','O','m','N','n','M','o','L','p','K','q','J','r','I','s','H','t','G','u','F','v','E','w','D','x','C','y','B','z','A',',','.','?','!',':',';','-','―','_','"','(',')',' ']
        self.encoded_str = ''
        self.decoded_str = ''  
        
    def show_menu(self):
        self.menu_option = 0
        while self.menu_option != 3:
            print('Menu:\n[+] 1. Encode\n[+] 2. Decode\n[+] 3. Quit')
            self.menu_option = int(input('Choose menu option: '))
            if self.menu_option == 1:
                self.input_str = input('Enter some text: ')
                self.shift = int(input('Enter a shift nubmer: '))
                self.encode()
            elif self.menu_option == 2:
                self.input_str = input('Enter some text: ')
                self.shift = int(input('Enter a shift nubmer: '))
                self.decode()
            elif self.menu_option == 3:
                quit()
            else:
                print('Error!')
    
    
    def encode(self):
        self.encoded_str = ''
        self.ch_list_len = len(self.ch_list)
        for i in self.input_str:
            self.finish = False
            while self.finish == False:
                self.ch_index = self.ch_list.index(i)
                if self.ch_index + self.shift >= self.ch_list_len:
                    self.len_diff = self.ch_list_len - self.ch_index
                    self.new_list = [*self.ch_list[self.ch_index:self.ch_list_len],*self.ch_list[0:self.shift - self.len_diff + 1]]
                    if i in self.new_list:
                        self.ch_index = 0
                        self.encoded_str = f'{self.encoded_str}{self.new_list[self.ch_index + self.shift]}'
                else:
                    if i in self.ch_list:
                        self.encoded_str = f'{self.encoded_str}{self.ch_list[self.ch_index + self.shift]}'
                self.finish = True
        print(self.encoded_str)
    
    
    def decode(self):
        self.decoded_str = ''
        self.ch_list_len = len(self.ch_list)
        for i in self.input_str:
            self.finish = False
            while self.finish == False:
                self.ch_index = self.ch_list.index(i)
                if self.ch_index - self.shift <= 0:
                    self.len_diff =  self.shift - self.ch_index
                    self.new_list = [*self.ch_list[self.ch_list_len - self.len_diff:self.ch_list_len],*self.ch_list[0:self.ch_index + 1]]
                    if i in self.new_list:
                        self.ch_index = len(self.new_list)
                        self.decoded_str = f'{self.decoded_str}{self.new_list[self.ch_index - self.shift - 1]}'
                else:
                    if i in self.ch_list:
                        self.decoded_str = f'{self.decoded_str}{self.ch_list[self.ch_index - self.shift]}'
                self.finish = True
        print(self.decoded_str)


if __name__ == '__main__':
    App().show_menu()