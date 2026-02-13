#4. Find sum of first n natural numbers
def SumOfDigits(n):
    if n == 0:
        return 0
    return n+SumOfDigits(n-1)
n = int(input("Enter value for n: "))
print(SumOfDigits(n))
