# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:55:20 2017

@author: Mahesh
"""
import time
import os

class Robot:
    x=0
    y=0
    angle=0
    max_speed=1
    def move(self,x,y):
        self.x=x
        self.y=y
    def left(self):
        self.y=self.y-1
    def right(self):
        self.y=self.y+1
    def up(self):
        self.x=self.x-1
    def down(self):
        self.x=self.x+1
class World():
    obstacles=[[5,5,],[6,6]]
    size=[10,10]
    worldMatrix=[]
    robot=None
    def init(self,obstacles,size):
        self.obstacles=obstacles
        self.size=size
        for i in range(0,size[0]):
            row=[]
            for j in range(0,size[1]):
                row.append(0)
            self.worldMatrix.append(row)
        for ob in self.obstacles:

            self.worldMatrix[ob[0]][ob[1]]=1
    def printWorld(self):
        for i in range(0,self.size[0]):
            if i==self.robot.x:
                col=list(self.worldMatrix[i])
                col[self.robot.y]='*'
                print col
                continue
            print self.worldMatrix[i]

    def setRobot(self,robot):
        self.robot=robot
    def getx(self):
        return self.size[0]
    def gety(self):
        return self.size[1]
    def obsx(self,i) :
        for j in range(0,len(self.obstacles)):
            if i+1==self.obstacles[j][0]:
                return False
            else :
                return True
    def obsy(self,y) :
        for j in range(0,len(self.obstacles)):
            if y+1==self.obstacles[j][1]:
                return False
            else :
                return True

sinan=Robot()
sinan.move(0,0)
gridWorld=World()
gridWorld.init([[5,5],[6,6]],[10,10])



gridWorld.setRobot(sinan)
getx=gridWorld.getx()
gety=gridWorld.gety()
i=0
y=0
obsx=True
obsy=True
while i<getx-1 and y<gety-1:
    obsx=gridWorld.obsx(i)
    obsy=gridWorld.obsy(y)
    if obsx==True and obsy==True:
        sinan.down()
        sinan.right()
        os.system('cls' if os.name == 'nt' else 'clear')
        gridWorld.printWorld()
        print " ******************"
    else :
       # break
        obsx = gridWorld.obsx(i-1)
        obsy = gridWorld.obsy(y-1)
        if obsy==True:
            while y<gety:
                obsy = gridWorld.obsy(y-1)
                if obsy == True:
                    sinan.right()
                    gridWorld.printWorld()
                    print " ******************"
                    y=y+1
                else:
                    break
    time.sleep(1)
    i=i+1
    y=y+1




print sinan.x