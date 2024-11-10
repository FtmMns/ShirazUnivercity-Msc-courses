# q4
def multiplication():
    inp_number = int(input("Enter a number between 1 and 10 : "))
    k = 1
    while k < 10:
        print(f'{inp_number}*{k}={inp_number * k}')
        k += 1

    choice = input("Do you want to see another multiplication table ? (yes/no) : ")
    while choice != "no":
        n = int(input("Enter a number between 1 and 10 : "))
        j = 1
        while j < 10:
            print(f'{n}*{j}={n * j}')
            j += 1
        choice = input("Do you want to see another multiplication table ? (yes/no) : ")


multiplication()
