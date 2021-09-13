---
title: 'Divisibilité, congruence'
created: '2021-09-08T12:26:49.531Z'
modified: '2021-09-10T13:46:14.858Z'
---

#  Divisibilité, congruence

## Tex 
$\exist$ = exist (exsiste)
$\forall$ = forall (pour tout)

## I) Arithmétique, règles du jeu

L'arithmetique est l'étude des nombres entiers

L'ensembles des entiers est noté $\Z$

Les entiers positifs sont appeléss des entiers naturels.
L'ensembles des entiers naturels est noté $\N$

On admet les règles suivantes
  - La somme, la différence, le produits de deux entiers est un entier
  - Si $a \in \Z$ et $n \in \N$, alors $a^n \in \Z$
  - Toute partie non vide de $\N$ admet un plus petit élément
  - On notera $[[a;b]]$ l'intervale d'entiers allant de a à b $(a < b)$
  - Ici, a et b sont 2 entiers, et $[[a;b]] = [a;b] \cap \Z$
    - Exemple $[[3;7]] = {3,4,5,6,7}$
  - On definit de la meme façon $]]a;b[[, [[a;b[[, ]]a;b]].$
  
## II) Divisibilité

### 1) Définition

a et b étant deux entiers, on dit que $a$ divise $b$, si il exsiste un entier $k$ tel que $b = ka$. On écrit alors $a|b$

$a|b (1) \exist k\in \Z, b=ka$

Cela se formule également de la façon suivante:
  - a est un <u>diviseur</u> de b
  - b est un <u>multiple</u> de a

### 2) Propriétes

Soit 
$n \in \Z,$ on a $n= 1*n$ donc $1|n$ et $n|n$
$n=-1*(-n)$ donc $-1|n$ et $-n|n$

$\forall k \in \Z$, on a $0=0*k$
<u>Tout les entiers divisent 0</u>

On admet le résultat suivant (voir preuve en exercice)
Tout entier non nul admet un nombre fini de diviseur
Si $n \in \Z^*$ et d est un divieur de n, alors $d \in [[ -|n|; |n|]]$

Par la suite, on notera $D(n)$ l'ensembe des diviseurs de n
Exemple: $D(6) = \{-6;-3;-2;-1;1; 2; 3; 6\}$

Transitivité: a,b et c etant 3 entiers, si $a|b$ et $b|c$ alors $a|c$

Preuve:
$a|b$, donc $\exist k \in \Z, b=ka$
$b|c$, donc $\exist k' \in \Z, c=k'b$
On a alors $c = k'*(ka) = (k'k)*a$;
$k'k \in \Z$, donc $a|c$

---
Prof: 
a,b et n étant 2 entiers monterer que si n|a et n|b alors n|(a+b)
