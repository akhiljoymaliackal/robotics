def inp(a):
	i=0
	l=[]
	while i<a:
		n=input("")
		l.append(n)
		i=i+1
	return l
l=[]
len1=input("enter the length of first list")
l=inp(len1)
print l
subl=[]
lens=input("enter the length of sub list")
subl=inp(lens)
print subl
i=0
p=0
flag=False
while i<len1:
	if l[i]==subl[p]:
		c=i
		j=0
		print c
		while j<len(subl):
			if l[c]==subl[j]:
				flag=True
				
			else :
				flag=False
				break
			c=c+1			
			j=j+1
		i=i+1
	else:
		i=i+1
if flag==True:
	print "found"
else :
	print "not found"
				

