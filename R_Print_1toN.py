#1. Print numbers from 1 to n
def print_1_t0_n(n):
    if n == 0:
        return 
    print_1_t0_n(n-1)
    print(n)
n = int(input("Enter value for n: "))
print_1_t0_n(n)
