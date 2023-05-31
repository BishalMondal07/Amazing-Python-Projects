n = int(input("Enter the number :\n"))
digits = []


for digit in str(n):
    digit = int(digit)
    digits.append(digit)
    print(digit, end="\b")


total_digits = len(digits)
power = [digit**total_digits for digit in digits]
sum_of_squares = sum(power)

if sum_of_squares == n:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is the not an armstrong number")