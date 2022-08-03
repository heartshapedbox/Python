# Write a function which gets main array, length of array, search element and returns index of element. If index of element is not found, return -1.

def array_search(list, length, element):
    for i in range(length):
        if list[i] == element:
            return i
    return -1

# test functions
def test_array_search():
    A1 = [1,2,3,4,5]
    a = array_search(A1, 5, 3)
    if a == -1:
        print("Element is not found.")
    else:
        print("Element is found. The index of the element: " + str(a))
test_array_search()
# Element is found. The index of the element: 2

def test_array_search():
    A2 = [-1,2,7,4,15]
    a = array_search(A2, 5, 10)
    if a == -1:
        print("Element is not found.")
    else:
        print("Element is found. The index of the element: " + str(a))
test_array_search()
# Element is not found.

def test_array_search():
    A3 = [11,2,9,-4,27]
    a = array_search(A3, 5, -4)
    if a == -1:
        print("Element is not found.")
    else:
        print("Element is found. The index of the element: " + str(a))
test_array_search()
# Element is found. The index of the element: 3
