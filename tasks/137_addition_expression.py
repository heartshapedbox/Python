def sum(*args):
    result = 0
    for i in args:
        result += i
    return result

print(sum(1,3,5,9,10,7))
print(sum(1,7,7,3,10,4,2,10,24))
print(sum(2,3,5,4,16,7))
print(sum(1,22,2.7,2,10,9))
print(sum(28,3,1,2,8,1.5,9,1))
