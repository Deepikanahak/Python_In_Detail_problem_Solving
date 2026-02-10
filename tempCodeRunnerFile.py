def multiplication(n):
    product = 1
    print("multiplication table is:")
    for i in range(1,11):
        print(n, "X", i, "=", n*i)
num = int(input("Enter a number of which you want to print a table: "))
multiplication(num)