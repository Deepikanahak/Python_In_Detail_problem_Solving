#Write a function to check whether a string is a palindrome
def palindrome(str):
    rev = ""
    for ch in str:
        rev = ch + rev
    if str == rev:
        return "This string is palindrome"
    return "This string is not palindrom"
str = input("enter a string to check for palindrome: ")
print(palindrome(str))
