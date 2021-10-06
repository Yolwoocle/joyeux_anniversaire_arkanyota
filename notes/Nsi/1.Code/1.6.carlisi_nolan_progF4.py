#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 06/10/2021 08:15:53              ┃
#┃ Mise a jour: 06/10/2021 09:05:13           ┃
#┃ Fichier: 1.6.carlisi_nolan_progF4.py       ┃
#┃ Exercice fiche 4                           ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# Exo 1 {{{2
def truc(a,b):
    print(f"{a=}, {b=}")
    if b==0: return a
    return truc(a+1, b-1)

print(f"a=7, b=5, {truc(7, 5)=}")

# Exo 2 {{{2
def fctA():
    print ("Début fonction fctA")
    i=0
    while i<5:
        print(f"fctA {i}")
        i = i + 1
    print ("Fin fonction fctA")

def fctB():
    print ("Début fonction fctB")
    i=0
    while i<5:
        if i==3:
            fctA()
            print("Retour à la fonction fctB")
        print(f"fctB {i}")
        i = i + 1
    print ("Fin fonction fctB")

fctB()

# Exercice 3 {{{2

def fact1(n):
    P=1
    for k in range(1,n+1):
        P=P*k
    return P

def fact2(n):
    P=1
    cpt=n
    while cpt>0:
        P=P*cpt
        cpt=cpt-1
    return P

def fact3(n):
    if n<=1:
        return 1
    else :
        return n*fact3(n-1)


print(fact3(998))


n = int(input("n = "))
print(fact1(n))
print(fact2(n))
print(fact3(n))

#5) 
# Exo 4 {{{2

