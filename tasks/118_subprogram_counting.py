# Определите подпрограмму, которая предлагает пользователю ввести число и сохраняет его в переменной num.
# Определите другую подпрограмму, которая использует
# значение num и проводит отсчет от 1 до этого числа.

def get_num():
    num = int(input('Please, enter a number: '))
    return num

def count(num):
    for i in range(1, num):
        print(i)

def main():
    num = get_num()
    count(num)

main()
