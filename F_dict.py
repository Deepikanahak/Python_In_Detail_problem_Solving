#Write a function that accepts a dictionary and prints all keys and values
def Print_dict(data,n):
    for i in range(n):
        key = input("enetr key: ")
        values =input("enter values: ")
        data[key]= values
    print("Now finl dictionary is:\n ",data)
n = int(input ("Enter how many pairs of data you want from user: "))
data = {}
print(Print_dict(data,n))