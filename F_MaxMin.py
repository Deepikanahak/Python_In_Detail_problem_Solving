#Write a function to find the maximum and minimum values in a list
def Max_Min_InList(l1):
    max = l1[0]
    min = l1[0]
    for i in l1:
        if i>max:
            max = i
        if i<min:
            min = i 
    print("max is:",max,"\nmin is:",min) 
l1 = list(map(int,input("enter the elements for list: ").split()))
Max_Min_InList(l1)
