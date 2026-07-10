# Problème P vs NP (P ≠ NP)

Dossier dédié à l'investigation et à la résolution du problème **P vs NP**.

---

## 🔗 Ressources et Documents

| Document | Description |
| :--- | :--- |
| [**Tableau de Bord**](../dashboard.md) | Suivi général de l'avancement des problèmes du millénaire. |
| [**Notes de Recherche**](notes.md) | Synthèse des barrières et des pistes formelles. |

---

## 1. Présentation du Problème

Le problème **P vs NP** est l'une des questions ouvertes les plus fondamentales de l'informatique théorique et des mathématiques contemporaines. Posé formellement par Stephen Cook en 1971, il cherche à déterminer si toute question dont la réponse peut être vérifiée rapidement (en temps polynomial) peut également être résolue rapidement.

### Les Classes de Complexité

1. **La classe $\mathbf{P}$ (Polynomial time) :**
   La classe des langages de décision décidables par une machine de Turing déterministe en temps polynomial par rapport à la taille de l'entrée $n$. Autrement dit, il existe un algorithme efficace pour résoudre le problème.
   $$\mathbf{P} = \bigcup_{k \ge 1} \mathbf{TIME}(n^k)$$

2. **La classe $\mathbf{NP}$ (Nondeterministic Polynomial time) :**
   La classe des langages de décision décidables par une machine de Turing non déterministe en temps polynomial. Équivalemment, c'est la classe des problèmes pour lesquels une solution candidate peut être vérifiée en temps polynomial par une machine de Turing déterministe.
   $$\mathbf{NP} = \bigcup_{k \ge 1} \mathbf{NTIME}(n^k)$$

Le problème s'énonce simplement :
$$\mathbf{P} \overset{?}{=} \mathbf{NP}$$

La conjecture ultra-majoritaire de la communauté scientifique est que $\mathbf{P} \neq \mathbf{NP}$.

---

## 2. Les Obstacles Fondamentaux (Les Barrières)

Toute tentative de démonstration directe se heurte à trois barrières logiques et théoriques majeures démontrées dans la littérature scientifique. Un critère de validité absolu pour toute preuve est sa capacité à contourner simultanément ces trois barrières.

### A. La Barrière de Relativisation (Baker, Gill, Solovay, 1975)

La plupart des techniques de diagonalisation classique s'appliquent de manière identique en présence d'un oracle (un trou noir computationnel gratuit). Or, Baker, Gill et Solovay ont démontré qu'il existe deux oracles $A$ et $B$ tels que :
$$\mathbf{P}^A = \mathbf{NP}^A \quad \text{et} \quad \mathbf{P}^B \neq \mathbf{NP}^B$$

* **Conséquence :** Toute preuve de $\mathbf{P} \neq \mathbf{NP}$ doit être **non relativisante**, c'est-à-dire qu'elle doit exploiter des propriétés internes des machines de Turing déterministes qui cessent d'être vraies en présence d'un oracle.

### B. La Barrière des Preuves Naturelles (Razborov, Rudich, 1994)

La majorité des tentatives de preuve de $\mathbf{P} \neq \mathbf{NP}$ cherchent à minorer la taille des circuits booléens requis pour résoudre un problème de $\mathbf{NP}$ (comme SAT). Razborov et Rudich ont démontré que sous des hypothèses cryptographiques standard (existence de générateurs de nombres pseudo-aléatoires), aucune preuve "naturelle" ne peut établir de minoration super-polynomiale. Une preuve est dite naturelle si elle définit une propriété combinatoire des fonctions booléennes qui est :

1. **Large :** Possédée par une fraction suffisante de toutes les fonctions.
2. **Constructive :** Décidable en temps polynomial.

* **Conséquence :** Toute preuve par la complexité des circuits doit être **non naturelle** ou s'attaquer à des modèles de circuits non restreints par des propriétés larges et constructives.

### C. La Barrière d'Algébrisation (Aaronson, Wigderson, 2008)

Conçue pour analyser les techniques d'arithmétisation des protocoles interactifs (utilisées pour prouver $\mathbf{IP} = \mathbf{PSPACE}$), cette barrière montre que les arguments qui s'étendent aux oracles algébrisés ne peuvent pas séparer $\mathbf{P}$ de $\mathbf{NP}$.

* **Conséquence :** La preuve doit être **non algébrisante**.

---

## 3. Pistes et Stratégies Modernes

Pour franchir ces barrières, plusieurs directions de recherche avancées ont été proposées :

1. **La Théorie Géométrique de la Complexité (GCT - Geometric Complexity Theory) :**
   Initiée par Ketan Mulmuley et Milind Sohoni, elle reformule les questions de complexité computationnelle (notamment l'analogue algébrique de $\mathbf{P} \neq \mathbf{NP}$, à savoir la conjecture de Valiant $\mathbf{VP} \neq \mathbf{VNP}$) en termes de géométrie algébrique et de théorie des représentations des groupes de Lie. La séparation des classes se traduit par la non-inclusion d'orbites fermées de polynômes (ex. le permanent vs le déterminant).

2. **La Complexité Descriptive :**
   Basée sur le théorème de Fagin, elle caractérise les classes de complexité par la logique mathématique. Par exemple, $\mathbf{NP}$ correspond exactement aux propriétés exprimables en logique du second ordre existentielle ($\Sigma^1_1$). Le problème se ramène alors à prouver qu'une certaine propriété logique ne peut pas être formulée dans un fragment logique plus restreint.

3. **L'Analyse Algébrique Fine des Algorithmes et Algèbres d'Opérateurs :**
   Rechercher des obstructions topologiques ou spectrales dans les graphes de configuration des machines computationnelles, en s'inspirant de la théorie spectrale des graphes et de la géométrie non-commutative.

---

## 4. Programme de Recherche Actuel

Notre objectif est d'étudier la structure interne de $\mathbf{NP}$-complet (en prenant comme référence 3SAT) sous l'angle de la géométrie algébrique et de la théorie des représentations, afin d'identifier des obstructions non relativisantes et non naturelles.

* **Étape 1 :** Rédaction d'un état de l'art détaillé des obstacles combinatoires et algébriques.
* **Étape 2 :** Analyse de la structure locale des obstructions dans les représentations de carquois associées aux formules propositionnelles.
* **Étape 3 :** Modélisation d'un invariant géométrique non naturel pour séparer les classes.
