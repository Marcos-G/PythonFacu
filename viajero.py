from funciones import *
from time import time
import random
from time import time
def generate_primos_array(n):#Genero un array de primos donde cada primo representa una ciudad
    P=[[0] for i in range(n)]
    pos=0
    curr=2
    while pos<n:
        primo=True
        for i in range(0,pos):
            if curr%P[i]==0:
                primo=False
                break
        if primo:
            P[pos]=curr
            pos+=1
        curr+=1

    return P
class Rama:#Clase Rama para devolver dos valores de distinto tipo en la funcion viajero
	lista=None
	costo=None
progressval=0
import sys
timer=round(time())
def progress(irep):
	global progressval
	global timer
	progressval+=irep
	if(round(time())>timer+3):
		timer=round(time())
		global Milis
		print(progressval,"%,faltan aprox",(time()-Milis)/progressval*(100-progressval),"segundos",end="\r")
def generate_mendoza(N):
    M=array(N,array(N,0))
    # Generamos valores para la matriz triangular inferior
    if N>9: #fila 9
    	M[9][0]=421
    	M[9][1]=333
    	M[9][2]=347
    	M[9][3]=390
    	M[9][4]=371
    	M[9][5]=269
    	M[9][6]=437
    	M[9][7]=188
    	M[9][8]=265
    if N>8: #fila 8
    	M[8][0]=323
    	M[8][1]=299
    	M[8][2]=288
    	M[8][3]=290
    	M[8][4]=251
    	M[8][5]=235
    	M[8][6]=248
    	M[8][7]=84
    if N>7: #fila 7
    	M[7][0]=232
    	M[7][1]=215
    	M[7][2]=229
    	M[7][3]=250
    	M[7][4]=252
    	M[7][5]=150
    	M[7][6]=250
    if N>6: #fila 6
    	M[6][0]=140
    	M[6][1]=154
    	M[6][2]=133
    	M[6][3]=100
    	M[6][4]=104
    	M[6][5]=217
    if N>5: #fila 5
    	M[5][0]=82
    	M[5][1]=64
    	M[5][2]=78
    	M[5][3]=121
    	M[5][4]=102
    if N>4: #fila 4
    	M[4][0]=55
    	M[4][1]=46
    	M[4][2]=38
    	M[4][3]=8
    if N>3: #fila 3
    	M[3][0]=43
    	M[3][1]=59
    	M[3][2]=38
    if N>2: #fila 2
    	M[2][0]=16
    	M[3][1]=16
    if N>1: #fila 1
    	M[1][0]=19

    # Copiamos los valores generados para la matriz triangular superior
    for i in range(0,N):
        for j in range(0,N):
            if i>j:
                M[j][i]=M[i][j]
    return M
def viajero(costo,city_ant,minimoHEM,control,n,repetir,rec,rep,city_obj,todos,debug):#costo:(real)costo acumulado hasta el momento en la rama, city_ant:(entero) ciudad anterior en la rama, minimoHEM:(real)costo del recorrido mas rapido Hasta El Momento, control:(entero) valor de control para saber que ciudades se han visitado, n:(entero) cantidad de ciudades, repetir:(boolean) si se pueden repetir o no las ciudades

    minr=-1
    minL=LinkedList()#creo una lista donde voy a guardar la rama de menor costo de este nodo
    h=0
    irep=rep/(n-1)
    while h<n and (control%P[OP[city_ant][h]])==0:
        h+=1
    for i in range(0,n):#avanzo por todas las posibles ciudades
        k=(OP[city_ant][(i+h)%n])
        recr=rec+"-"+str(k)
        if k!=city_ant and M[city_ant][k]!=None :#solo puedo avanzar por una ciudad distinta de a actual y por la que exista camino

            costor=costo+M[city_ant][k]
            controlr=control*P[k]
            if(debug):
            	print("     "*(len(rec)-1),recr,end="")
            if costor>=minimoHEM:#si al sumar el costo del viaje se supera el minimoHEM, o si no se puede repetir y si se repitió una ciudad
                if(debug):
                	print("--",costor,"MALO(Supero el minimoHEM)")
                progress(irep)
                continue#no evaluo la rama porque no me va a servir
            elif ((not repetir) and (not (exito%controlr==0))):#si al sumar el costo del viaje se supera el minimoHEM, o si no se puede repetir y si se repitió una ciudad
                if(debug):
                	print("--",costor,"MALO(No se puede repetir)")
                progress(irep)
                continue#no evaluo la rama porque no me va a servir
            elif k==city_obj and (controlr%exito==0 or (not todos)):#si estoy probando volver a la ciudad inicial y ya recorri todos los nodos(y ya probe que costor es menor que minimoHEM)
                minimoHEM=costor#guardo el costo final de esta rama y el nodo que es 0 porque se esta cerrando el camino
                minr=city_obj
                print(" ",recr,"--",costor,"BUENO")
                progress(irep)
            elif(recr.count(str(city_ant)+str(k))+recr.count(str(k)+str(city_ant)))<3:#si no he recorrido todos los nodos y el costo sigue siendo menor al minimoHEM
                if(debug):
                	print("",costor,"("+str(minimoHEM)+")")
                rama=viajero(costor, k, minimoHEM, controlr, n,repetir,recr,irep,city_obj,todos,debug)#llamo a esta misma funcion agregando el costo y el valor de control correspondiente a la rama que estoy probando así como el minimoHEM(actualizado si se cerro alguna rama en esta funcion incluso)
                if rama.lista!=None:#si existe la lista devuelta y el costo es menor a minimoHEM(redundante?)
                    minimoHEM=rama.costo#actualizo el minimoHEM
                    minr=k#guardo el nodo atravez del cual obtuve la rama
                    minL=rama.lista#guardo la lista devuelta por la funcion
            elif(debug):
                print("--",costor,"MALO(por repetir mas de dos veces el mismo camino):",recr)
    ret=Rama()#creo la Rama para devolver
    if minr!=-1:#si alguna de las ciudades genero un camino que mejora el costo
        add(minL, minr)#hago add a la lista nueva o obtenida(dependiendo de si llegue aca porque cerre un camino o porque obtuve una rama)de la ciudad que derivo en encontrarla
        ret.lista=minL #guardo la lista y el costo y los retorno
        ret.costo=minimoHEM

    return ret
