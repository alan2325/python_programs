# while True:
#     try :
#         a=int(input("Enter a number : "))
#         print(a)
#         break
#     except :
#         print("Invalid input !")


try:
    print(10+'abc')
except NameError:
    print("Name error !")
except TypeError:
    print("Type error !")
else:
    print("Else")
finally:
    print("finally")