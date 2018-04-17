class Robot:
	x=0
	y=0
	angle=0
	max_speed=1
class World:
	obstacles=[[5,5],[6,6]]
	size=[10,10]
	worldmatrix=[]
	robot=None
	def init(self,obstacles,size):
		self.obstacles=obstacles
		self.size=size
		for i in range(0,size[0]):
			row=[]
			for j in range(0,size[1]):
				row.append(0)
			self.worldmatrix.append(row)
		for ob in obstacles:
			self.worldmatrix[ob[0]][ob[1]]=1
	def printworld(self):
		for i in range(0,self,size[0]):
			
