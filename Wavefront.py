from colorama import Cursor, init, Fore,Back
import os
import sys
import time

try:

	filePath=sys.argv[1]
except Exception as e:

	filePath="Data.txt"

try:

	anim=int(sys.argv[2])
except Exception as e:

	anim=0

try:
	if(anim==0):
		process=sys.argv[3]
		if(process=="true" or process=="True"):
			process=True
		elif(process=="false" or process=="False"):
			process=False
	else:
		process=False
except Exception as e:

	process=False


timeBetweenAnmim=0.05

line           ="_________"
startWord      ="  START  "
finlaWord      ="  FINAL  "
space          ="         "
bar            ="|"

blockColor     =Back.WHITE
finalColor     =Back.MAGENTA
startColor     =Back.YELLOW
lineColor      =Fore.CYAN
wayColor       =Back.GREEN

block0         =lineColor+bar+blockColor+space
block1         =lineColor+bar+finalColor+space
block2         =lineColor+bar+startColor+space

goal           ="i"
way            ="c"

originalMatriz = []

class route:
	def __init__(self):
		self.x=None
		self.y=None

init(autoreset=True)

def clean():

	os.system("cls")

def getMatriz():
	openFile=open(filePath,"r")
	file=openFile.read()

	matriz=file.split("\n")

	for i in range(len(matriz)):
		matriz[i]=matriz[i].split(",")

	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if(matriz[i][j]=="-1"):
				matriz[i][j]=-1

	return matriz

def printM(matriz,showIn=False):
	global originalMatriz
	init       =startColor +Fore.WHITE+   startWord
	end        =finalColor +Fore.WHITE+   finlaWord
	forWay     = wayColor+ space
	
	for j in range(len(matriz[0])):
			print(lineColor+" "+lineColor+line+"",end="")
	print()
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if(matriz[i][j]==-1):
				print(block0,end="")
			elif(matriz[i][j]==1):
				print(block1,end="")
			elif(matriz[i][j]==goal):
				print(block2,end="")
			elif(matriz[i][j]==way):
					print(lineColor+bar+forWay,end="")
			else:
				print(lineColor+bar+space,end="")
		print(lineColor+bar+space)

		for j in range(len(matriz[i])):
			if(matriz[i][j]==-1):
				print(block0,end="")
			else:
				if(matriz[i][j]==1):
					print(lineColor+bar+end,end="")
				elif(matriz[i][j]==goal):
					print(lineColor+bar+init,end="")
				elif(matriz[i][j]==way):
					print(lineColor+bar+forWay,end="")
				elif(matriz[i][j]==" "):
					if(showIn):
						newI=None
						newJ=None
						if(i<10):
							newI="   "+str(i)
						elif(i<100):
							newI="  "+str(i)
						else:
							newI=" "+str(i)
						if(j<10):
							newJ=str(j)+"   "
						elif(j<100):
							newJ=str(j)+"  "
						else:
							newJ=str(j)+" "

						print(lineColor+bar+newI+","+newJ,end="")
					else:
						print(lineColor+bar+space,end="")
				else:	
					num=matriz[i][j]
					if(num<10):
						num="    "+str(num)+"    "
					elif(num<100):
						num="   "+str(num)+"    "
					elif(num<1000):
						num="   "+str(num)+"   "
					elif(num<10000):
						num="  "+str(num)+"   "
					print(lineColor+bar+num,end="")
		print(lineColor+bar+space)

		for j in range(len(matriz[i])):
			if(matriz[i][j]==-1):
				print(block0,end="")
			elif(matriz[i][j]==1):
				print(block1,end="")
			elif(matriz[i][j]==goal):
				print(block2,end="")
			elif(matriz[i][j]==way):
					print(lineColor+bar+forWay,end="")
			else:
				print(lineColor+bar+space,end="")
		print(lineColor+bar+space)

		for j in range(len(matriz[i])):
			if(matriz[i][j]==-1):
				print(lineColor+bar+blockColor+lineColor+line+"",end="")
			elif(matriz[i][j]==1):
				print(lineColor+bar+finalColor+lineColor+line+"",end="")
			elif(matriz[i][j]==goal):
				print(lineColor+bar+startColor+lineColor+line+"",end="")	
			elif(matriz[i][j]==way):
				print(lineColor+bar+wayColor+lineColor+line+"",end="")	
			else:
				print(lineColor+bar+lineColor+line+"",end="")
		print(lineColor+bar+space)
		
