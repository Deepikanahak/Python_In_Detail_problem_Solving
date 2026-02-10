#Write a function to calculate the factorial of a number using a loop
def factorial(num):
    if num == 0 or num == 1:
        priint("factorial is 1")
    else:
        for i in range(1,num+1):
            global fact
            fact = fact*i
        print("factorial of number is: ",fact )
num = int(input("Enter a number of which you want to calculate factorial: "))
fact = 1
factorial(num)