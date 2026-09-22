First_num = int(input("Enter the first number : "))
Second_num = int(input("Enter the second number : "))
Result = First_num * Second_num

if Result > 0 :
        print(f"{First_num} x {Second_num} = {Result}")
        print("The result is positive")
elif Result == 0 :
        print(f"{First_num} x {Second_num} = {Result}")
        print("The result is positive and negative")
else :
        print(f"{First_num} x {Second_num} = {Result}")
        print("The result is negative")