import random

while True:
    rand_num = random.randint(1,100)
    while True:
        try:
            num_in = input("Please guess a number between 1 and 100 : ")
            if num_in.isdigit():
                num_in = int(num_in)
            elif not num_in.isdigit() == True:
                raise Exception("Invalid Input! Try Again!")
            elif num_in < 1 or num_in > 100:
                raise ValueError("Please guess a number within the given range")

            # check answer
            if num_in == rand_num:
                print("You got it")
            elif num_in < rand_num:
                print("It's lower")
            elif num_in > rand_num:
                print("It's higher")
        except Exception as err:
            print("Exception: ", err)
        except ValueError as err:
            print("ValueError: ", err)