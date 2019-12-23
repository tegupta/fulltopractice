def first_last_swap(str):
    str=list(str)
    if (len(str)>1):
        first=[str[0]]
        last=[str[-1]]
        middle=str[1:-2]
        return ''.join(last+middle+first)
    else:
        return str

str="Hello world"
print(first_last_swap(str))