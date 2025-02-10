def power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent number: "))
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")