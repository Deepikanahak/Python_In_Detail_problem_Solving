#Write a function to take a number as input and check whether it is even or odd
def Check_even_odd(n):
    if n%2 == 0:
        return "True"
    else:
        return "False"
n = int(input("enetr a number: "))
print(Check_even_odd(n))