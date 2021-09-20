---
title: 'Divisibilité, congruence'
created: '2021-09-08T12:26:49.531Z'
modified: '2021-09-15T13:01:42.502Z'
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
$a \in \Z^*, b \in \Z^*$ Montrer que si $a|b$ et $b|a$ alors $|a| = |b|$

On considère 2 entiers a  et b non null tels que $a|b$ et $b|a$ 
On a alors 
$\exist k \in \Z, b = ka$
$\exist k' \in \Z, a = k'b$

on a alors $a = k'*ka = kk'a$
$kk'a - a = 0$
$(kk'-1) * a = 0$
$kk'-1= 0$ ou $a =0$


On sait que $a \neq 0$
in a donc $kk' = 1$

k et k' sont des diviseur de 1, ils ne peuvent prendre pour valeur que 1 ou -1

si $k=1$: $b=a$
si $k=-1$: $b= -a$

$a \in \Z^*, b \in \Z^*, a|b\text{ et }b|a \Rightarrow |a| = |b|$

---
## II) Ensemble $n\Z$

n n'etant un entier, on note $n\Z$ l'ensemble des multiples de n.
$n\Z = \{ kn, k\in\Z\}$
De façon immédiate, si $a \in n\Z$, alors $\exist k \in \Z, a = kn \Leftrightarrow n|a$
$a|n\Z \Leftrightarrow n|a$

Stabilité:

Si $a \in n\Z$ <=> $n|a$ <=> $\exist k \in \Z$, a = kn
Si $b \in n\Z$ <=> $n|b$ <=> $\exist k' \in \Z$, b = k'n

on a alors
a+b = kn+k'n = (k+k')n
Donc a+b \in n\Z

Cela s'écrit de 2 façon differentes

$$
n|a\; et\; n|b \Rightarrow n|(a+b) \\
a \in n\Z \text{ et } b \in n\Z \Rightarrow  a+b \in n\Z
$$

SI $a \in n\Z$ et $k \in \Z$

$\exist k' \in \Z$, a $k'n$ donc

$ka = kk'$ donc $ka \in n\Z$

Cela s'écrit de deux daçons differantes


$$
n|a\; et\; k\in Z \Rightarrow n|ka \\
a \in n\Z \text{ et } b \in \Z \Rightarrow  ka \in n\Z
$$

Combinaison linéaire

a et b etant 2 entier tout entier de la forme ka + k'b, à k \in \Z et k'\in \Z, est une combinaision linéaire de a et b

---

si $a\in n\Z, b\in n\Z, k \in \Z, k' \in \Z$ alors $ka + k'b \in n\Z$

$n\Z$ est stable par combinaison linéaire
Cela s'écrit aussi:
$n|a, n|b, k\in\Z, k'\in\Z \Rightarrow n|(ka+k'b)$
$a\in\Z^*,b \in \Z^*$
$a|b \Leftrightarrow b\Z \sub a\Z$

Preuve:
Soit $n\in k\Z$, alors $b|n$ or $a|b$, donc par **transitivité** $a|n \Rightarrow n \in a\Z$ 
Ceci étant vrai pout tout n de $k\Z$, on a donc $b\Z \sub a\Z$

*Réciproque:*
Si $b\Z \sub a\Z$
Or $b \in b\Z$, donc $b\in a\Z$, donc $a|b$

