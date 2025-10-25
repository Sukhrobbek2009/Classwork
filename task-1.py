balance = 1000
print("Welcome to our ATM!😊")
try:
    answer = input("Would you like to withdraw money : yes/no")
except TypeError:
    print("You should only aswer with yes or no")
if answer == "yes":
    amount = int("How much money would you like to get : ")
    balance = balance - amount
    print(f"Remained balance is {balance}")
elif answer == "no":
    print("Thanks for using our ATM!")

print("Bye")