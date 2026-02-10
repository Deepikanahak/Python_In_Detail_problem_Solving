#Write a function that accepts a list and returns only the even numbers
def even_inList(l1):
    l2 = []
    for ele in l1:
        if  ele % 2 == 0:
            l2.append(ele)
    print("list of even numbers:",l2)
l1 = list(map(int,input("enter elements for list: ").split()))
even_inList(l1)
