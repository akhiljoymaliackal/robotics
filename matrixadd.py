def matprint(l,n,m):
    print "\n"
    for i in range(0,n):
        for j in range(0,m):
            print l[i][j],"\t",
        print "\n"
n=input("enter the no of rows")
m=input("enter the no of coloums")
print"enter the elements of first matrix"
mat1=[]
for i in range(0,n):
    l=[]
    for j in range(0,m):
        ele=input()
        l.append(ele)
    mat1.append(l)
print "enter the elements of matrix 2"
mat2=[]
for i in range (0,n):
    l=[]
    for j in range(0,m):
        ele=input()
        l.append(ele)
    mat2.append(l)
print "the first matrix is"
matprint(mat1,n,m)
print "the second matrix  is"
matprint(mat2,n,m)
matsum=[]
for i in range(0,n):
    l=[]
    for j in range(0,m):
        ele=mat1[i][j]+mat2[i][j]
        l.append(ele)
    matsum.append(l)
print "the sum of the both matrixs are "
matprint(matsum,n,m)
