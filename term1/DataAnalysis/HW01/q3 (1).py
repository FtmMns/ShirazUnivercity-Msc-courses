import random
def number_checking(number):
    found_number=False
    count=7
    while count>0:
        user_guess = int(input(f"remain guess {count}, enter your guess : "))
        if user_guess < number:
            count -= 1
            print("number is bigger than {} , remain guess {}".format(user_guess,count))
        elif user_guess > number:
            count -= 1
            print("number is smaller than {} , remain guess {}".format(user_guess,count))
        else:
            print("congratulations!".center(30,"-"))
            found_number=True
            break
    if found_number == False:
        print("sorry,you've lost! The correct number was {}".format(number))
selected_number=random.randint(0,100)
number_checking(selected_number)