import random

class Math:
    def __init__(self, args):
        self.result = 0
        self.args = args
        print(f'Random list: {self.args}\n')

    def do(self, action):
        if action == "addition":
            for i in range(0, len(self.args)):
                self.result += self.args[i]
        elif action == "multiplication":
            self.result = 1
            for i in range(0, len(self.args)):
                self.result *= self.args[i]
        elif action == "subtraction":
            self.result = self.args[0]
            for i in range(1, len(self.args)):
                self.result -= self.args[i]
        elif action == "division":
            result = self.args[0]
            for i in range(1, len(self.args)):
                result /= self.args[i]
                self.result = round(result, 4)
        else:
            print("Error!")
            self.result = None

        print(f'The result of {action} is: {self.result}')
        self.result = 0

list = Math([random.randrange(1, 20) for i in range(0, random.randrange(4, 7))])
list.do("subtraction")
list.do("division")
list.do("addition")
list.do("multiplication")
