"""
Marinica Catalina
grupa 212
AFD-minimal
"""

def afisare_AFD_minimal(Q,alfabet,F,matrice):
    g.write(str(len(Q)))
    g.write("\n")
    for x in alfabet:
        g.write(x)
        g.write(" ")
    g.write("\n")
    for x in F:
        g.write(str(x))
        g.write(" ")
    g.write("\n")
    for element in matrice:
        for x in element:
            g.write(x)
            g.write(" ")
        g.write("\n")


def unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def afisare_matrice(matrice,m,n):
    for i in range(m):
        for j in range(i):
            print(matrice[i][j],end=" ")
        print("\n",end="")

"""
--------------------------------------
Citire din fisier
--------------------------------------
"""

f=open("AFD-minimal.in","r")
g=open("AFD-minimal.out","w")

n=int(f.readline())
alfabet=f.readline().split()
stari_finale=f.readline().split()
nr_muchii=int(f.readline())

matrice=[]
for i in range(nr_muchii):
    line=f.readline()
    matrice.append(list   ( map(str, line.split()) )  )


"""
--------------------------------------
Crearea matricei X si umplerea ei cu 1
--------------------------------------
"""

X=[[0 for col in range(n)] for row in range(n)]

for i in range(1,n):
    for j in range(n):
        if(i>j):
            if(str(i) in stari_finale and str(j) not in stari_finale):
                X[i][j]=1
            if (str(j) in stari_finale and str(i) not in stari_finale):
                X[i][j] = 1


while True:
    changed=False
    for i in range (1,n):
        for j in range(i):
            if(X[i][j]==0):  #suntem pe linia i coloana j in X
                for litera in alfabet:
                    ok=0
                    for pozitie in range(nr_muchii):
                        if matrice[pozitie][0] ==str(i) and matrice[pozitie][1] == litera:
                            p=int(matrice[pozitie][2])
                            ok+=1

                        if matrice[pozitie][0] ==str(j) and matrice[pozitie][1] == litera:
                            q=int(matrice[pozitie][2])
                            ok+=1

                    if ok==2: #daca am gasit muchie si pentru i si pentru j cu litera
                        if X[p][q]==1:
                            X[i][j]=1
                            changed=True
    if changed==False:
       break


"""
--------------------------------------
Determinarea starilor echivalente
--------------------------------------
"""
stari_echivalente=[]

for i in range(n):
    for j in range(i):
        if X[i][j]==0: #sunt stari echivalente
            stari_echivalente.append([i,j])

if len(stari_echivalente)!=0:
    g.write("0 - Nu este AFD minimal\n")
    while True:
        changed=False
        for i in range(len(stari_echivalente)):
            for j in range(i+1,len(stari_echivalente)):
                if len([i for i in stari_echivalente[i] if i in stari_echivalente[j]])!=0: #daca exista un element comun in 2 stari le combinam
                    [stari_echivalente[i].append(x) for x in stari_echivalente[j] if x not in stari_echivalente[i]]
                    stari_echivalente.pop(j)
                    changed=True
                    break
            if changed==True: #vreau sa o ia de la capat de fiecare data cand se face un merge intre 2 stari
                break
        if changed==False:
           break

    for i in range(len(stari_echivalente)):
        stari_echivalente[i].sort()


    """
    --------------------------------------
    Inlocuim starile echivalente in matricea initiala
    --------------------------------------
    """

    matrice_finala=matrice

    for i in range(nr_muchii):
        for j in range(len(stari_echivalente)):
            if int(matrice_finala[i][0]) in stari_echivalente[j]:
                matrice_finala[i][0]=str(stari_echivalente[j][0])
                break
        for j in range(len(stari_echivalente)):
            if int(matrice_finala[i][2]) in stari_echivalente[j]:
                matrice_finala[i][2]=str(stari_echivalente[j][0])
                break




    matrice_finala=unique(matrice_finala)

    Q=[]
    Q=unique(  [matrice_finala[i][0] for i in range(len(matrice_finala)) if matrice_finala[i][0] ] )

    """
    --------------------------------------
    Determinam noile stari finale 
    --------------------------------------
    """

    F=[]
    vizitat=[0 for col in range(n)]
    for p in stari_echivalente:
        for x in stari_finale:
            x=int(x)
            if x in p:
                vizitat[x]=1
                F.append(p[0])
    for x in stari_finale:
        x=int(x)
        if vizitat[x]==0:
            F.append(x)
    F=unique(F)

    afisare_AFD_minimal(Q,alfabet,F,matrice_finala)

else:
    g.write("1 -AFD minimal")

