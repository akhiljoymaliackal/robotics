mat1=[]
mat2=[]
matres=[]
print "enter the details of first matrix:"
n=input("enter the no of rows :\t")
m=input("enter the no of coloums :\t")
print"enter the elements of first matrix\t\n"
for i in range(0,n):
    l=[]
    for j in range(0,m):
        res=input("")
        l.append(res)
    mat1.append(l)
    print "\n"
print "enter the details of second matrix:"
q=input("enter the no of rows")
r=input("enter the no  of coloums")
print "enter the elements of second matrix"
for i in range (0,q):
    l=[]
    for j in range(0,r):
        res=input("")
        l.append(res)
    mat2.append(l)
    print("\n")
print"************the matrixes are ******************************"
print "matrix 1 "
for i in range (0,n):
    for j in range(0,m):
        print mat1[i][j],"  ",
    print "\n"
print "matrix 2"
for i in range (0,q):
    for j in range(0,m):
        print mat2[i][j],"  ",
    print "\n"
if m==q:
    for i in range (0,n):
        l=[]
        for j in range(0,r):
            ans=0
            for y in range(0,m):
                ans=ans+mat1[i][y]*mat2[y][j]
            l.append(ans)
        matres.append(l)
    print "the resultant matrix is "
    for i in range(0,n):
        for j in range(0,r):
            print matres[i][j],"  ",
        print"\n"
    else:
        print "matrix multiplication not possible"
