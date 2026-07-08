# La Conjecture de Hodge

Dossier dédié à l'investigation et à la résolution de la **Conjecture de Hodge**.

---

## 🔗 Ressources et Documents
| Document | Description |
| :--- | :--- |
| [**Tableau de Bord**](../dashboard.md) | Suivi général de l'avancement des problèmes du millénaire. |
| [**Notes de Recherche**](notes.md) | Synthèse des barrières et des pistes formelles. |

---

## 1. Présentation du Problème

La conjecture de Hodge est une question majeure de géométrie algébrique complexe et de topologie algébrique. Elle établit un pont entre la topologie d'une variété algébrique complexe projective lisse et sa géométrie algébrique sous-jacente.

Soit $X$ une variété algébrique complexe, lisse et projective. $X$ peut être vue comme une variété kählérienne compacte. La cohomologie de de Rham à coefficients complexes $H^r(X, \mathbb{C})$ admet la décomposition de Hodge :
$$H^r(X, \mathbb{C}) = \bigoplus_{p+q=r} H^{p,q}(X)$$
où $H^{p,q}(X)$ est le sous-espace représenté par les formes différentielles de type $(p,q)$ (contenant $p$ différentielles de type $dz$ et $q$ de type $d\bar{z}$).

Soit $H^{2k}(X, \mathbb{Q})$ la cohomologie rationnelle de degré $2k$. Les **classes de Hodge** de degré $2k$ sont définies comme l'intersection :
$$\operatorname{Hdg}^k(X) = H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X)$$

Par ailleurs, toute sous-variété algébrique fermée $Y \subset X$ de codimension $k$ définit une classe de cohomologie fondamentale $[Y] \in H^{2k}(X, \mathbb{Z})$ qui, après projection sur $\mathbb{Q}$, appartient à $\operatorname{Hdg}^k(X)$. Une combinaison linéaire rationnelle de telles classes de sous-variétés est appelée un **cycle algébrique rationnel**.

La conjecture de Hodge s'énonce ainsi :
> **Conjecture :** Sur une variété algébrique projective lisse complexe $X$, toute classe de Hodge est une combinaison linéaire rationnelle de classes de cycles algébriques :
> $$\operatorname{Hdg}^k(X) = \operatorname{Span}_{\mathbb{Q}} \{ [Y] \mid Y \subset X \text{ sous-variété de codimension } k \}$$

---

## 2. Obstacles et Résultats Fondamentaux (Les Barrières)

### A. Le Théorème de Lefschetz (1,1)
Démontré par Solomon Lefschetz, la conjecture est vraie pour $k=1$ (codimension 1, c'est-à-dire les diviseurs).
* **Le verrou :** Pour $k > 1$, la correspondance entre les faisceaux analytiques cohérents et les diviseurs algébriques s'estompe, et il n'y a plus de relation directe simple via l'exponentielle de faisceaux ($0 \to \mathbb{Z} \to \mathcal{O}_X \to \mathcal{O}_X^* \to 0$).

### B. Le Contre-exemple d'Atiyah-Hirzebruch (Barrière Entière)
La conjecture de Hodge est fausse si l'on remplace les coefficients rationnels $\mathbb{Q}$ par des coefficients entiers $\mathbb{Z}$. Atiyah et Hirzebruch (1961) ont construit des variétés projectives lisses possédant des classes de cohomologie entière de type $(k,k)$ qui ne peuvent pas être représentées par des cycles algébriques entiers en raison d'obstructions de torsion topologiques (opérations de Steenrod).
* **Conséquence :** Toute preuve doit fondamentalement exploiter la structure rationnelle $\mathbb{Q}$ et annuler ou contourner la torsion.

### C. La Barrière Transcendante (Analytique vs Algébrique)
Les classes de Hodge sont définies par des formes différentielles (qui dépendent de la structure complexe analytique de $X$), tandis que les cycles de Hodge doivent être construits algébriquement (via des équations polynomiales). Le passage du transcendant à l'algébrique requiert le contrôle des équations de Picard-Fuchs et de la locus de Hodge.

---

## 3. Stratégies et Programme de Recherche

Pour démontrer la conjecture, nous suivrons les axes de recherche suivants :

1. **Axe 1 : Faisceaux Cohérents et Complexes de Hochschild-Mitchell**
   Transposer les cycles algébriques en termes de complexes d'objets dans la catégorie dérivée des faisceaux cohérents $D^b(X)$. Les classes de Hodge seront identifiées à des classes de Chern d'objets parfaits, traduisant le problème topologique en un problème d'existence d'objets dans la catégorie dérivée.
   
2. **Axe 2 : Les Courants de Hodge et Analyse Kählérienne**
   Utiliser la théorie des courants de Lelong et l'équation de Monge-Ampère complexe pour régulariser les formes de Hodge et reconstruire des sous-variétés algébriques singulières à partir de courants fermés positifs.
   
3. **Axe 3 : La Dualité d'Amitsur et Invariants de Grothendieck**
   Formuler la conjecture de Hodge comme l'évanouissement d'une classe d'obstruction de Hochschild-Mitchell pour des foncteurs de réalisation motiviques.
