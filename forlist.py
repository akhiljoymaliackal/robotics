n1=input("enter the limit of first list")
print "enter the list"
i=0
l1=[]
l2=[]
while i<n1:
	a=input("")
	l1.append(a)
	i=i+1
n2=input("enter the limit of second list")
print "enter the second lis"
i=0
while i<n2:
	a=input("")
	l2.append(a)
	i=i+1
tot=n1+n2
print "l1=   ",l1
print "l2=   ",l2
m=[]
j=0
for i in range(0,tot):
	if i<n1:
		a=l1[i]
		m.append(a)
	else:
		a=l2[j]
		m.append(a)
		j=j+1
print m
