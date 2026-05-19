
#strings (strings are immutable)
#operations perform on string
#1.CONCATENATION
str1="Pratik "
str2="Gadhe"
final=str1+str2
print("Your Name is",final)

n1='1'
n2='1'
print(n1+n2)

#2.LENGTH OF STRING len()
print(len(final))
n3=12
print(len(str(n3)))

#3.Indexing
name="Pratik"
ch=name[1]
print("Chracter :",ch) #r

#slicing
name1="Pratik Vilas Gadhe"
print(name1[0:6])
print(name[:6])
print(name1[0:])
print(name1[0:len(name1)])
print(name1[13:])
print(name1[0:20])#ending index is out of range but still working

#negative indexing 

a="apple"
print(a[-3:-1]) #2:4 -> 5-3=2 : 5-1=4
print(a[6:-1])