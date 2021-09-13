---
title: Raisinoment par récurence
created: '2021-09-07T06:19:20.025Z'
modified: '2021-09-12T21:12:34.040Z'
---

# Raisinoment par récurence

## Tex Help
$$
\left
\{
  \begin{array}
    {rcr}x+2y & = & -1 \\
    -x+4y & = & 0 \\
    -x+4y & = & 0 \\
  \end{array}
\right.$$

## 1) Principe

On donne une propriété qui depends d'un entier naturel n notée P(n)
On veut montrer que cette propriété est vraie pour tout entier naturel n
On pourra le démontrer de la façon suivante
INITIALATION: on montre que la propriété est VRAIE pour n = 0
Et
HéréDITé: On montre que poun tout entier naturel n;
  - Si $P(n)$ est VRAIE
  - Alors $P(n+1)$ est VRAIE

On poura affirmer selon le principe de raisonnement par récurrance, pour tout entier naturel naturel n, P(n) est VRAI

## 2) Exemple

Exemple N°1:

$(u_n) = \{ u_0=600, pour \;u_n+1 = 0,85u_n + 300$

Démonterer en utilisant le raisonement par récurence pour tout n $\in \N$, $u_n=-1400*0,85^n+2000$

<u>Notation</u> : Soit n $\in \N$, on note P(n) : **$"u_n=-1400*0,85^n+2000"$**

<u> INITIALISATION: </u> on montre que P(o) est *VRAIE*
On sait que $u_n = 600$

on calcule: $u_0=-1400*0,85^0+2000 =-1400*1+2000 = 600$
On a prouvé que $u_0 = -1400*0,85⁰+2000$

<u>BILAN</u>: P(0) est *VRAIE*

<u>HéRéDITé</u>: Soit $n \in \N$

Hypothèse de récurence: $u_n=-1400*0,85^n+2000$ 
Conclustion$_\text{ce que on doit démonter}$: $u_{n+1} = -1400*0,85^{n+1}+2000$  

<u>PREUVE</u>: D'apres la relation de récurence $u_{n+1} = 0,85^{u_n} + 300$

D'apres l'hypothese de récurence
$u_n =  -1400*0,85^{n}+2000$

Donc:  $u_{n+1} = 0,85*(-1400*0,85^{n}+2000) + 300$
Soit: $u_{n+1} = 0,85*(-1400*0,85^{n})+0,85*2000 + 300$
Soit: $u_{n+1} = -1400*0,85^{1}0,85^n + 1700 +300$
Soit: $u_{n+1} = -1400*0,85^{n+1} + 2000$
**C'est ce que l'on devait démonterer**

<u>BILAN</u>: D'apres le princepe de raisement par récurrence pour tout $n \in \N$, P(n) est *VRAIE*


Exemple N°2: Inégalité de BERNOULLI

$Soit\;a \in ]0; + \infin[$
On a pour tout $n \in \N: (1+a)^n \ge 1+na$
On pose pour $n \in \N P(n): "(1+a)^n \ge 1+na"$

On doit donc montrer que $(1+a)⁰ \ge 1+0*a$
Or $(1+a)⁰ = 1\; et \;1+0*a = 1 \;et \;1>1 \;on\; a: (1+a)⁰ 1+0*a$


Hérédité: Soit $n \in \N$

Hypothèse de récurence **HR** : $(1+a)^n \ge 1+na$
Conclustion          **CCL** : $(1+a)^{n+1} \ge 1+(n+1)a$

Preuve:
On rappelle que $X^{n+1} = X*X^n$

On a : $(1+a)^{n+1} = (1+a)*(1*a)^n$

Sachant que a $\in ]0; +inf[\;;0<1+a$
D'apres l'hypothèse de récurence:
$(1+a)^n \ge 1+na$
Comme 1+a est positif on garde le sens de l'inégalité

Donc : $(1+a)*(1+a)^n \ge 1+na*(1+a)$      *(1)*
 CAR $(1+a) \ge 0$

Or:  $(1+a)*(1+a)^n = (1+a)^{n+1}$
ET $1+na*(1+a) = 1+na+a+na²$

Soit $(1+a)(1+na) = 1+(n+1)a+na²$
or $na² \ge 0$ donc $(1+a)(1+na)\ge 1+(n+1)a$    *(2)*


En utilisant: (1) et (2)

$(1+a)^{n+1} \ge (1+a)(1+na)$
et: $(1+a)(1+na) \ge 1+(n+1)a$

Donc: $(1+a)^{n+1} \ge 1+(n+1)a$    *CQFD*

**Bilan: pour tout n \in \N, P(n) est *VRAIE* d'apres le principe de raisonement par récurrence**

---

### 3) Autre cas pratique

Dans certains cas, on doit démonterer que la propriété est VRAI a partir d'un certain rang: c'est à dire un entier naturel $n_0$ tel que pour tout n $\ge n_0$, P(n) est VRAIE

Dans ce cas l'initalisation consiste à verifier que $P(n_0)$ est *VRAIE* et que l'hérédité en indiquant cepandant: pour $n \in \N$, tel que $n \ge n_0$

n_0 est un entier naturel

---

### 4) Principe de récurrence double

a) exemple: $(u_n): \{ u_0=1; u_1 =2, \text{pour tout} n \in \N, u_{n+2} = u_{n+1} + 2u_n$

1) Calculer u_2

<span color="green">Dans la relation de récurrence on remplace n=0</span>, $u_2 = u_n+2u_0 = 2+2*1 = 4$ 

<u>$u_2 = 4$</u>

2) Démontrer que: pour tout $n \in \N, u_n = 2^n$

On pose pour $n \in \N, P(N) : "u_n = 2^n"$

INITIALISATION: on montre que P(0) ET P(1) sont VRAIES

EN effet: u_0 = 2⁰ = 1 et u_1 = 2 = 2^1

.
.
.
.
.
.
.
.


.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.


