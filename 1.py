def find_max(num_list):
    count = 0
    if num_list == []:
        return 0
    for num in num_list:
        count += 1
        if count == 1:
            max_num = num
        else:
            if num > max_num:
                max_num = num
    return max_num 


print(find_max([1,3,1,3,5,55,1111,0,800000,111]))
print(find_max([]))