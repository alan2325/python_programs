print('___Welcome___')
year = int(input("How many years service do you have ? : "))

if year >5:
    salary = float(input("Enter your net salary : RS "))
    
    bonus_amount = 0.05 * salary

    print("Congratulations! You are eligible for a bonus.")
    print("Your net bonus amount is : RS ",bonus_amount)
    print("Your total amount is : RS ",bonus_amount+salary)

else:

    print("Sorry, you are not eligible for a bonus at this time.")