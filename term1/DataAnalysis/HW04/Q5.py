#q5
from  typing import List
input_list = input("enter your numbers separated by comma : ")
string_numbers = input_list.split(",")
number_list = []
for i in string_numbers:
    number_list.append(int(i))
def process_numbers(number_list: List[int]):
    unique_list=[]
    result=[]
    for number in number_list:
        if number not in unique_list:
            unique_list.append(number)
    sorted_list=sorted(unique_list, reverse=True)
    for number in sorted_list:
        if number%2==0:
            result.append(number**2)
        else:
            result.append(number*2)

    return result
print(process_numbers(number_list))