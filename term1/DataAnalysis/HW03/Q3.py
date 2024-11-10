def sum_of_products(touple_list):
    sumation = 0
    for touple in touple_list:
        x, y, z = touple
        if x % 3 == 0 and y % 5 != 0:
            sumation += x * y * z
    return sumation


# test_case1=[(3,4,5),(9,10,2),(6,7,8),(12,15,3),(15,6,3)]
# print(sum_of_products(test_case1))

def category(category_list):
    result = []
    for x, y in category_list:
        result += [x, sum_of_products(y)]
    return result


test_case = [("Set 1", [(2, 3, 5), (8, 2, 6), (4, 3, 5)]),
             ("Set 2", [(6, 2, 12), (5, 5, 5), (3, 6, 9)]),
             ("Set 3", [(2, 4, 8), (4, 8, 16), (3, 3, 3)])
             ]
print(category(test_case))
