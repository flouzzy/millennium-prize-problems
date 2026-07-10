# Notes de Recherche : Synthèse Littéraire et Modélisation Topologique de 3SAT

Ce document présente l'état de l'art de la recherche sur le problème **P vs NP** (2025-2026) et établit les fondements de notre modèle géométrique de **3SAT** via la théorie des arrangements de sous-espaces.

---

## Partie I : Synthèse de la Littérature Récente (2025-2026)

L'investigation moderne de $\mathbf{P}$ vs $\mathbf{NP}$ s'est polarisée autour de plusieurs approches novatrices visant à contourner les barrières classiques de relativisation, d'algébrisation et de naturalité.

### 1. L'Approche Homologique et Topologique (Jian-Gang Tang, 2025)

* *Papier clé :* `arXiv:2510.17829` - *A Homological Separation of $\mathbf{P}$ from $\mathbf{NP}$ via Computational Topology and Category Theory*.
* *Concept :* L'auteur tente de définir des foncteurs de la catégorie des algorithmes polynomiaux vers des catégories algébriques stables (comme les groupes de cohomologie ou d'homotopie). L'idée est de montrer que la vérification d'une solution de $\mathbf{NP}$ possède un invariant homologique non nul (une classe d'obstruction) qui ne peut pas s'annuler dans le sous-espace associé à $\mathbf{P}$.
* *Statut & Limites :* Bien que l'utilisation de la topologie computationnelle soit prometteuse pour contourner la barrière de relativisation, cette tentative spécifique a été critiquée pour des imprécisions majeures dans les définitions et des faiblesses dans le processus de vérification formelle. Elle souligne néanmoins le besoin d'outils géométriques globaux.

### 2. Le Modèle de l'Observateur et le Rang SPDP (Darren J. Edwards, 2025)

* *Papier clé :* `arXiv:2512.11820` - *Toward $\mathbf{P}$ vs $\mathbf{NP}$: An Observer-Theoretic Separation via SPDP Rank*.
* *Concept :* Edwards propose d'étudier la complexité via le rang des polynômes de dérivées partielles décalées (SPDP - Shifted Partial Derivative Polynomial). Cette mesure algébrique permet de quantifier la complexité de fonctions polynomiales en mesurant la dimension de l'espace vectoriel engendré par leurs dérivées partielles sous des décalages polynomiaux.
* *Lien avec GCT :* C'est une variante de la Théorie Géométrique de la Complexité (GCT). Elle vise à prouver que le permanent d'une matrice (représentant $\mathbf{VNP}$) ne peut pas être projeté dans l'orbite du déterminant (représentant $\mathbf{VP}$) en raison d'une borne inférieure stricte sur le rang SPDP.

### 3. Approche par la Physique Statistique et les Tuiles de Wang (Canfora-Marco, 2026)

* *Papier clé :* `arXiv:2601.18968` - *Detecting the finer structure of the $\mathbf{P}$ vs $\mathbf{NP}$ problem with statistical mechanics*.
* *Concept :* Modélisation du problème NP-complet des pavages de Wang sous la forme d'un modèle de spin en physique statistique. L'existence d'un pavage valide équivaut à un état fondamental d'énergie nulle. En utilisant les équations de Schwinger-Dyson et les limites thermodynamiques, les auteurs étudient la transition de phase entre les instances satisfaisables et insatisfaisables, révélant une obstruction de type "gap d'énergie".

---

## Partie II : Modélisation Topologique de 3SAT par les Arrangements de Sous-espaces

Pour concevoir une preuve non relativisante et non naturelle, nous modélisons les formules propositionnelles de 3SAT sous la forme d'un **arrangement de sous-espaces linéaires** au sein d'une variété algébrique globale.

### 1. Construction de l'Espace des Phases

Soit $\Phi$ une formule 3SAT sur $n$ variables $x_1, \dots, x_n$ et $m$ clauses $C_1, \dots, C_m$. Soit $k$ un corps commutatif (par exemple $k = \mathbb{C}$ ou un corps fini $\mathbb{F}_q$).

Nous définissons l'espace vectoriel ambiant $V = (k^2)^n \simeq k^{2n}$.
Chaque variable $x_i$ est associée à un plan vectoriel $V_i = k^2$, dont les coordonnées sont notées $(u_i, v_i)$.

* L'état de vérité de la variable $x_i$ est encodé par une droite projective $\mathbb{P}(V_i) \simeq \mathbb{P}^1(k)$.
* Par convention, nous associons :
  * La valeur **VRAI** à la droite d'équation $u_i - v_i = 0$ (c'est-à-dire le point $[1 : 1] \in \mathbb{P}^1$).
  * La valeur **FAUX** à la droite d'équation $u_i = 0$ (c'est-à-dire le point $[0 : 1] \in \mathbb{P}^1$).

