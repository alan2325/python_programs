print('___Welcome___')
salary = float(input("Enter your net salary : RS "))
years_of_service = int(input("Enter your years of service : "))


if years_of_service >5:
    
    bonus_amount = 0.05 * salary

    print("Congratulations! You are eligible for a bonus.")
    print("Your net bonus amount is : RS ",bonus_amount)
    print("Your total amount is : RS",bonus_amount+salary)

else:

    print("Sorry, you are not eligible for a bonus at this time.")