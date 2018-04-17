head=input("enter the no of heads")
leg=input("enter the no of legs")
hhead=0
hcond=True
i=True
while i==True:
	hleg=(hhead*2)
	phead=0
	hcond=True
	while hcond==True :
		pleg=(phead*2)
		if hcond<=head:
			hcond=False
		if pleg+hleg==leg and hhead+phead==head :
			i=False
			hcond=False
			print hhead,"\n",phead
		else:
			phead=phead +1
		
	hhead=head+1
