l=[]
llen=input("enter the limit of list")
i=0
while i<llen:
	n=input("")
	l.append(n)
	i=i+1
print l
m=[]
b=[]
f=[]
i=0
j=0
while i<llen:
	v1=l[i]
	j=0
	while j<llen:
		v2=l[j]
		f.append(v1)
		f.append(v2)
		j=j+1
		print f
		m.append(f)
		f=[]
	i=i+1
print m
