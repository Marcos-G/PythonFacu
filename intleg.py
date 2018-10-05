import sys

if(len(sys.argv)<2):
    print("FALTA RUTA DE PROGRAMA")
    exit()
if(not sys.argv[1].endswith(".ll")):
    print("ARCHIVO INCORRECTO")
    exit()
filelines=open(sys.argv[1],'r').readlines()
estados={}
reglas={}
alfabetoE={}
alfabetoT={}
for n in len(filelines):
    line=filelines[n].rstrip()
    terms=line.split("=>")
    if(not terms==2):
        print("ERROR EN LA LINEA",n,":",line)


filelines.close()
