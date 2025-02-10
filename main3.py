def count_digits(user_input):
    return sum(c.isdigit() for c in user_input)

user_input = input("Enter a string: ")
digit_count = count_digits(user_input)
print(f"The number of digits entered is: {digit_count}")

