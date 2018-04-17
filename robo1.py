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
                col[self.robot.y]="*"
                print col
                continue
            print self.worldMatrix[i]
    def findob(self,i,j):
        if self.worldMatrix[i+1][j]==1:
            return True
        else :
            return False

    def checkj(self,j):
        if j-1<self.size[1]:
            return True
        else:
            return False

    def checki(self,i):
        if i< self.size[0]:
            return True
        else:
            return False
    def cheroot(self,i):
        if self.worldMatrix[i][i+1]!=1:
            return "right"
        elif self.worldMatrix[i+1][i-1]!=1:
            return "down"
    #def outbox(self,i):
     #   if i>size[i]  and
    def setRobot(self,robot):
        self.robot=robot
sinan=Robot()
sinan.move(0,0)
gridWorld=World()
gridWorld.init([[5,5],[6,6]],[10,10])



gridWorld.setRobot(sinan)
check=False
outbox=False
gridWorld.printWorld()
print " ******************"
i=0
j=0
while i<10:
    checkj=False
    while j<11:
        checkj=gridWorld.checkj(j)
        check = gridWorld.findob(i,j)
        if check==False and checkj==True:
            sinan.right()
            gridWorld.printWorld()
            print " ******************"
            j=j+1

            time.sleep(1)
        #else :

    i=i+1
    checki= gridWorld.checki(i)
    check = gridWorld.findob(i,j)
    if check == False and checki==True:
        sinan.left()
        break
        gridWorld.printWorld()
        print " ******************"
    os.system('cls' if os.name == 'nt' else 'clear')


    time.sleep(1)




print sinan.x