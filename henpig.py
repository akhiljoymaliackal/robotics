heads=input("enter the head")
legs=input("enter the legs")
i=True
cond=0
hhead=0
while i==True :
	phead=heads-hhead
#	l=True
#	while l=True :
	hleg=(hhead*2)		
	pleg=(phead*4)
	cond=hleg+pleg
	if cond==legs :
		i=False
		print "fal"
	else :
		hhead=hhead+1
		print "true"
	if phead<=heads and phead >=0 and hhead<=heads and hhead>=0:
		if i==False and (phead+hhead!=heads) :
			i=True
print "no of heans :",hhead,"\nno of pigs :",phead
