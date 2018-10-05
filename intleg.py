import sys

def error(errormsg,n,line):
    print"ERROR:",errormsg,"en la linea",n,":",line
    exit()
if(len(sys.argv)<2):
    print"FALTA RUTA DE PROGRAMA"
    exit()
if(not sys.argv[1].endswith(".ll")):
    print"ARCHIVO INCORRECTO"
    exit()
fileObj=open(sys.argv[1],'r')
filelines=fileObj.readlines()
automata={}
reglas={}
alfabetoE={}
alfabetoT={}
lenguaje=[]
for n in range(len(filelines)):
    line=filelines[n].rstrip()
    if(line.startswith("//")):
        continue
    if("//" in line):
        line=line[0:line.index("//")]
    if(not all(c in dict.fromkeys("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890=>(),/") for c in line)):
        error("Caracteres no aceptados presentes",n,line)
    terms=line.split("=>")
    if(not len(terms)==2):
        error("Mal definido el simbolo de transicion '=>'",n,line)
    if(not (terms[0].startswith("(") and terms[0].endswith(")") and terms[1].startswith("(") and terms[1].endswith(")"))):
        error("Faltan parentesis",n,line)
    valspre=terms[0][1:-1].split(",")
    valspos=terms[1][1:-1].split(",")
    if(len(valspre)>3 or len(valspos)>3):
        error("Cantida de valores incorrecta en la transicion",n,line)
    if(valspre[0] not in automata.keys()):
        automata[valspre[0]]={}
    if(valspre[1] not in automata[valspre[0]].keys()):
        automata[valspre[0]][valspre[1]]={}
    if("&" not in automata[valspre[0]][valspre[1]].keys()):
        automata[valspre[0]][valspre[1]]["&"]=[]
    automata[valspre[0]][valspre[1]]["&"].append((valspos[0],"&","D"))
print(str(automata))


fileObj.close()
