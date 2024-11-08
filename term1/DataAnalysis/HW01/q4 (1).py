#q4
def upper_to_lower(string):
    uper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(string)-1):
        if string[i]==" ":
            string=string.replace(" ","")
        for j in range(0,len(uper)-1):
            if string[i]== uper[j] :
                string=string.replace(string[i],lower[j])
    return string
def is_angrams(st1,st2):
    count=0
    for i in str1:
        if i in st2:
            count+=1
    if count==len(st1):
        print("True")
    else:
        print("False")

str1=input("str1: ")
str2=input("str2: ")
str1=upper_to_lower(str1)
str2=upper_to_lower(str2)
is_angrams(str1,str2)