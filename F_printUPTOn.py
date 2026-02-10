#Write a function to print numbers from 1 to n using a loop
def fun_print(n):
    for i in range(1,n+1):
        print(i, end =" ")
n = int(input("Enter a number upto which you want to print: "))
fun_print(n)
