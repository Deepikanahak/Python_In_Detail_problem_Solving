#9. Count digits in a number
count = 0
def CountDigit(num):
    global count
    if num == 0:
        return 1
    else:
        count += 1
        CountDigit(num//10)
    return count

num = int(input("Enter a num: "))
print(CountDigit(num))