def inputInitEnd(tag):
	global originalMatriz
	while(True):
		try:
			start=str(input(tag+" x,y: ")).split(",")
			start[0]=int(start[0])
			start[1]=int(start[1])
			if(start[0]<0 or start[0]>(len(originalMatriz)-1) or start[1]<0 or start[1]>(len(originalMatriz[0])-1) or originalMatriz[start[0]][start[1]]==-1):
				print("Error: coordenadas invalidas")
			else:
				break
		except Exception as e:
			print("Error: coordenadas invalidas")
	return start

def printMinM():
	global originalMatriz
	if(anim==2):
		clean()
		printM(originalMatriz)
	elif(process):
		print()
		for i in range(len(originalMatriz)):
			print(originalMatriz[i])

def newmann(x,y):
	global originalMatriz
	enable=False
	##################################################
	try:
		if((x)>=0 and (y-1)>=0):
			if(originalMatriz[x][y-1]==goal ):
				originalMatriz[x][y-1]=originalMatriz[x][y]+1
				return True
			elif(originalMatriz[x][y-1]==(" ")):
				originalMatriz[x][y-1]=originalMatriz[x][y]+1
				printMinM()
				enable=True
			
	except Exception as e:
		pass
	##################################################
	try:
		if((x)>=0 and (y+1)>=0):
			if(originalMatriz[x][y+1]==goal):
				originalMatriz[x][y+1]=originalMatriz[x][y]+1
				return True
			elif(originalMatriz[x][y+1]==(" ")):
				originalMatriz[x][y+1]=originalMatriz[x][y]+1
				printMinM()
				enable=True
			
	except Exception as e:
		pass
	##################################################
	try:
		if((x+1)>=0 and (y)>=0):
			if(originalMatriz[x+1][y]==goal ):
				originalMatriz[x+1][y]=originalMatriz[x][y]+1
				return True
			elif(originalMatriz[x+1][y]==(" ")):
				originalMatriz[x+1][y]=originalMatriz[x][y]+1
				printMinM()
				enable=True
			
	except Exception as e:
		pass
	##################################################
	try:
		if((x-1)>=0 and (y)>=0):
			if(originalMatriz[x-1][y]==goal ):
				originalMatriz[x-1][y]=originalMatriz[x][y]+1
				print(str(x-1),y)
				return True
			elif(originalMatriz[x-1][y]==(" ")):
				originalMatriz[x-1][y]=originalMatriz[x][y]+1
				printMinM()
				enable=True
			
	except Exception as e:
		pass
	##################################################

	if(not enable):
		return None
	return False

def do(x,y):
	global originalMatriz

	counter=1
	auxG=newmann(x,y)
	counter+=1

	while(True and auxG!=None):
		enable=False
		arrived=False

		for i in range(len(originalMatriz)):
			for j in range(len(originalMatriz[0])):
				if(originalMatriz[i][j]==counter):
					aux=newmann(i,j)
					if(aux!=None):
						enable=True

					if(aux==True):
						arrived=True

		if(not enable):
			print("No hay ruta disponible")
			return False
		if(arrived):
			#print("Llegó")
			return True
		
		counter+=1

