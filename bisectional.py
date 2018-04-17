num=input("enter the number\t:\t")
dif=.00001  
high=num
low=0.00000
mid=(high+low)/2.00000
a=1
c=mid*mid*mid
while abs(num-c)>dif:
	if c>num :
		high=mid
		mid=(high+low)/2.00000
	elif c<num :
		low=mid
		mid=(high+low)/2.00000
	c=mid*mid*mid
print "\nthe cube root is \t:\t",mid

	
