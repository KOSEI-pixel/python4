def decimal_to_binary(n):
    if n >= 1:
        decimal_to_binary(n // 2)
    print(n % 2, end='')

# Input from the user
decimal_number = int(input("Enter a decimal number: "))
if decimal_number == 0:
    print("Binary representation of", decimal_number, "is: 0")
else:
    print("Binary representation of", decimal_number, "is: ", end='')
    decimal_to_binary(decimal_number)