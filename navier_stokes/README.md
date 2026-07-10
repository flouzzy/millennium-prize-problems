# Les Équations de Navier-Stokes (Existence et Lissité)

Dossier dédié à l'investigation et à la résolution du problème des **Équations de Navier-Stokes** en 3D.

---

## 🔗 Ressources et Documents

| Document | Description |
| :--- | :--- |
| [**Tableau de Bord**](../dashboard.md) | Suivi général de l'avancement des problèmes du millénaire. |
| [**Notes de Recherche**](notes.md) | Synthèse des barrières et des pistes formelles. |

---

## 1. Présentation du Problème

Les équations de Navier-Stokes décrivent le mouvement des fluides visqueux incompressibles. En dimension 3 ($\mathbb{R}^3$), pour un fluide homogène de densité constante et de viscosité cinématique $\nu > 0$, les équations s'écrivent :
$$\partial_t u + (u \cdot \nabla) u = -\nabla p + \nu \Delta u + f$$
$$\nabla \cdot u = 0$$
avec la condition initiale $u(x,0) = u_0(x)$, où :

* $u(x,t) \in \mathbb{R}^3$ est le champ de vitesse du fluide.
* $p(x,t) \in \mathbb{R}$ est la pression.
* $f(x,t) \in \mathbb{R}^3$ est la force extérieure appliquée.
* $\nabla \cdot u_0 = 0$.

Le problème du prix du millénaire demande de prouver l'une des deux assertions suivantes (en supposant $f = 0$ ou $f$ lisse et à décroissance rapide) :

1. **Existence et lissité globale (cas affirmatif) :** Pour toute donnée initiale $u_0 \in C^\infty(\mathbb{R}^3)$ de divergence nulle et à décroissance rapide, il existe des fonctions lisses $u, p \in C^\infty(\mathbb{R}^3 \times [0, \infty[)$ satisfaisant les équations.
2. **Explosion en temps fini (cas négatif / Blow-up) :** Il existe une donnée initiale lisse $u_0$ et une force $f$ lisse telles que la solution unique locale perd sa lissité à un temps fini $T^* < \infty$ (explosion de la norme ou de la vorticité).

---

## 2. Obstacles et Résultats Fondamentaux (Les Barrières)

Toute tentative de résolution globale doit s'accorder avec les verrous et les limites physiques/mathématiques suivants :

### A. Solutions Faibles de Leray-Hopf (1934)

Jean Leray et Eberhard Hopf ont démontré l'existence globale de solutions faibles (dans l'espace d'énergie $L^\infty(0, T; L^2) \cap L^2(0, T; H^1)$) pour toute donnée initiale d'énergie finie.

* **Le verrou :** On ne sait pas si ces solutions faibles sont uniques, ni si elles restent lisses en dimension 3.

### B. Le Critère de Beale-Kato-Majda (BKM, 1984)

Une solution forte locale $u$ sur $[0, T^*[$ perd sa régularité au temps $T^*$ si et seulement si la norme $L^\infty$ de la vorticité $\omega = \nabla \times u$ n'est pas intégrable en temps :
$$\int_0^{T^*} \|\omega(\cdot, t)\|_{L^\infty} dt = \infty$$

* **Conséquence :** L'analyse doit se focaliser sur le contrôle de la vorticité et de son étirement (*vortex stretching*).

### C. La Barrière des Équations Moyennées (Terence Tao, 2016)

Terence Tao a construit une version modifiée ("moyennée") des équations de Navier-Stokes qui conserve l'énergie et possède la même structure d'échelle, mais qui explose en temps fini.

* **Conséquence :** Les arguments purement basés sur l'analyse harmonique classique, les estimations d'énergie standard (type Sobolev) ou les lois d'échelle ne suffisent pas pour prouver la régularité globale. Toute preuve de l'existence globale doit exploiter la géométrie exacte de l'advection non linéaire $(u \cdot \nabla) u$ (notamment le fait que le terme non linéaire est orthogonal à la vitesse).

### D. Le Théorème de Caffarelli-Kohn-Nirenberg (CKN, 1982)

Ce théorème montre que la dimension de Hausdorff de l'ensemble singulier (dans l'espace-temps) d'une solution faible convenable est au plus 1.

* **Conséquence :** Si des singularités existent, elles sont extrêmement localisées (par exemple, des filaments ou des points singuliers isolés dans le temps).

---

## 3. Stratégies et Programme de Recherche

Nous allons structurer notre recherche selon les axes suivants :

1. **Axe 1 : Analyse Géométrique de la Vorticité et de l'Étirement du Vortex**
   Étudier l'équation de transport de la vorticité $\partial_t \omega + (u \cdot \nabla) \omega = (\omega \cdot \nabla) u + \nu \Delta \omega$. Le terme de vortex stretching $(\omega \cdot \nabla) u$ est la source potentielle d'explosion. Nous analyserons les contraintes géométriques imposées par l'incompressibilité ($\nabla \cdot u = 0$) sur l'orientation de $\omega$.

2. **Axe 2 : Modélisation Énergétique et Obstructions Algébriques de Tao**
   Comprendre comment le transfert d'énergie vers les hautes fréquences (la cascade d'énergie de Kolmogorov) est tempéré par la dissipation visqueuse $\nu \Delta u$.

3. **Axe 3 : Régularité Globale via les Espaces de Besov et Estimations de Dérive**
   Utiliser des méthodes d'analyse harmonique fine (estimations bilinéaires dans les espaces de Besov critiques ou de Morrey-Campanato) pour contrôler le flux d'énergie.
