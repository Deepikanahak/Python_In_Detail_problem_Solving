def CheckPrime(num):
    if num<= 1:
        return "Not a Prime Number"
    for i in range(2,(num//2)+1):
        if num%i == 0:
            return "It is not a Prime Number"
    else:
        return "it is a prime"
num = int(input("Enter a number: "))
print(CheckPrime(num))