### 2. Encodage des Clauses comme des Sous-espaces

Une clause $C_j$ est une disjonction de trois littéraux, par exemple $C_j = x_1 \lor \neg x_2 \lor x_3$.
Une affectation des variables rend la clause $C_j$ **insatisfaite** si et seulement si tous ses littéraux sont faux. Pour notre exemple, cela correspond à l'unique configuration :
$$x_1 = \text{FAUX}, \quad x_2 = \text{VRAI}, \quad x_3 = \text{FAUX}$$

Nous traduisons cette configuration insatisfaisante sous forme d'équations linéaires dans $V$ :

1. $x_1 = \text{FAUX} \implies u_1 = 0$
2. $x_2 = \text{VRAI} \implies u_2 - v_2 = 0$
3. $x_3 = \text{FAUX} \implies u_3 = 0$

Ces équations définissent un sous-espace vectoriel linéaire $W_j \subset V$ de codimension 3 :
$$W_j = \{ (u, v) \in V \mid u_1 = 0, \ u_2 - v_2 = 0, \ u_3 = 0 \}$$

De manière générale, à chaque clause $C_j$ nous associons un sous-space linéaire $W_j \subset V$ de codimension 3.

### 3. L'Arrangement de Sous-espaces $\mathcal{A}_{\Phi}$

La formule complète $\Phi$ est satisfaite par une affectation si et seulement si cette affectation n'annule aucune clause.
L'ensemble de toutes les affectations insatisfaisantes pour la formule globale est l'union des sous-espaces $W_j$.
L'arrangement de sous-espaces associé à la formule $\Phi$ est la collection :
$$\mathcal{A}_{\Phi} = \{W_1, W_2, \dots, W_m\}$$

Le lieu des affectations satisfaisantes est le **complémentaire de l'arrangement** :
$$U_{\Phi} = V \setminus \bigcup_{j=1}^m W_j$$

Le problème 3SAT se reformule alors de manière purement géométrique :
> **Théorème :** La formule 3SAT $\Phi$ est satisfaisable si et seulement si le complémentaire de l'arrangement associé est non vide :
> $$U_{\Phi} \neq \emptyset$$

### 4. Obstruction Topologique par la Cohomologie de Goresky-MacPherson

Pour analyser la satisfaisabilité de manière globale, nous utilisons le théorème de Goresky-MacPherson qui calcule la cohomologie singulière (ou étale) du complémentaire $U_{\Phi}$.

Soit $L(\mathcal{A}_{\Phi})$ le poset (ensemble partiellement ordonné) des intersections des sous-espaces de $\mathcal{A}_{\Phi}$, ordonné par l'inclusion inverse, avec $\hat{0} = V$. Pour tout sous-espace d'intersection $X \in L(\mathcal{A}_{\Phi})$, nous notons $d(X)$ sa dimension.

Le théorème de Goresky-MacPherson stipule que pour tout entier $i$ :
$$\widetilde{H}^i(U_{\Phi}, \mathbb{Q}) \simeq \bigoplus_{X \in L(\mathcal{A}_{\Phi}) \setminus \{\hat{0}\}} \widetilde{H}_{2n - d(X) - i - 2}(\Delta(\hat{0}, X), \mathbb{Q})$$
où $\Delta(\hat{0}, X)$ désigne le complexe simplicial ordonné de l'intervalle $(\hat{0}, X)$ dans le poset $L(\mathcal{A}_{\Phi})$.

### 5. Conséquence pour la complexité

Si $\mathbf{P} = \mathbf{NP}$, il existerait un algorithme polynomial capable de décider si $U_{\Phi} \neq \emptyset$. Or, la topologie du complémentaire (notamment ses nombres de Betti $b_i = \dim H^i(U_{\Phi})$) est intrinsèquement liée à la structure combinatoire extrêmement complexe du poset d'intersection $L(\mathcal{A}_{\Phi})$.
La détection de l'existence d'une section globale dans $U_{\Phi}$ équivaut à la non-trivialité de l'homologie du poset.

* **Notre axe de preuve :** Nous allons chercher à démontrer que la structure cohomologique du poset $L(\mathcal{A}_{\Phi})$ pour des formules insatisfaisables forme une famille d'obstructions géométriques (des cycles cohomologiques de torsion) dont la détection requiert un nombre d'opérations algébriques qui croît de manière exponentielle par rapport au nombre de variables $n$, interdisant ainsi l'existence d'un algorithme polynomial global.
