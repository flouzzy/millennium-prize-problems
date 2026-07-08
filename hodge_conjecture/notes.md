# Notes de Recherche : Synthèse Littéraire et Blueprint Cohomologique de Hodge

Ce document résume l'état de l'art (2025-2026) sur la conjecture de Hodge et pose les fondements mathématiques de notre analyse de la conjecture de Hodge via la catégorie dérivée des faisceaux cohérents et l'isomorphisme de Hochschild-Kostant-Rosenberg (HKR).

---

## Partie I : Synthèse de la Littérature Récente (2025-2026)

La conjecture de Hodge reste l'un des piliers les plus actifs de la géométrie algébrique complexe, avec des avancées marquantes récemment :

### 1. Preuve pour les Variétés de Weil OG6 (Floccari-Fu, 2025)
* *Résultat clé :* `arXiv:2504.13607` - Preuve de la conjecture de Hodge pour les classes de Weil sur les variétés abéliennes de Weil de dimension 4 en utilisant des variétés OG6 (O'Grady) singulières. Ce travail a été au cœur du Séminaire Bourbaki de janvier 2026 (Exposé n°1248).

### 2. Réfutation de la Conjecture de Hodge Entière (Engel et al., 2025)
* *Résultat clé :* `arXiv:2507.15704` - Réfutation de la conjecture de Hodge entière pour des variétés abéliennes génériques principalement polarisées de dimension $\ge 4$ via la géométrie tropicale et la théorie des matroïdes. Ce résultat confirme que les obstructions de torsion entière (Atiyah-Hirzebruch) sont structurelles et que seul le cadre rationnel $\mathbb{Q}$ est valide pour la conjecture générale.

### 3. Extension aux Singularités Rationnelles (Dan-Kaur, 2025)
* *Résultat clé :* `arXiv:2506.13220` - Extension du théorème de Lefschetz (1,1) au cadre des singularités de surface rationnelles en utilisant l'application de classe de cycle de Bloch-Gillet-Soulé.

---

## Partie II : Blueprint Mathématique : Catégorie Dérivée et Isomorphisme HKR

Notre programme de recherche vise à démontrer la conjecture de Hodge en traduisant les classes de Hodge rationnelles sous forme de classes de Chern d'objets (complexes parfaits) de la catégorie dérivée des faisceaux cohérents $D^b(X)$.

### 1. Le Groupe de Grothendieck $K_0(X)$ et le Caractère de Chern
Soit $X$ une variété algébrique projective lisse sur $\mathbb{C}$.
* Soit $D^b(X)$ la catégorie dérivée bornée des faisceaux cohérents sur $X$. Tout objet $\mathcal{E}^\bullet \in D^b(X)$ est quasi-isomorphe à un complexe parfait (un complexe borné de fibrés vectoriels lisses).
* Le groupe de Grothendieck $K_0(X)$ est engendré par les classes d'isomorphisme d'objets de $D^b(X)$.
* Le caractère de Chern $ch : K_0(X) \to H^{\text{even}}(X, \mathbb{Q})$ associe à tout complexe parfait $\mathcal{E}^\bullet$ ses classes de Chern :
  $$ch(\mathcal{E}^\bullet) = \sum_{k=0}^{\dim X} ch_k(\mathcal{E}^\bullet), \quad ch_k(\mathcal{E}^\bullet) \in H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X, \mathbb{C})$$

La conjecture de Hodge s'énonce de manière équivalente en K-théorie rationnelle :
> **Théorème :** La conjecture de Hodge est vraie pour $X$ si et seulement si l'application caractère de Chern induit un surjection :
> $$ch : K_0(X) \otimes \mathbb{Q} \twoheadrightarrow \bigoplus_{k} \operatorname{Hdg}^k(X)$$

### 2. Homologie de Hochschild et l'Isomorphisme HKR
Pour analyser le passage du transcendant à l'algébrique, nous utilisons la catégorie DG (différentielle graduée) des complexes parfaits $\operatorname{Perf}(X)$. L'homologie de Hochschild de cette catégorie $\mathrm{HH}_*(\operatorname{Perf}(X))$ est reliée à la géométrie de $X$ par l'**isomorphisme de Hochschild-Kostant-Rosenberg (HKR)** :
$$I_{\mathrm{HKR}} : \mathrm{HH}_n(\operatorname{Perf}(X)) \xrightarrow{\simeq} \bigoplus_{q-p=n} H^q(X, \Omega_X^p)$$

L'isomorphisme HKR décompose l'homologie de Hochschild en cohomologie de Dolbeault. Les classes de Hodge rationnelles de type $(k,k)$ correspondent exactement aux composantes diagonales $H^k(X, \Omega_X^k)$ de cette décomposition.

### 3. La Classe de Déformation de Chern comme Obstruction
Pour toute classe de Hodge $\alpha \in \operatorname{Hdg}^k(X)$, nous construisons un foncteur de déformation dans la catégorie $D^b(X)$.
Si la classe $\alpha$ ne provient d'aucun cycle algébrique rationnel (et donc d'aucun complexe parfait), alors il existe une obstruction cohomologique sous forme d'une classe de Hochschild-Mitchell non nulle :
$$[\theta_\alpha] \in \mathrm{HH}^2(D^b(X))$$

### 4. Programme de Preuve pour la Conjecture de Hodge
Notre stratégie de démonstration se décompose en 4 étapes clés :
1. **Dictionnaire K-théorique :** Modéliser les classes de Hodge rationnelles comme des classes de Chern de complexes parfaits de faisceaux cohérents.
2. **Localisation via HKR :** Utiliser l'isomorphisme HKR pour projeter les cycles topologiques sur la diagonale de l'homologie de Hochschild de la catégorie dérivée.
3. **Résolution des Singularités dans $D^b(X)$ :** Démontrer que l'existence d'une résolution projective de faisceaux pour des sous-schémas fermés singuliers garantit la surjectivité locale de l'application de Chern.
4. **Annulation de la Classe de Déformation :** Démontrer que la structure kählérienne projective de $X$ force l'annulation de la classe d'obstruction $[\theta_\alpha]$ dans le groupe $\mathrm{HH}^2(D^b(X))$, prouvant ainsi que toute classe de Hodge est algébrique.
