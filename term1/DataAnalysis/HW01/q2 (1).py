s1=input("str1 : ")
s2=input("str2 : ")
def match(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    count=0
    for i in range(0,len(str1)):
        if  str1[i]==str2[i] and str1[i] !=" " and str2[i] !=" ":
            count+=1
    print(count)
if len(s1) == len(s2):
    match(s1,s2)
else:
    print("strings must be equal lenght")