def generar_mat_preprocesada(M):
	n=len(M)
	Mord=[[0]*n for i in range(n)]
	for i in range(n):
		for j in range(i+1,n):
			Mord[i][j]=M[i][j]
			Mord[j][i]=M[i][j]
	OP=[[j for j in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			v=Mord[i][j]
			mini=v
			minipos=j
			posj=OP[i][j]
			for k in range(j+1,n):
				if v==None:
					v=Mord[i][k]
					mini=v
					minipos=k
				elif Mord[i][k]!=None:
					if Mord[i][k]<mini:
						mini=Mord[i][k]
						minipos=k
			Mord[i][j]=mini
			Mord[i][minipos]=v
			OP[i][j]=OP[i][minipos]
			OP[i][minipos]=posj
	for i in range(n):#imprimo bonito la matriz
		print(Mord[i])
	return OP
n=5
M=generate_mendoza(n)
maximo=100
for i in range(n):#imprimo bonito la matriz
	print(M[i])
OP=generar_mat_preprocesada(M)
for i in range(n):#imprimo bonito la matriz
	print(OP[i])
P=generate_primos_array(n)
exito=2#variable global que uso en la funcion viajero
for i in range(n):
    exito*=P[i]#multiplico todos los numeros primos que corresponden a cada ciudad para obtener el valor de exito, que me va a permitir saber que paso por todas o si pasó dos veces por una
Milis=time()#instante de inicio de busqueda
print(maximo*n+1)
inicial=0
objetivo=6
pasarPorTodasLasCiudades=True
repetirCiudades=False
debug=True
stairway_to_heaven=viajero(0,inicial,maximo*n+1,P[inicial], n,repetirCiudades,str(inicial),100.0,objetivo,pasarPorTodasLasCiudades,debug)#pido el mejor camino repitiendo y con todos los caminos, paso 0 para costo, 0 para la ciudad inicial, 100*n+1 de costo minimoHEM ya que el peor caso sería en el que todos los caminos cuestan el maximo en cuyo caso el mas barato costaria 100*n y sumo 1 para que si sucede el ultimo caso devuellva alguna de las posibilidades,2 de variable de control porque iniciamos en la ciudad cero que es el numero primo 2,n cantidad de ciudades y True para que se puedan repetir las ciudades
print(time()-Milis, "s")#imprimo tiempo de busqueda
print(stairway_to_heaven.costo)
print_list(stairway_to_heaven.lista)
print("")
"""for i in range(n):
	print(M[i])
stairway_to_heaven=viajero(0,0,100*n+1,2, n,False)#Mejor camino sin repetir
ElNodo=stairway_to_heaven.lista.head
while ElNodo!=None:
	print("=>",ElNodo.value, end="")
	ElNodo=ElNodo.nextNode
eliminar_caminos(M,4,3)#elimino un camino
print("")
for i in range(n):
	print(M[i])
stairway_to_heaven=viajero(0,0,100*n+1,2, n,True)#Mejor nodo repitiendo pero con un nodo eliminado
ElNodo=stairway_to_heaven.lista.head
while ElNodo!=None:
	print("=>",ElNodo.value, end="")
	ElNodo=ElNodo.nextNode"""
