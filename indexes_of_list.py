text = "abcdef"
array = [str(i) for i in text]

def get_indexes_of_list():
    for x in range(len(array)):
        array[x] = x
    return array

print(get_indexes_of_list()) # 0,1,2,3,4,5
