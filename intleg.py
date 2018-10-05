import sys

def error(errormsg,n,line):
    print("ERROR:",errormsg,"en la linea",n,":",line)
    exit()
if(len(sys.argv)<2):
    print("FALTA RUTA DE PROGRAMA")
    exit()
if(not sys.argv[1].endswith(".ll")):
    print("ARCHIVO INCORRECTO")
    exit()
fileObj=open(sys.argv[1],'r')
filelines=fileObj.readlines()
estados=[]
reglas={}
alfabetoE={}
alfabetoT={}
lenguaje=[]
for n in range(len(filelines)):
    line=filelines[n].rstrip()
    if(line.startswith("//")):
        continue
    terms=line.split("=>")
    if(not len(terms)==2):
        error("Mal definido el simbolo de transicion '=>'",n,line)
    if(not (terms[0].startswith("(") and terms[0].endswith(")") and terms[1].startswith("(") and terms[1].endswith(")"))):
        error("Faltan parentesis",n,line)
    terms[0]=terms[0][1:-1]
    terms[1]=terms[1][1:-1]
    print(str(terms))


fileObj.close()
