#assignment 4
#Name:Vasu Jain
#rollno:2019125
import time
import os
import random
class Grid:
	def __init__(self, N, start, goal, myObstacles, myRewards):
		self.N=N
		self.start=start
		self.goal=goal
		self.myObstacles=myObstacles
		self.myRewards=myRewards
	def rotateClockwise(n):
		for s in range(n):	
			rotated_c=[]
			for i in range(grid.N):
				rotated_c.append([b[j][i] for j in range(grid.N-1,-1,-1)])
			tempP=rotated_c[Player.y][Player.x]
			tempG=rotated_c[grid.goal[1]][grid.goal[0]]
			if tempP=="#":
				print("sorry no rotation is possible")
				break
			if type(tempP)==int:
				Player.energy+=tempP*grid.N
			rotated_c[Player.y][Player.x]="@"
			rotated_c[grid.goal[1]][grid.goal[0]]="$"
			for i in range(grid.N):
				for j in range(grid.N):
					if j!=Player.y and i!=Player.x:
						if rotated_c[j][i]=="@":
							rotated_c[j][i]="."
					if j!=grid.goal[1] and i!=grid.goal[0]:
						if rotated_c[j][i]=="$":
							rotated_c[j][i]="."
			Player.energy-=1
			global b
			b=rotated_c[:]
			time.sleep(0.5)
			print("current energy:"+str(Player.energy))
			grid.showGrid()


	def rotateAnticlockwise(n):
		for s in range(n):	
			rotated_a=[]
			for i in range(grid.N-1,-1,-1):
				rotated_a.append([b[j][i] for j in range(grid.N)])
			tempP=rotated_a[Player.y][Player.x]
			tempG=rotated_a[grid.goal[1]][grid.goal[0]]
			if tempP=="#":
				print("sorry no rotation is possible")
				break
			if type(tempP)==int:
				Player.energy+=tempP*grid.N
			rotated_a[Player.y][Player.x]="@"
			rotated_a[grid.goal[1]][grid.goal[0]]="$"
			for i in range(grid.N):
				for j in range(grid.N):
					if j!=Player.y and i!=Player.x:
						if rotated_a[j][i]=="@":
							rotated_a[j][i]="."
					if j!=grid.goal[1] and i!=grid.goal[0]:
						if rotated_a[j][i]=="$":
							rotated_a[j][i]="."
			Player.energy-=1
			global b
			b=rotated_a[:]
			time.sleep(0.5)
			print("current energy:"+str(Player.energy))
			grid.showGrid()
			
	def showGrid(self):
		for i in b:
			for k in range(len(i)):
				print(i[k], end=" ")
			print("\n")


class Obstacle:
	def __init__(self, x, y):
		Obstacle.x=x
		Obstacle.y=y

class Reward:
	def __init__(self, x, y, value):
		Reward.x=x
		Reward.y=y
		Reward.value=value

class Player:
	def __init__(self, x, y, energy):
		self.x=x
		self.y=y
		self.energy=energy
	def makeMove(self):
		if mm.find("R")!=-1:
			r=int(mm[mm.find("R")+1:])
			for t in range(r):
				Player.x+=1
				if Player.x>=grid.N:
					Player.x=Player.x%grid.N
				b[Player.y][Player.x-1]="X"
				Player.energy-=1 
				if b[Player.y][Player.x]=="#":
					Player.energy-=4*int(grid.N)
				if type(b[Player.y][Player.x])==int:
					Player.energy+=int(b[Player.y][Player.x])*int(grid.N)
				if b[Player.y][Player.x]=="$":
					b[Player.y][Player.x]="*"
					os.system("cls")
					grid.showGrid()
					print("you have reached your goal with energy:"+str(Player.energy))
					break
				elif Player.energy<0:
					b[Player.y][Player.x]="X"
					os.system("cls")
					print("current energy:"+str(Player.energy))
					grid.showGrid()
					print("you Loose")
					break
				b[Player.y][Player.x]="@"
				os.system("cls")
				print("current energy:"+str(Player.energy))
				grid.showGrid()
				time.sleep(0.5)
			print()

		if mm.find("L")!=-1:
			l=int(mm[mm.find("L")+1:])
			for t in range(l):
				Player.x-=1
				b[Player.y][Player.x+1]="X"
				Player.energy-=1
				if b[Player.y][Player.x]=="#":
					Player.energy-=4*int(grid.N)
				if type(b[Player.y][Player.x])==int:
					Player.energy+=int(b[Player.y][Player.x])*int(grid.N)
				if b[Player.y][Player.x]=="$":
					b[Player.y][Player.x]="*"
					os.system("cls")
					grid.showGrid()
					print("you have reached your goal with energy:"+str(Player.energy))
					break
				elif Player.energy<0:
					b[Player.y][Player.x]="X"
					os.system("cls")
					print("current energy:"+str(Player.energy))
					grid.showGrid()
					print("you Loose")
					break
				b[Player.y][Player.x]="@"
				os.system("cls")
				print("current energy:"+str(Player.energy))
				grid.showGrid()
				time.sleep(0.5)
			print()
		
		if mm.find("D")!=-1:
			d=int(mm[mm.find("D")+1:])
			for t in range(d):
				Player.y+=1
				if Player.y>=grid.N:
					Player.y=Player.y%grid.N
				b[Player.y-1][Player.x]="X"
				Player.energy-=1
				if b[Player.y][Player.x]=="#":
					Player.energy-=4*int(grid.N)
				if type(b[Player.y][Player.x])==int:
					Player.energy+=int(b[Player.y][Player.x])*int(grid.N)
				if b[Player.y][Player.x]=="$":
					b[Player.y][Player.x]="*"
					os.system("cls")
					grid.showGrid()
					print("you have reached your goal with energy:"+str(Player.energy))
					break
				elif Player.energy<0:
					b[Player.y][Player.x]="X"
					os.system("cls")
					print("current energy:"+str(Player.energy))
					grid.showGrid()
					print("you Loose")
					break
				b[Player.y][Player.x]="@"
				os.system("cls")
				print("current energy:"+str(Player.energy))
				grid.showGrid()
				time.sleep(0.5)
			print()

		if mm.find("U")!=-1:
			u=int(mm[mm.find("U")+1:])
			for t in range(u):
				Player.y-=1
				b[Player.y+1][Player.x]="X"
				Player.energy-=1
				if b[Player.y][Player.x]=="#":
					Player.energy-=4*int(grid.N)
				if type(b[Player.y][Player.x])==int:
					Player.energy+=int(b[Player.y][Player.x])*int(grid.N)
				if b[Player.y][Player.x]=="$":
					b[Player.y][Player.x]="*"
					os.system("cls")
					grid.showGrid()
					print("you have reached your goal with energy:"+str(Player.energy))
					break
				elif Player.energy<0:
					b[Player.y][Player.x]="X"
					os.system("cls")
					print("current energy:"+str(Player.energy))
					grid.showGrid()
					print("you Loose")
					break
				b[Player.y][Player.x]="@"
				os.system("cls")
				print("current energy:"+str(Player.energy))
				grid.showGrid()
				time.sleep(0.5)
			print()

