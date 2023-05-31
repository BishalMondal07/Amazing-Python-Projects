Operation = input("Enter Operation : ")
if (Operation == "LCM" or "lcm") :
    a = int(input("Enter thr number : "))
    b = int(input("Enter the number : "))
    max = max(a, b)

    while True:
        if max % a == 0 and max % b == 0:
            lcm = max
            break
        max += 1

    print(f"The LCM of  {a} and {b} is {lcm}.")
elif (Operation == "HCF" or "hcf") :
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))

    min = min(a, b)
    for i in range(1, min + 1):
        if (a % i == 0 and b % i == 0):
            HCF = i

    print(f"The HCF or GCD of {a} and {b} is {HCF}")