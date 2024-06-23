# Define the list
numbers = [5, 3, 8, 6, 2, 9, 1]

# Print the list
print("List of numbers:", numbers)

# Find the largest number using a swapping method
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            # Swap numbers[i] and numbers[j]
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

# The largest number is now the first element
largest_number = numbers[0]
print("Largest number in the list:", largest_number)