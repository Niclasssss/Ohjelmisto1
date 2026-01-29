def sum_of_list(number_list):
    result = 0
    for luku in number_list:
        result += luku
    return result

number_list = [1, 2, 3, 4, 5]
result = sum_of_list(number_list)
print(f"The sum of the numbers in the list is: {result}")