#q1
def is_palindrom(inp_list):
    found_palindrom=False
    for word in inp_list:
        j = len(word) - 1
        count=0
        if len(word)%2==0:
            for k in range(0,len(word)//2):
                if word[k]==word[j]:
                    count+=1
                    j-=1
            if count == len(word) // 2:
                 print(word,end=",")
                 found_palindrom=True
    if found_palindrom is False:
            print("No even_lenght palindromes found")
str_vorodi=input("word list : ")
input_list=[]
input_list=str_vorodi.split(",")
is_palindrom(input_list)

