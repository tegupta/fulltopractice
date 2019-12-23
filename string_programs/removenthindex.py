
def remove(string,index):
    first=string[:index]
    last=string[index+1:]
    return first+last


string=input("Enter string:")
index=int(input("Enter index value:"))
print(remove(string,index))
