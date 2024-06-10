unit=float(input("Enter the unit of electricity used : "))
if unit<=100:
  print("no charges")
elif unit<=200:  
  charge=(unit-100)*5
  print("charge is : ",charge)  

else:
  charge=(unit-200)*10+500
  print("charge is : ",charge)