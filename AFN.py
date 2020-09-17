"""
Marinica Catalina
grupa 212
Simulare AFN
"""

def list_of_list(lista):
    matrix=[]
    aux=[]
    for el in lista:
        aux=[  list(i) for i in el ]
        matrix.append(aux)
    return matrix

f=open("AFN.in","r")
g=open("AFN.out","w")

n=int(f.readline())
alfabet=f.readline().split()
stari_finale=f.readline().split()

matrice=[]
for i in range(n):
    line=f.readline()
    matrice.append(list   ( map(str, line.split()) )  )
matrice=list_of_list(matrice)

m=int(f.readline())
cuvinte=f.readline().split()
f.close()

for i in range(m):
    queue=[0]
    cuvant=cuvinte[i]
    g.write(cuvant)

    j=0
    ok=1
    while j<len(cuvant) and len(queue)!=0 :
            aux=len(queue)
            for i in range(0,aux):
                stare_curenta=queue[0]
                for q in range(n):
                    if cuvant[j] in matrice[stare_curenta][q]:
                        ok=1
                        queue.append(q)

                queue.pop(0)
            j+=1

    if len(queue)==0:
        g.write(" : 0\n")
    else:
        ok=0
        for i in queue:
            if str(i) in stari_finale and j == len(cuvant):
                g.write(" : 1\n")
                ok=1
                break
        if ok==0:
            g.write(" : 0\n")


