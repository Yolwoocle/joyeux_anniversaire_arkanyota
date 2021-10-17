#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 13/10/2021 08:19:29              ┃
#┃ Mise a jour: 15/10/2021 14:56:23           ┃
#┃ Fichier: 1.7.carlisi_nolan_progF5.py       ┃
#┃ Exercice fiche 5                           ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from turtle import *
from time   import sleep

# Exercice 1 {{{1
def spirale(a, long):
    if long >= 0:
        forward(long)
        right(a)
        spirale(a, long-5)


# Exercice 2 {{{1
def cercles(n):
    if n>0:
        circle(n, 360)
        cercles(n-5)

def polygone(n, long):
    assert 360%n==0, "!possible"
    angle = 360//n
    for k in range(n):
        forward(long)
        left(angle)

def des_polygones(n, long):
    if long>0:
        polygone(n, long)
        des_polygones(n, long-5)
        #polygone(n-5, long)


# Exercice 3 {{{1
def dessin_recursif(n, max_n=None, angle=360):
    max_n = n if max_n is None else max_n
    n_angle = ((n-1)/max_n)*360
    if n <= 0: return None
    setheading(angle)
    up()
    goto(0,0)
    down()
    l = 20
    begin_fill()
    for i, j in [(1, 1), (5, 1), (6, 1), (2, 1), (4, -1), (3, 1),(1, 1)]:
        forward(i*l)
        left(90*j)
    end_fill()
    dessin_recursif(n-1, max_n,n_angle)
    

# Exercice 4 {{{1
def parenthese(txt, n):
    if txt=="":
        return n==0
    else:
        if txt[0]=="(":
            return parenthese(txt[1:], n+1)
        elif txt[0]==")":
            return parenthese(txt[1:], n-1)
def parenthese2(txt, n):
    print(txt, n)
    if n<0:
        return False
    if txt=="":
        return n==0
    else:
        if txt[0]=="(":
            return parenthese2(txt[1:], n+1)
        elif txt[0]==")":
            return parenthese2(txt[1:], n-1)
            
def parenthese3(txt, n):
    print(txt, n)
    if n<0:
        return False
    if txt=="":
        return n==0
    else:
        if txt[0]=="(":
            return parenthese3(txt[1:], n+1)
        elif txt[0]==")":
            return parenthese3(txt[1:], n-1)
        else:
            return parenthese3(txt[1:], n)

# Exercice 5 {{{1
def consecutifs(L):
    if len(L) <= 1: return False
    return True if L[0]+1==L[1] else consecutif(L[1:])
    # VERSION MONOLINE
    # return if len(L) <= 1 else (True if L[0]+1==L[1] else consecutif(L[1:]))

# Exercice 6 {{{1
def som(x, n):
    if n<=0:
        return 1
    print(f"{x=} * som({x=}, {n-1=})+1")
    return x * som(x, n-1)+1

# Exercice 7 {{{1
def u(n):
    if n==-1: return 5
    return 2*v(n)

def v(n):
    if n==-1: return 2
    return 2*u(n-1)+v(n-1)

# IF NAME == MAIN: {{{1
if __name__== "__main__":
    speed("fastest")
    ## Exo 2
    # des_polygones(4, 80)
    # des_polygones(6, 80)
    ## Exo 3
    dessin_recursif(4)
    ## Exo 4
    # print(parenthese3("test", 0))
    # print(parenthese3("()", 0))
    # print(parenthese3("(test)", 0))
    # print(parenthese3("(hello)azer)", 0))
    # print(parenthese3("((m) ) (on()t( est (est (bo))n))", 0))
    # print(parenthese3("((m) ) (on)t( est (est (bo))n))", 0))
    # print(parenthese3("truc(22()bidule(23)56", 0))
    ## Exo 5
    ## Exo 6
    # print(som(5, 3))
    ## Exo 7
    # for i in range(10):
    #     print(i,"\t", u(i), "\t", v(i))

    sleep(1)


