#8. Find GCD of two numbers
def GCD(a,b):
    if b==0:
        return a 
    return GCD(b,b%a)
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(GCD(a,b))
9. Count digits in a number
10. Find sum of digits of a number