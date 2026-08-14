# Blueprint Formel : Régularité Globale des Équations de Navier-Stokes en 3D

## 1. Énoncé Formel
Pour un fluide incompressible visqueux dans $\mathbb{R}^3$ soumis à une viscosité $\nu > 0$ et une donnée initiale lisse à divergence nulle $u_0 \in C^\infty(\mathbb{R}^3)$ avec $\nabla \cdot u_0 = 0$ et $\int_{\mathbb{R}^3} |u_0|^2 dx < \infty$ :
$$\partial_t u + (u \cdot \nabla) u = -\nabla p + \nu \Delta u$$
$$\nabla \cdot u = 0$$
Existe-t-il une solution lisse globale $u \in C^\infty(\mathbb{R}^3 \times [0, \infty))$ à énergie bornée $\sup_{t \ge 0} \int |u|^2 dx < \infty$ ?

## 2. Déconstruction des Barrières
1. **Échelle Critique et Invariance d'Échelle :** L'équation est invariante sous $u(x,t) \mapsto \lambda u(\lambda x, \lambda^2 t)$. L'énergie $L^2$ est sous-critique en 2D (garantissant la régularité globale), mais strictement sur-critique en 3D.
2. **Critère de Beale-Kato-Majda (BKM 1984) :** Une solution forte explose au temps $T^*$ si et seulement si :
   $$\int_0^{T^*} \|\omega(\cdot, t)\|_{L^\infty} dt = \infty, \quad \omega = \nabla \times u$$
3. **Obstacle de Tao (Modèles d'explosion par blow-up auto-similaire) :** Terence Tao (2016) a démontré l'existence de blow-up en temps fini pour des équations non linéaires moyennées respectant la conservation d'énergie de Navier-Stokes.

## 3. Analyse Critique de l'Ébauche Précédente
* **Faiblesse identifiée :** L'affirmation que l'incompressibilité $\operatorname{Tr}(S) = 0$ force un "frein géométrique automatique" par réalignement de vorticité n'était pas démontrée comme une inégalité a priori uniforme.
* **Redressement Méthodologique :** Formaliser en Lean 4 les solutions faibles de Leray-Hopf, la formule de Biot-Savart, et l'espace de Sobolev critique $\dot{H}^{1/2}(\mathbb{R}^3)$.

## 4. Graphe de Décomposition Modulaire (Lean 4)
- [ ] Définition des espaces de Sobolev $H^s(\mathbb{R}^3)$ et des champs solénoïdaux $L^2_\sigma$.
- [ ] Formalisation de l'inégalité d'énergie de Leray-Hopf.
- [ ] Formalisation du lemme de Grönwall appliqué au critère BKM.
- [ ] Dérivation des estimations locales d'énergie de Caffarelli-Kohn-Nirenberg (dimension de Hausdorff singulière $\le 1$).
