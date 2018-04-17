mat1=[]
mat2=[]
rowsize1=input("enter the row size of matrix")
colsize1=input("enter the coloum size of matrix")
print "enter the elements in the first matrix"
for i in range(0,rowsize1):
    sublist=[]
    for j in range(0,colsize1):
        val=input("enter the element")
        sublist.append(val)
    mat1.append(sublist)
print "the first matrix is"
for i in range (0,rowsize1):
    for j in range(0,colsize1):
        print mat1[i][j],
    print "\n"
rowsize2=input("enter the row size of matrix")
colsize2=input("enter the coloum size of matrix")
print "enter the elements in the first matrix"
for i in range(0,rowsize2):
    sublist=[]
    for j in range(0,colsize2):
        val=input("enter the element")
        sublist.append(val)
    mat2.append(sublist)
print "the first matrix is"
for i in range (0,rowsize2):
    for j in range(0,colsize2):
        print mat2[i][j],
    print "\n"