def organizeRoutes(x,y):
	global originalMatriz
	routes=[]

	r=route()
	r.x=x
	r.y=y

	#routes.append(r)
	cont=originalMatriz[x][y]

	while(cont>1):
		x=r.x
		y=r.y

		r=route()
		r.x=x
		r.y=y
		
		routes.append(r)

		try:
			if((x)>=0 and (y-1)>=0):
				if(originalMatriz[x][y-1]==(cont-1)):
					r.x=x
					r.y=y-1
					#print("r:",r.x,r.y," , ",x,y," | ","c:",cont)
				else:
					#Solo para generar el error
					originalMatriz[len(originalMatriz)+5][y]
			else:
				#Solo para generar el error
				originalMatriz[len(originalMatriz)+5][y]
		except Exception as e:
			##################################################
			try:
				if((x)>=0 and (y+1)>=0):
					if(originalMatriz[x][y+1]==(cont-1)):
						r.x=x
						r.y=y+1
						#print("r:",r.x,r.y," , ",x,y," | ","c:",cont)
					else:
						#Solo para generar el error
						originalMatriz[len(originalMatriz)+5][y]
				else:
					#Solo para generar el error
					originalMatriz[len(originalMatriz)+5][y]
					
			except Exception as e:
				##################################################
				try:
					if((x+1)>=0 and (y)>=0):
						if(originalMatriz[x+1][y]==(cont-1)):
							r.x=x+1
							r.y=y
							#print("r:",r.x,r.y," , ",x,y," | ","c:",cont)
						else:
							#Solo para generar el error
							originalMatriz[len(originalMatriz)+5][y]
					else:
						#Solo para generar el error
						originalMatriz[len(originalMatriz)+5][y]
						
				except Exception as e:
					##################################################
					try:
						if((x-1)>=0 and (y)>=0):
							if(originalMatriz[x-1][y]==(cont-1)):
								r.x=x-1
								r.y=y
								#print("r:",r.x,r.y," , ",x,y," | ","c:",cont)	
							else:
								#Solo para generar el error
								originalMatriz[len(originalMatriz)+5][y]
						else:
							#Solo para generar el error
							originalMatriz[len(originalMatriz)+5][y]
					except Exception as e:
						print("FatalError: Esto nunca debió suceder")
						##################################################
		cont-=1	
		#os.system("pause")

	return routes

def showAnim(copyMatriz,result):
	clean()
	printM(copyMatriz)
	time.sleep(1)

	result.pop()
	for i in range(len(result)):
		copyMatriz[result[i].x][result[i].y]=way
		clean()
		printM(copyMatriz)
		time.sleep(timeBetweenAnmim)

def showWithoutAnim(copyMatriz,result):
	result.pop()
	for i in range(len(result)):
		copyMatriz[result[i].x][result[i].y]=way

	if(not process):
		clean()
	printM(copyMatriz)

def putZeros():
	global originalMatriz
	for i in range(len(originalMatriz)):
		for j in range(len(originalMatriz[i])):
			if(originalMatriz[i][j]==" "):
				originalMatriz[i][j]=0

def main():
	global originalMatriz
	print("Wavefront Game")
	originalMatriz=getMatriz()

	clean()
	printM(originalMatriz,True)

	print()

	start=inputInitEnd("Inicio")
	end=inputInitEnd("Final")

	originalMatriz[start[0]][start[1]]=goal
	originalMatriz[end[0]][end[1]]=1

	if(process):
		print("Proceso detallado")
	printMinM()
	if(do(end[0],end[1])):
		printMinM()
		result=organizeRoutes(start[0],start[1])

		putZeros()

		if(anim==0):
			if(not process):
				clean()
			if(process):
				print("Coordenadas del camino")
				for i in range(len(result)):
					print(result[i].x,result[i].y)
			copyMatriz=originalMatriz
			copyMatriz[start[0]][start[1]]=goal
			showWithoutAnim(copyMatriz,result)
		else:

			copyMatriz=originalMatriz
			copyMatriz[start[0]][start[1]]=goal
			showAnim(copyMatriz,result)

if __name__ == '__main__':
	if((anim>=0 and anim<3) and str(type(process))=="<class 'bool'>"):
		main()
	else:
		print("Error: argumentos invalidos") 