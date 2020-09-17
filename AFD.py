"""
Marinica Catalina
grupa 212
Simulare AFD
"""

def list_of_list(lista):
    matrix=[]
    aux=[]
    for el in lista:
        aux=[  list(i) for i in el ]
        matrix.append(aux)
    return matrix

f=open("AFD.in","r")
g=open("AFD.out","w")

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

    cuvant=cuvinte[i]
    g.write(cuvant)
    stare_curenta=0
    j=0
    ok=1
    while ok==1 and j<len(cuvant):

        for q in range(n):

            if cuvant[j] in matrice[stare_curenta][q]:
                stare_curenta=q
                j+=1
                ok=1
                break
            else:
                ok=0

    if str(stare_curenta) in stari_finale and j==len(cuvant):
        g.write(" : 1\n")
    else:
        g.write(" : 0\n")


