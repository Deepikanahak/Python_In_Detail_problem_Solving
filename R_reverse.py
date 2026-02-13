#6. Reverse a string using recursion
def reverse(str):
    if len(str)<=1:
        return str
    return reverse(str[1:]) + str[0]
str = input("Enter a string: ")
print(reverse(str))

