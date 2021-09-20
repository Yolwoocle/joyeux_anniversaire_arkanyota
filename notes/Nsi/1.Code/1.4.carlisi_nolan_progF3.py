#!/usr/bin/env python
# vim: set sw=4 sts=4 et fdm=marker:
#┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
#┃ Creation: 20/09/2021 16:08:20              ┃
#┃ Mise a jour: 20/09/2021 16:13:20           ┃
#┃ Fichier: 1.4.carlisi_nolan_progF3.py       ┃
#┃ Exercice fiche 3 Exo 1 à 10                ┃
#┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

def Exo1(): # {{{1
    m = int(input("L'entier m : "))
    n = int(input("L'entier n : "))
    return list(range(n+1, m))


def Exo2(): # {{{1
    pass


def Exo3(): # {{{1
    pass


def Espacement(n): # {{{1
    print("=================")
    print(f"Exo {n}\n")


if __name__ == "__main__": # {{{1
    import sys
    Exos = [Exo1, Exo2, Exo3] # , Exo4, Exo5, Exo6, Exo7, Exo8, Exo9, Exo10, Exo11]
    # Si il y'a un argument dans l'execution 
    if len(sys.argv) == 1 or (not sys.argv[1].isdigit()):
        for index,i in enumerate(Exos):
            Espacement(index+1)
            retour = i()
            if retour != None:
                print(retour)
    else:
        Espacement(sys.argv[1])
        retour = Exos[int(sys.argv[1])-1]()
        if retour != None:
            print(retour)
        
        

    print("C'est la fin")


