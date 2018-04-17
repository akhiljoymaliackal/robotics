a=[]
i=0
lim=input("enter the limit of lit")
print "enter the list"
while i<lim:
	b=input("")
	a.append(b)
	i=i+1
def quicksrt(first,last):
	i=first
	j=last-1
	p=a[first]
	if first<last:
		while i<j:
			while a[i]<=p and i<last:
				i=i+1
			while a[j]>=p and j>first:
				j=j-1
			if(i<j):
				temp=a[i]
				a[i]=a[j]
				a[j]=temp
		temp=a[j]
		a[j]=a[first]
		a[first]=temp
		quicksrt(first,j-1)
		quicksrt(j+1,last)
quicksrt(0,lim)
print a

			
	
