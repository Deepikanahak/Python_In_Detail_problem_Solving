#5. Find power (a^b)
def power(n,p):
    if p == 0:
        return 1
    return n*n**(p-1)
n = int(input("Enter value for base: "))
p = int(input("Enter value for power: "))
print(power(n,p))