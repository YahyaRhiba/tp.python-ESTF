import os 

def list_de_note():
    note = []
    nombre_de_note = int(input("---le nombre de note : "))
    for i in  range(nombre_de_note) :
        n = float(input(f"-entrer la note  {i+1} : "))
        note.append(n)
    os.system('cls' if os.name=='nt' else 'clear')    
    return note


def  informations_sur_etudiant():
    info = {}
    print("\n----Saisi les informations d'etudiant suivant : \n")
    info["cne"] = input("---cne :  ")
    info["nom"] = input("---nom :  ")
    info["prenom"] = input("---prenom :  ")
    info["ville"] = input("---ville :  ")
    return info


# info1 : une fonction qui appelle la fonction 
# informations_sur_etudiant() et complète 
# le dictionnaire par le résultat de la fonction
# list_de_note() et retourne le dictionnaire modifié 
# de l'étudiant.
def info1() :
    etudiant = informations_sur_etudiant()
    etudiant["note"] = list_de_note()
    return etudiant


def liste_Etudiant():
    # n : Nombres des etudiants dans la class
    print("\nyahya rhiba : hello ! ")
    n = int(input("\nEntrer le nombre des etudiants dans la class : "))
    listeEtudiant = []
    for i in range(n) :
        etudiant = info1()
        listeEtudiant.append(etudiant)
    return listeEtudiant


# une fonction qui permet d’afficher la moyenne
#    des notes de chaque étudiant 
def moyenE(listeEtudiant) :
    for i in range(len(listeEtudiant)) :
        l = len(listeEtudiant[i]["note"])
        s = 0
        for j in listeEtudiant[i]["note"] :
            s += j
            m = s/l
        nom =  listeEtudiant[i]["cne"]   
        print(f"le moyen de l'etudiant de cne  '"+str(nom)+"' est : ",m)      
    print()    

def moyen_general(listeEtudiant):
    liste_moyen = []
    somme_general = 0
    for i in range(len(listeEtudiant)) :
        l = len(listeEtudiant[i]["note"])
        s = 0
        for j in listeEtudiant[i]["note"] :
            s += j
            m = s/l
        liste_moyen.append(m)
    for i in liste_moyen :
        somme_general += i
    moyen_general = somme_general/len(liste_moyen) 
    return moyen_general


#  fonction qui affiche les étudiants ayant une moyenne 
#  supérieure à la moyenne générale.
def etudiant_pluM(listeEtudiant):
    moyengeneral = moyen_general(listeEtudiant)
    liste_moyen = []
    # liste index on enregistre les indise
    # des etudiant qui have moyenne plus grand
    # que moyenne general 
    index = []
    for i in range(len(listeEtudiant)) :
        l = len(listeEtudiant[i]["note"])
        s = 0
        for j in listeEtudiant[i]["note"] :
            s += j
            m = s/l
        liste_moyen.append(m)
    e = 0
    for i in liste_moyen :
        if i >= moyengeneral :
            index.append(e)
        e += 1
    print("\nles étudiants ayant une moyenne supérieure à la moyenne générale sont :  \n")    
    k = 1
    for i in index :
        print(f"etudiant numero {k}")
        print("nom  : "+str(listeEtudiant[i]["nom"]))
        print("prenom :  "+str(listeEtudiant[i]["prenom"])+"\n")                          
        k += 1


def top3(listeEtudiant):
    liste_moyen = []
    # liste index on enregistre les indise
    # des trois etudiant qui have moyenne plus grand 
    index = []
    for i in range(len(listeEtudiant)) :
        l = len(listeEtudiant[i]["note"])
        s = 0
        for j in listeEtudiant[i]["note"] :
            s += j
            m = s/l
        liste_moyen.append(m)
    r = len(listeEtudiant)   
    if r < 3 :
        for i in range(r) :
            o = liste_moyen.index(max(liste_moyen))
            index.append(o)
            liste_moyen[o] = 0
    else :    
        for i in range(3) :
            o = liste_moyen.index(max(liste_moyen))
            index.append(o)
            liste_moyen[o] = 0            
    print("\nles meillure etudiants sont : \n")    
    for i in index :
        print("nom  : "+str(listeEtudiant[i]["nom"]))
        print("prenom :  "+str(listeEtudiant[i]["prenom"])+"\n") 


def  les_plus_faibles(listeEtudiant) :
    liste_moyen = []
    # liste index on enregistre les indise
    # des trois etudiant qui have moyenne plus grand 
    index = []
    for i in range(len(listeEtudiant)) :
        l = len(listeEtudiant[i]["note"])
        s = 0
        for j in listeEtudiant[i]["note"] :
            s += j
            m = s/l
        liste_moyen.append(m)
    r = len(listeEtudiant)
    if r < 3 :
        for i in range(r) :
            o = liste_moyen.index(min(liste_moyen))
            index.append(o)
            liste_moyen[o] = 99999
    else :
        for i in range(3) :
            o = liste_moyen.index(min(liste_moyen))
            index.append(o)
            liste_moyen[o] = 99999
    print("\nles étudiants les plus faibles : \n")    
    for i in index :
        print("nom  : "+str(listeEtudiant[i]["nom"]))
        print("prenom :  "+str(listeEtudiant[i]["prenom"])+"\n")   
    

def moyen_ville(listeEtudiant):
    liste_moyen = []
    list_ville = []
    for i in range(len(listeEtudiant)) :
        l = len(listeEtudiant[i]["note"])
        s = 0
        for j in listeEtudiant[i]["note"] :
            s += j
            m = s/l
        liste_moyen.append(m)    
    k = 0
    for j in listeEtudiant :
        list_ville.append(listeEtudiant[k]["ville"])
        k += 1    
    g={}
    u = 0    
    for i in list_ville :
        c = list_ville.count(i)
        if  c == 1 :
            g[list_ville[u]] = liste_moyen[u]  
        else :
            p = []
            m = list_ville.copy()
            for j in range(c) :
                p.append(m.index(i))
                m[m.index(i)] = "0"
            a =  0    
            for t in p :
                a += liste_moyen[t]
                g[list_ville[u]]  = a/len(p)
        u+=1
    print(" la moyenne des étudiants par ville est : \n")    
    print(g)

liste = liste_Etudiant()
for i in liste :
    print(i)
print()    
moyenE(liste)
moyen_g = moyen_general(liste)
print("le moyenne general de la class est : ",moyen_g)
etudiant_pluM(liste)
top3(liste)
print()
les_plus_faibles(liste)
moyen_ville(liste)