N=int(input("enter a number(N) for creating NxN grid :"))
grid=Grid(N,5,5,5,5)
obs=[]
rew=[]
for o in range(random.randint(1,(grid.N)**2//2)):
	obs.append([random.randint(0,grid.N-1),random.randint(0,grid.N-1)])
for r in range(random.randint(1,(grid.N)**2//2)):
	rew.append([random.randint(0,grid.N-1),random.randint(0,grid.N-1),random.randint(1,9)])
Player=Player(random.randint(0,(grid.N)-1),random.randint(0,(grid.N)-1),2*grid.N)
rx= [i for i in range(0,Player.x)] + [i for i in range(Player.x+1,grid.N)]
yx= [i for i in range(0,Player.y)] + [i for i in range(Player.y+1,grid.N)]
grid.goal=[random.choice(rx),random.choice(yx)]
b=[]
for i in range(grid.N):
	a=[]
	for i in range(grid.N):
		a.append(".")
	b.append(a)
grid.myObstacles=obs
grid.myRewards=rew
for i in grid.myObstacles:
	b[i[1]][i[0]]="#"
for k in grid.myRewards:
	b[k[1]][k[0]]=int(k[2])
b[Player.y][Player.x]="@"
b[grid.goal[1]][grid.goal[0]]="$"
print("current energy:"+str(Player.energy))
grid.showGrid()
while Player.energy>0 and b[Player.y][Player.x]!="*":
	s=input("enter your steps : ")
	s=s.upper()
	splitindexlist=[]
	for i in range(len(s)):
		if s[i]=="R" or s[i]=="L" or s[i]=="D" or s[i]=="U" or s[i]=="C" or s[i]=="A":
			splitindexlist.append(int(i))
	inputlist=[]
	for i in range(len(splitindexlist)): # in range (4) [0246] : 
		if(i!=len(splitindexlist)-1):
			inputlist.append(s[splitindexlist[i]:splitindexlist[i+1]])
		else:
			inputlist.append(s[splitindexlist[i]:])
	for i in inputlist:	
		i=str(i)
		if i.find("R")!=-1 or i.find("U")!=-1 or i.find("L")!=-1 or i.find("D")!=-1:
			mm=i
			Player.makeMove()
		elif i.find("C")!=-1:
			Grid.rotateClockwise(int(i[i.find("C")+1:]))
		elif i.find("A")!=-1:
			Grid.rotateAnticlockwise(int(i[i.find("A")+1:]))
"""
#Player.energy:stores the Player's current energy
#inputlist:stores the sliced commands from the given input like r4d2c4 gives["R4","D2","C4"]
inputlist was needed so that commands are executed in the order in which they are given otherwise it would be depending on the code design 
#the list b is the nested list used for showing the grid every time
#in the rotating function I have implemented such that if after rotation obstacle arives at the player position then rotation is not possible 
#if after rotation there is reward that arives at the player position then player is awawrded the corresponding energy
#as showgrid function always prints the list b thus for every funciton of movement or rotation I have modified the original nested list b 
#grid.myObstacles and grid.myRewards class objects of class Grid store the randomly generated obstacle and reward objects of classes Obstacles and Rewards respectively 
#giveinput in the form (ex.)
for right 4:give r4
for moving left 7:give l7
for moving down by 8 give:d8
for moving up by 9 give :u9
for rotating clockwise 90 degree n times , give: cn
for rotating anticlockwise 90 degree n times, give:an
#note:all these inputs can be given in any order and any combinations with any values associated with each
"""

