# q2
def advanced_common_elements(list_a: list, list_b: list):
    min_count = int(input("min_count : "))
    dict1 = list_to_dictionary(list_a, min_count)
    dict2 = list_to_dictionary(list_b, min_count)
    result = []
    for k in dict1:
        l = []
        if k in dict2:
            if dict1[k] > dict2[k]:
                l.append(k)
                l.append(dict1[k])
            else:
                l.append(k)
                l.append(dict2[k])
        result.append(l)

    sorted_list=sorted(result,key=lambda x:x[1],reverse=True)
    return sorted_list


def list_to_dictionary(list_a: list, min_count: int):
    dict = {}
    tuple_a = ()
    for num in list_a:
        if num not in tuple_a:
            tuple_a += (num,)

    for t in tuple_a:
        count = 0
        for j in list_a:
            if t == j and t%2==0:
                count += 1
            if count >= min_count :
                dict[t] = count

    return (dict)


print(advanced_common_elements([1, 1,2, 2, 2, 2, 6, 8, 8, 9], [1, 1,1,1,1,1,1, 2, 2, 2, 8, 8, 8, 5]))
