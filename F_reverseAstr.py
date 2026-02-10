#Write a function to count the number of vowels in a given string
def count_vowel(str):
    count = 0
    for ch in str:
        if ch in "AEIOUaeiou":
            count += 1
    return count
str = input("Enter a string: ")
result = count_vowel(str)
print("Hence total number of vowels are: ",result)