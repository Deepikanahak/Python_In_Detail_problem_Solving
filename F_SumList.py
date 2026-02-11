##Write a function to find the sum of all elements in a list using a loop
def ele_sum_InLIst(l1):
    sum = 0
    for ele in l1:
        sum = sum + ele
    return sum
l1 = list(map(int,input("enter elements for list: ").split()))
result = ele_sum_InLIst(l1)
print("sum of all element in list: ",result)
