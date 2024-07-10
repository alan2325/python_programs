a = int(input("Enter the number: "))
for i in range(1, a + 1):
    for j in range(1, 11):
        b = f"{i} * {j} = {i * j}"
        print(b)