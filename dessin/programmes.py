"""
#Ce programme permet de calculer comment rembourser en utilisent le moinsde pièces possibles
def monnaie(somme):
    monnaie=[200,100,50,20,10,5,2,1]
    distribue=[]
    nb_pieces=[0]*8
    for i in range(len(monnaie)):
        while somme>=monnaie[i]:
            somme=somme-monnaie[i]
            distribue.append(monnaie[i])
            nb_pieces[i]=nb_pieces[i]+1
    return distribue, nb_pieces

print(monnaie(79))

#Ce programme permet de faire augmenter les trajectoires x, y et z afin de faire "avancer" le personnage
class Personnage:
        def __init__(self, x, y, z):
            self.x=x
            self.y=y
            self.z=z
        def avance(self):
            self.x= self.x + 1
            return self.x
        def droite(self):
            self.y= self.y + 1
            return self.y
        def saute(self):
            self.z= self.z + 1
            return self.z
        def __str__(self):
            return f"Les nouvelles positions sont ({self.x};{self.y};{self.z})"
        def affiche(self):
            print("C'est le vecteur de coordonnées(",self.x,";",self.y,";",self.z,")")
            return None

pers1=Personnage(0,0,0)
pers1.avance()
pers1.saute()
pers1.droite()
pers1.avance()
print(pers1.affiche())
print(pers1)
# Ce programme fait les calculs liés aux nombres complexes
from math import *
class Complexe:
    def __init__(self,re,im):
        self.z=(re,im)

    def __str__(self):
        return f"Le nombre complexe est {self.z}"

    def __add__(self,other):
        return self.z[0]+other.z[0],self.z[1]+other.z[1]

    def __sub__(self,other):
        return self.z[0]-other.z[0],self.z[1]-other.z[1]

    def __mul__(self,other):
        return self.z[0]*other.z[0]-self.z[1]*other.z[1],self.z[0]*other.z[0]+self.z[1]*other.z[1]

    def __eq__(self,other):
        return self.z[0]==other.z[0] and self.z[1]==other.z[1]

    def module(self):
        return sqrt(self.z[0]**2+self.z[1]**2)

z1=Complexe(-3,5)
z2=Complexe(7,1)
print(z1)
print(z1+z2)
print(z1-z2)
print(z1*z2)
print(z1==z2)
print(z1.module())



class Fraction:
    def __init__(self,numerateur,denominateur):
        self.num=numerateur
        self.denom=denominateur

    def __str__(self):
        return f"La fonction est({self.num};{self.denom})"

    def pgcd(self,a,b):
        if b==0:
            return a
        else:
            return self.pgcd(b,a%b)

    def simplifie(self):
        a=self.num//self.pgcd(self.num,self.denom)
        b=self.denom//self.pgcd(self.num,self.denom)
        return Fraction(a,b)

    def __eq__(self,other):
        return self.num*other.denom==self.denom*other.num

f1=Fraction(24,18)
f2=Fraction(4,2)
print(f1.pgcd(24,18))
print(f1.simplifie())
print(f1==f2)




class Date:
    def __init__(self,jour,mois,annee):
        self.jour=jour
        self.mois=mois
        self.annee=annee

    def __str__(self):

        return f"C'est la date {self.jour} {self.mois} {self.annee}"

    def __lt__(self,other):

        dic={"janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,"juillet":7,"aout":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12}

        if self.annee<other.annee:
            return "La première date est plus vielle"

        if self.annee > other.annee:
            return "La deuxième date est plus vielle"

        if self.annee == other.annee:
            if dic[self.mois] < dic[other.mois]:
                return "La première date est plus vielle"

            if dic[self.mois] > dic[other.mois]:
                return "La deuxième date est plus vielle"

            if self.mois == other.mois:
                if self.jour < other.jour:
                    return "La première date est plus vielle"

                if self.jour > other.jour:
                    return "La deuxième date est plus vielle"

                if self.jour == other.jour:
                    return "Les deux dates sont les mêmes"

#l={"janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,"juillet":7,"aout":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12}

date_1=Date(28,"juillet",2007)
date_2=Date(30,"décembre",2004)

print(date_1<date_2)





class Pile:

    def __init__(self):
        self.L=[]

    def __repr__(self):
        ch="Sommet\n"
        for i in range(len(self.L)-1,-1,-1):
            ch+=" | "+str(self.L[i]) + "|\n"
        return ch+ 'Fond'

    def estVide(self):
        return self.L==[]

    def empiler(self,x):
        self.L.append(x)

    def depiler(self):
        if len(self.L)==0:
            return 'Erreur'
        else:
            a=self.L.pop()

        return a

    def sommet(self):
        if len(self.L)==0:
            return 'Erreur'
        else:
            a=self.L[-1]

    def taille(self):
        return len(self.L)

    def trouver(pile_1):
        pile_2=[]

        if len(pile_1)/2==0:
            for elem in pile_1:
                if elem=='(':
                    pile_2.empiler(elem)

                elif elem==')':
                    if pile_1==[]:
                        return False
                else:
                    pile_1.depiler()
            if pile_1==[]:
                return True
        else:
            return False



def notation_polonaise(calcul):
    p=Pile()

    for elem in calcul:
        if elem not in ["+","-","*","/"]:
            p.empiler(elem)

        else:

            if elem=='+':
                a=p.depiler()
                b=p.depiler()
                p.empiler(a+b)

            if elem=='-':
                a=p.depiler()
                b=p.depiler()
                p.empiler(b-a)

            if elem=='*':
                a=p.depiler()
                b=p.depiler()
                p.empiler(a*b)

            if elem=='/':
                a=p.depiler()
                b=p.depiler()
                assert a!=0, 'division par 0'
                p.empiler(b/a)

    return p.depiler()


print(notation_polonaise([1,2,"+",3,"*"]))






class File:

    def __init__(self):
        self.L=[]

    def __repr__(self):
        ch="queue"
        for i in range(len(self.L)-1,-1,-1):
            ch+=" | "+str(self.L[i]) + "|"
        return ch+ 'tête'

    def estVide(self):
        return self.L==[]

    def enfiler(self,x):
        self.L.append(x)

    def defiler(self):
        if len(self.L)==0:
            return 'Erreur'
        else:
            a=(self.L).pop(0)

        return a

    def liretete(self):
        if len(self.L)==0:
            return 'Erreur'
        else:
            a=self.L[0]
















class Arbre:
    def __init__(self,r,g=None,d=None):
        self.racine=r
        self.gauche=g
        self.droit=d

    def __eq__(self,a):
        if type(self.gauche)!= type(a.gauche) or type(self.droit)!=type(a.droit):
            return False
        return self.racine == a.racine and self.gauche == a.gauche and self.droit==a.droit


    def affiche(self,space=0):
        if self.droit:
            self.droit.affiche(space+1)
        print("  "*space,self.racine)
        if self.gauche:
            self.gauche.affiche(space+1)

    def Taille(self):
        t=1

        if self.gauche is not None:
            t=t+self.gauche.Taille()

        if self.droit is not None:
            t=t+self.droit.Taille()

        return t

    def Hauteur(self):
        hg=0
        hd=0

        if self.gauche is not None:
            hg=hg+self.gauche.Hauteur()

        if self.droit is not None:
            hd=hd+self.droit.Hauteur()

        return 1+max(hg,hd)

    def parcoursPre(self,l=[]):

        l.append(self.racine)

        if self.gauche is not None:
            self.gauche.parcoursPre()

        if self.droit is not None:
            self.droit.parcoursPre()

        return l

    def parcoursIn(self,l=[]):
        if self.gauche is not None:
            self.gauche.parcoursIn()

        l.append(self.racine)

        if self.droit is not None:
            self.droit.parcoursIn()
        return l

    def parcoursPost(self, l=[]):
        if self.gauche is not None:
            self.gauche.parcoursPost()

        if self.droit is not None:
            self.droit.parcoursPost()

        l.append(self.racine)

        return l

    def parcoursLarg(self):
        noeud_a_Visite=[self]
        ordreVisite=[]
        while noeud_a_Visite!=[]:
            noeud=noeud_a_Visite.pop(0)
            ordreVisite.append(noeud.racine)

            if noeud.gauche is not None:
                noeud_a_Visite.append(noeud.gauche)

            if noeud.droit is not None:
                noeud_a_Visite.append(noeud.droit)

        return ordreVisite

    def rechercher(self,valeur):
        if valeur==self.racine:
            return True
        if valeur<self.racine:
            if self.gauche is None:
                return False
            else:
                return self.gauche.rechercher(valeur)
        else:
            if self.droit is None:
                return False
            else:
                return self.droit.rechercher(valeur)

    def ajouter(self,valeur):
        if valeur <= self.racine:
            if self.gauche is None:
                self.gauche=Arbre(valeur)
            else:
                return self.gauche.ajouter(valeur)
        else:
            if self.droit is None:
                self.droit=Arbre(valeur)
            else:
                return self.droit.ajouter(valeur)

        return self

    def minimum(self):
        if self.gauche is None:
            return self.racine
        else:
            return self.gauche.minimum()

    def maximum(self):
        if self.droit is None:
            return self.racine
        else:
            return self.droit.maximum()
"""