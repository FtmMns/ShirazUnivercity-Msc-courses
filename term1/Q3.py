#q3
def check_password():
    password=input("password = ")
    has_upper=False
    has_lower=False
    has_digit=False
    if len(password)>=8:
        for char in password:
            if char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True
            if char.islower():
                has_lower = True
    if has_lower and has_upper and has_digit :
        return  "Strong"
    else:
        return "Weak"
print(check_password())