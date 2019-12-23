def isAnagram(str1,str2):
    return (sorted(str1)==sorted(str2))


str1=input("Enter String1:")
str2=input("Enter String2:")

if isAnagram(str1,str2):
    print("String is anagram")
else:
    print("String not anagram")
