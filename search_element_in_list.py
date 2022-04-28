# search an element in the list and return its index. If the element is not presented in the list, return -1.

def search_element_in_list(array, array_length, search_element):
    for x in range(array_length):
        if array[x] == search_element:
            print(array.index(array[x]))
            return
    print(-1)


search_element_in_list([3,2,5,18,22,1,17,9,13,7], 10, 9) # 7
search_element_in_list([3,2,5,18,22,1,17,11,13,7], 10, 9) # -1
