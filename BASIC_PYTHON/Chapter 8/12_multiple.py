class A:
    var1=print("Welcome A")
class B :
    var2=print("Welcome B")
class C(A,B):
    var3=print("Welcome C")

abc=C()
(abc.var1)
(abc.var2)
(abc.var3)