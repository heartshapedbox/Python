# Write function which returns multi-dim list. The function gets 2 parameters: main list and sub lists length.

def get_multi_dim_list(main_list, sub_list_length):
    multi_list = [0 for i in range(len(main_list))]
    launch = 0

    for x in range(len(main_list)):
        if launch < len(main_list):
            slice_obj = slice(launch, launch + sub_list_length)
            multi_list[x] = main_list[slice_obj]
            launch = launch + sub_list_length

    while multi_list[-1] == 0:
        multi_list.pop()
    print(multi_list)

get_multi_dim_list([1,3,5,10,11,13,7], 2)
# [[1, 3], [5, 10], [11, 13], [7]]

get_multi_dim_list([1,3,5,10,11,13,7], 3)
# [[1, 3, 5], [10, 11, 13], [7]]
