items=["apple","orange","mango","pineapple","grape"]
value=[40,30,20,15,5]
weight=[10,15,5,12,2]
m=[]
max_weight=20
max_value=0
j=1
w=0
i=0
while i<len(items):
	if weight[i]+w>max_weight:
		i=i+1
	else :
		max_value=max_value+value[i]
		w=w+weight[i]
		m.append(i)
		i=i+1 
print "max_value=",max_value
print "items  = ",
#print m
i=0
while i<len(m):
	a=m[i]
	print items[a],",",	
	i=i+1			
