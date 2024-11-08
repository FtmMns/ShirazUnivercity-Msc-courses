#q4
from typing import List

input_list = input("enter your numbers separated by spaces : ")
string_numbers = input_list.split(" ")
number_list = []
for i in string_numbers:
    number_list.append(int(i))

def f(number: int):
    if number <= 1:
        return 1
    else:
        return number * f(number - 1)


def factorial(number_list: List[int]):
    result = []

    dict = {}
    for number in number_list:
        if number not in dict:
            dict[number] = f(number)
            result.append(dict[number])
        else:
            result.append(dict[number])
    return result


print(factorial(number_list))
