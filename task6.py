costprice=float(input('Enter cost price of the bike : '))
if costprice > 100000:
        tax_percentage = 0.15 * costprice
        print("your tax is : ",tax_percentage)
elif costprice > 50000:
        tax_percentage = 0.10 * costprice
        print("your tax is : ",tax_percentage)
else:
        tax_percentage = 0.05 * costprice
        print("your tax is : ",tax_percentage)