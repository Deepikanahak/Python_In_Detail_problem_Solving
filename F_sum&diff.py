#Write a function that takes two numbers as input and returns their sum and difference
def sum_diff(n1,n2):
    return n1+n2,n1-n2
n1 = int(input("enter a number: "))
n2 = int(input("enter a number: "))
print(sum_diff(n1,n2))
