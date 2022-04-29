# Write a function which inverts a list. The function gets main list and its length and returns: boolean True of False and inverted list.

def invert_list(list, length):
    invert_list = [0 for i in list]
    launch = 0

    for i in range(length):
        invert_list[i] = list[-1 + launch]
        launch = launch + -1
    return invert_list

#test functions
def test_invert_list():
    A1 = [1,2,3,4,5]
    a = invert_list(A1, 5)
    if a == [5,4,3,2,1]:
        print("True")
        print(a)
    else:
        print("False")
test_invert_list()
# True
# [5, 4, 3, 2, 1]


def test_invert_list():
    A2 = [0,0,5,0,0,0,0,10,0,10]
    a = invert_list(A2, 10)
    if a == [10,0,10,0,0,0,0,5,0,0]:
        print("True")
        print(a)
    else:
        print("False")
test_invert_list()
# True
# [10, 0, 10, 0, 0, 0, 0, 5, 0, 0]
