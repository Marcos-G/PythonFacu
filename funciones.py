import copy
def input_int( str ):
	try:
		ingreso=int(float(input( str )))
	except:
		ingreso=0
	return ingreso

def input_real( str ):
	try:
		ingreso=float(input( str ))
	except:
		ingreso=0.0
	return ingreso

def input_str( str ):
	try:
		ingreso=input( str )
	except:
		ingreso=""
	return ingreso

# Clase arreglos
class array:
        data=[]
        def __init__(self,size=None,init_value=0):
                if size == None:
                        self.size=0
                else:
                        self.size=size
                self.data= [copy.deepcopy(init_value) for i in range(0,size)]
                self.type = type(init_value)
        def __getitem__(self,index):
                if index > self.size:
                        print ("IndexError: index Out of bounds")
                else:
                        return self.data[index]
        def __setitem__(self,index,value):
                if index > self.size:
                        print ("IndexError: index Out of bounds")
                elif type(value) != self.type and value!=None:
                        print ("TypeError: value error")
                else:
                        self.data[index]=value
        def __str__(self):
                return str([self.data[i] for i in range(0,len(self.data))])

        def __len__(self):
                return(self.size)
class LinkedList:
    head=None
class Node:
    value=None
    nextNode=None
class Empleado:
    nombre=None
    edad=None
    nroLegajo=None
def append(linkedList,element):
    newNode=Node()
    newNode.value=element
    if linkedList.head==None:
        linkedList.head=newNode
    else:
        n=linkedList.head
        while n.nextNode!=None:
            n=n.nextNode
        n.nextNode=newNode
def add(linkedList,element):
    new=Node()
    new.value=element
    new.nextNode=linkedList.head
    linkedList.head=new
def search(linkedList,element):
    if linkedList.head!=None:
        res=0
        n=linkedList.head
        if n.value==element:
            return res
        while(n.nextNode!=None):
            n=n.nextNode
            res+=1
            if n.value==element:
                return res
    return -1
def insert(linkedList,element,position):
    new=Node()
    new.value=element
    if position==0:
        new.nextNode=linkedList.head
        linkedList.head=new
    elif position<0:
        return -1
    else:
        n=linkedList.head
        for i in range(1,position):
            n=n.nextNode
            if n==None:
                return -1
        new.nextNode=n.nextNode
        n.nextNode=new
    return position
def delete(linkedList,element):
    n=linkedList.head
    pos=0
    if n!=None and n.value==element:
        linkedList.head=n.nextNode
        return pos
    while n.nextNode!=None:
        pos+=1
        if n.nextNode.value==element:
            n.nextNode=n.nextNode.nextNode
            return pos
        n=n.nextNode
    return -1
def deleteFrom(linkedList,element,init):
    n=linkedList.head
    pos=0
    if n!=None and n.value==element and init==0:
        linkedList.head=n.nextNode
        return pos
    while n!=None and init>0:
        n=n.nextNode
        init-=1
    while n.nextNode!=None:
        pos+=1
        if n.nextNode.value==element:
            n.nextNode=n.nextNode.nextNode
            return pos
        n=n.nextNode
    return -1
def intercalar(L1,L2):
    curr1=L1.head
    curr2=L2.head
    C=LinkedList()
    while(curr1!=None or curr2!=None):
        if(curr1!=None):
            append(C,curr1.value)
            curr1=curr1.nextNode
        if(curr2!=None):
            append(C,curr2.value)
            curr2=curr2.nextNode
    return C
def deleteCoincidenciaPar(A,C):
    currA=A.head
    while currA!=None:
        if(currA.value%2 == 0):
            delete(C,currA.value)
        currA=currA.nextNode
def listaImpares(C):
    D=LinkedList()
    curr=C.head
    while curr!=None:
        if curr.value%2 != 0:
            append(D,curr.value)
        curr=curr.nextNode
    return D
def deleteRepetidos(A):
    curr=A.head
    pos=0
    while curr!=None:
        for i in range(count(A,curr.value)-1):
            deleteFrom(A,curr.value,pos)
        pos+=1
        curr=curr.nextNode
def deleteRepetidosE(A):
    curr=A.head
    while curr.nextNode!=None:
        busqueda=curr
        while busqueda.nextNode!=None:
            if busqueda.nextNode.value==curr.value:
                busqueda.nextNode=busqueda.nextNode.nextNode
                continue
            busqueda=busqueda.nextNode
        if curr.nextNode!=None:
            curr=curr.nextNode
def deleteRepetidosEmp(A):
    curr=A.head
    while curr.nextNode!=None:
        busqueda=curr
        while busqueda.nextNode!=None:
            if busqueda.nextNode.value.nroLegajo==curr.value.nroLegajo:
                busqueda.nextNode=busqueda.nextNode.nextNode
                continue
            busqueda=busqueda.nextNode
        if curr.nextNode!=None:
            curr=curr.nextNode
def print_list(linkedList):
    st="Vacio"
    if(linkedList.head!=None):
        n=linkedList.head
        st=str(n.value)
        while n.nextNode!=None:
            n=n.nextNode
            st=st+"=>"+str(n.value)
    print(st)
import random
