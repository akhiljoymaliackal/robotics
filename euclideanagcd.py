def swaplar(a,b):
    if a>b:
        return a,b
    else:
        return b,a
def replc(a,b):
    c=a-b
    if a>=c:
        a=c
    elif b>=c:
        b=c
    return a,b

print "*******************euclidean algorith to find gcd of 2 numbers*******************"
a=input("enter the first number\t")
b=input("enter the second number\t")
flag=True
temb=a
while flag:
    a,b=swaplar(a,b)
    if a==b:
        print "gcd = ",a
        flag=False
    elif a-b==1:
        print "gcd = ",1
        flag=False
    else:
        a,b=replc(a,b)
