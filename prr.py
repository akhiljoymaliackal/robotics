heads=input("enter the no of heads")
leags=input("enter the no of legs")
hen=0
while hen<=heads:
	pig=heads-hen
	tleg=(2*hen)+(4*pig)
	if tleg==leags:
		print "no of hen = ",hen,"\n","no of pig =",pig
		break
	else :
		hen=hen+1
else:
	print "err"
