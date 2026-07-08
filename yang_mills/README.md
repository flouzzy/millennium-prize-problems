# Les Équations de Yang-Mills (Existence et Gap de Masse)

Dossier dédié à l'investigation et à la résolution du problème des **Équations de Yang-Mills et du Gap de Masse** en 4D.

---

## 🔗 Ressources et Documents
| Document | Description |
| :--- | :--- |
| [**Tableau de Bord**](../dashboard.md) | Suivi général de l'avancement des problèmes du millénaire. |
| [**Notes de Recherche**](notes.md) | Synthèse des barrières et des pistes formelles. |

---

## 1. Présentation du Problème

La théorie de Yang-Mills classique est une généralisation non-abélienne de l'électromagnétisme de Maxwell, décrivant les interactions fortes et faibles entre particules élémentaires.
Soit $G$ un groupe de Lie compact, simple et connexe (le groupe de jauge, ex. $SU(3)$) et $\mathfrak{g}$ son algèbre de Lie. Une théorie de jauge classique sur l'espace-temps $\mathbb{R}^4$ est définie par une 1-forme de connexion $A$ à valeurs dans $\mathfrak{g}$. La courbure (ou champ de force) associée est la 2-forme $F = dA + A \wedge A$. L'action de Yang-Mills s'écrit :
$$S(A) = \frac{1}{2g^2} \int_{\mathbb{R}^4} \operatorname{Tr}(F \wedge *F)$$
où $g > 0$ est la constante de couplage et $*$ désigne l'opérateur étoile de Hodge.

Le problème du millénaire posé par l'Institut Clay demande de démontrer deux assertions fondamentales :
1. **Existence globale (axiomatique) :** Établir l'existence d'une théorie quantique des champs de Yang-Mills non-abélienne rigoureuse sur l'espace-temps de Minkowski $\mathbb{R}^4$, satisfaisant un ensemble d'axiomes standard comme les axiomes de Wightman ou d'Osterwalder-Schrader.
2. **Gap de masse (Mass Gap) $\Delta > 0$ :** Démontrer que le spectre du Hamiltonien quantique de la théorie possède un gap d'énergie strictement positif au-dessus de l'état fondamental (le vide). C'est-à-dire que la masse de la particule la plus légère de la théorie est strictement positive ($m \ge \Delta > 0$), bien que le lagrangien classique ne contienne aucun paramètre de masse.

---

## 2. Obstacles et Résultats Fondamentaux (Les Barrières)

### A. La Barrière non-perturbative et la Liberté Asymptotique
Découverte par Gross, Wilczek et Politzer, la liberté asymptotique indique que le couplage efficace $g(\mu)$ tend vers 0 à haute énergie (courtes distances). Cependant, à basse énergie (grandes distances), le couplage diverge :
$$\lim_{\mu \to 0} g(\mu) = \infty$$
* **Le verrou :** À cause de cette divergence infrarouge (IR), les méthodes de perturbation (diagrammes de Feynman) échouent complètement pour étudier le gap de masse et le confinement des couleurs. L'analyse doit être strictement non-perturbative.

### B. Les Limites de la Théorie des Champs Constructive
La théorie constructive a réussi à définir rigoureusement des théories quantiques en dimension 2 et 3, ainsi que des théories scalaires (comme $\phi^4$) avec troncature en dimension 4.
* **Le verrou :** En dimension 4, les divergences ultraviolettes (UV) sont sévères (renormalisation requise) et le groupe de jauge non-abélien introduit des contraintes géométriques (l'espace des connexions modulo l'action du groupe de jauge, $\mathcal{A}/\mathcal{G}$, est de dimension infinie et possède des singularités de Gribov).

### C. La Limite du Continu à partir du Réseau (Wilson, 1974)
La formulation sur réseau de Kenneth Wilson discrétise l'espace-temps sur une grille, fournissant un régulateur UV naturel et permettant de démontrer l'existence d'un gap de masse à couplage fort.
* **Le verrou :** Prendre la limite mathématique du continu (quand le pas du réseau $a \to 0$) de manière à préserver la covariance de Lorentz et la liberté asymptotique reste le cœur de la difficulté mathématique.

---

## 3. Stratégies et Programme de Recherche

Pour surmonter ces verrous, nous allons suivre les axes stratégiques suivants :

1. **Axe 1 : Géométrisation du Vide Quantique via l'Espace des Connexions $\mathcal{A}/\mathcal{G}$**
   Étudier la topologie de l'espace quotient $\mathcal{A}/\mathcal{G}$ et les copies de Gribov. Le vide quantique doit être modélisé comme une mesure de probabilité géométrique stable sur l'espace des orbites de jauge.
   
2. **Axe 2 : Flot de Renormalisation non-perturbatif et Estimations Infrarouges**
   Utiliser les équations du flot de renormalisation (Polchinski / Wetterich) pour contrôler l'évolution de la mesure de jauge des échelles UV vers les échelles IR.
   
3. **Axe 3 : Modélisation Algébrique du Gap de Masse par des Invariants Cohomologiques**
   Formuler le gap de masse comme une obstruction cohomologique à l'existence d'états d'énergie nulle excités dans l'algèbre des opérateurs locaux (champs de Wilson/Polyakov).
