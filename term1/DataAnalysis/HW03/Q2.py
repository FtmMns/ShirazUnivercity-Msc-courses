# q2
def longest_valley(number_list):
    longest = []
    current_valley = []
    n = len(number_list)
    if n < 3:
        return "No valley found"
    for i in range(1, n - 2):
        if number_list[i] < number_list[i + 1] and number_list[i] < number_list[i - 1]:
            left = i - 1
            right = i + 1
            while left > 0 and number_list[left - 1] > number_list[left]:
                left -= 1
            while right < n - 1 and number_list[right + 1] > number_list[right]:
                right += 1
            current_valley = number_list[left:right + 1]
            if len(current_valley) > len(longest):
                longest = current_valley
    return longest if longest else "No valley found"


test_case1 = [9,7,5,3,4,6,8]
test_case2 = [1,2,3,4,5,6]
test_case3 = [10,8,6,5,7,9,3,2,4,6]
print(longest_valley(test_case1))
print(longest_valley(test_case2))
print(longest_valley(test_case3))
