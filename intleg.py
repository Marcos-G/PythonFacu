import sys

if(len(sys.argv)<2):
    print("FALTA RUTA DE PROGRAMA")
    exit()
if(not sys.argv[1].endswith(".ll")):
    print("ARCHIVO INCORRECTO")
    exit()
fileObj=open(sys.argv[1],'r')
filelines=fileObj.readlines()
estados={}
reglas={}
alfabetoE={}
alfabetoT={}
for n in range(len(filelines)):
    line=filelines[n].rstrip()
    terms=line.split("=>")
    if(not len(terms)==2):
        print("ERROR EN LA LINEA",n,":",line)


fileObj.close()
