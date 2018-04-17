def inp(a):
	l=[]
	i=0
	while i<a:
		b=input("")
		l.append(b)
		i=i+1
	return l	 
l1=[]
l2=[]
len1=input("enter the limit of first list")
print("enter the first list")
l1=inp(len1)
print l1
len2=input("enter the limit of scond list")
print("enter the second list")
l2=inp(len2)
print l2
m=[]
totlen=len(l1)+len(l2)
print totlen
i=0
b=0
d=0
while i<totlen:
	if i<len(l1):
		c=l1[b]
		m.append(c)
		b=b+1
	else:
		c=l2[d]
		m.append(c)
		d=d+1
	

	i=i+1
print m 

