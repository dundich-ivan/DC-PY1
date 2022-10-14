list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

for i in range(len(list_numbers)):
    if list_numbers[i] == max(list_numbers):
        index_max = i

last_index = -1
list_numbers[index_max], list_numbers[last_index] = list_numbers[last_index], max(list_numbers)


print(list_numbers)


