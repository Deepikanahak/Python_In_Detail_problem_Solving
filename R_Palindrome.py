#7. Check palindrome using recursion
def palindrome(str,left,right):
    if len(str)>=right:
        return True
    if str[left]!=str[right]:
        return False
    return palindrome(str,left+1,right-1)
str = input("Enter a string to check palindrome: ")
left = 0
right = len(str)
print(palindrome(str,left,right))
