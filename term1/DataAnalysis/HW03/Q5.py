# q5
def triangle():
    n = int(input("n = "))
    triangle = []
    row = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(j)
        for j in range(i - 1, 0, -1):
            row.append(j)
        triangle.append(row)
    for row in triangle:
        row_string = ""
        for num in row:
            row_string += str(num) + " "
        print(row_string.strip())


(triangle())
