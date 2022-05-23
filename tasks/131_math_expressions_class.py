import math
import random

class Math:
    def __init__(self, args):
        self.result = 0
        self.args = args

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
                self.result = round(result, 2)
        else:
            print("Error.")
            self.result = None
        print(f'Random list: {self.args}.')
        print(f'The result of {action} is: {self.result}.\n')

arguments1 = Math([random.randrange(1, 10) for i in range(0, random.randrange(4, 7))])
arguments1.do("subtraction")

arguments2 = Math([random.randrange(1, 10) for i in range(0, random.randrange(4, 6))])
arguments2.do("division")

arguments3 = Math([random.randrange(1, 10) for i in range(0, random.randrange(4, 6))])
arguments3.do("addition")

arguments4 = Math([random.randrange(1, 10) for i in range(0, random.randrange(4, 6))])
arguments4.do("multiplication")
