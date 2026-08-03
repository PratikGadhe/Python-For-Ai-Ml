# WAF to print the elements of a list in a single line. ( list is the parameter)

list=["pratik","iron man","hulk","spiderman","shaktiman","superman"]

def print_list(list):
    for i in list:
        print(i,end=",")

print_list(list)