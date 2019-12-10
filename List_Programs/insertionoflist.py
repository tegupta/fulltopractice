# def intersection(list1,list2):
#     list3=[value for value in list1 if value in list2]
#     return list3

def intersection(list1,list2):
    return list(set(list1) & set(list2))

list1=[1,2,78,3,28,57,33,90,30,29,44]
list2=[44,57,99,3,1,77,45,60]
print(intersection(list1,list2))