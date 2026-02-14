#10. Find sum of digits of a number
def SumDigits(num):
    if num == 0:
        return 0
    else:
        return (num%10)+SumDigits(num//10)
num = int(input("Enter a vallue for num: "))
print(SumDigits(num))