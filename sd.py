a=[]
b=[]
na=input("enter the limit of a and values")
i=0
resa=0.0
resb=0.0
resy=0
resx=0
resxy=0
resxx=0
resyy=0
while i<na:
    b=[]
    va=input("enter a")
    vb=input("enter b")
    b.append(va)
    b.append(vb)
    a.append(b)
    i=i+1

for i in range(0,na):
    resy=resy+a[i][1]
    resx=resx+a[i][0]
    resxy=resxy+a[i][1]*a[i][0]
    resxx=resxx+a[i][0]*a[i][0]
    resyy=resyy+a[i][1]*a[i][1]
resa=(float)((resy)*(resxx)-(resx)*(resxy))/((na*resxx)-(resx*resx))
resb=(float)((na*resxy)-(resx)*(resy))/((na*(resxx))-(resx*resx))
print resa
print resb 
#y=reasa+resbx
resa=9.2
resb=0.8
newy=[]
i=0
while i<na:
    b=resa+resb*a[i][0]
    newy.append(b)
    i=i+1
error=[]
errorsqr=[]
i=0
sum=0.0
sqr=0.0
while i<na:
    b=a[i][1]-newy[i]
    error.append(b)
    sqr=(float)(b*b)
    errorsqr.append(sqr)
    sum=(float)(sqr+sum)
    i=i+1
    #print error
print errorsqr
print error
print sum
sum=(float)(sum/na)
print "error",sum
