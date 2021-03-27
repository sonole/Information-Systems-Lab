a_list = [10, 12, 14, 14, 16, 28, 28, 30]
#test_list = [15, 4, 7, 3, 2, 6, 10, 15, 10 , 4]

def removeDuplicates(list):
    b_list = []
    for item in list:
        if item not in b_list:
            b_list.append(item)
    return b_list
        
def sortList(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                # Swap
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list

def print_list(list):
    for i in list:
        print(i, end =" ")
    print('')



print_list(removeDuplicates(a_list))

print_list(sortList(removeDuplicates(a_list)))
