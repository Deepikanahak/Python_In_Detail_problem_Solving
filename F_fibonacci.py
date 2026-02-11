#Write a function to generate Fibonacci series up to n terms
def Fibonacci(num):
    if num == 0:
        return "invalid input NO series for 0."
    elif num == 1:
        return 0
    elif num > 1:
        i = 0 # i and j value should be outside of loop if it is in loop it will reset again and again that breaks our fibonacci logic
        j = 1
        print(i,j,end=" ") # it should be i and j as you have assigned 0 and 1 with i and j
        for n in range(num - 2): # as we are already printing 0 and 1 so we need n - 2 terms
            sum = i + j
            i,j =j,sum
            print(sum, end=" ")
num = int(input("Enter value for num to print Fibonacci series up to n terms: "))
Fibonacci(num)