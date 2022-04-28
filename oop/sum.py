class Sum:
    def __init__(self):
        self.result = None

    def sum(self, *args):
            if isinstance(arg1, list):
                self.result = []
            elif isinstance(arg1, int):
                self.result = 0
            else:
                self.result = ""

            for i in args:
                self.result += i
            return self.result
get_sum = Sum()

arg1 = 1
arg2 = 3
arg3 = 3
arg4 = 6
print(get_sum.sum(arg1,arg2,arg3,arg4))

arg1 = "1"
arg2 = "3"
arg3 = "3"
arg4 = "6"
print(get_sum.sum(arg1,arg2,arg3,arg4))

arg1 = [1,3,3]
arg2 = [6,3,8]
arg3 = [6,2,4]
arg4 = [3,4,0]
print(get_sum.sum(arg1,arg2,arg3,arg4))
