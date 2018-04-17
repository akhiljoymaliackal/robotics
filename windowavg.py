l=[]
wins=input("enter the window size")
lim=input("enter the limit")

i=0
avg=0.0
print "enter teh limit"
while i<lim :
	a=input("")
	l.append(a)
	i=i+1
print " the entered list is \n"
i=0
while i<lim :
	print l[i],"\t",
	i=i+1
i=0
print "\n"
while i<lim :
	j=0
	p=i
	sumw=0.0
	while j<wins :
		if p<lim:
			print l[p],",",
			sumw=sumw+l[p]
		#else :
							
		j=j+1
		p=p+1
	avg=sumw/wins
	print "\tavg =",avg,"\n"
	i=i+1
			
	


