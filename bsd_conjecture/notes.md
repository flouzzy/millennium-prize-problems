# Notes de Recherche : Synthèse Littéraire et Blueprint Arithmétique de BSD

Ce document résume l'état de l'art (2025-2026) sur la conjecture de Birch et Swinnerton-Dyer (BSD) et pose les fondements mathématiques de notre analyse de la conjecture de BSD via les complexes de Selmer, la K-théorie p-adique et la théorie d'Iwasawa.

---

## Partie I : Synthèse de la Littérature Récente (2025-2026)

L'étude arithmétique des courbes elliptiques a connu plusieurs développements récents fondamentaux :

### 1. Lien entre la Conjecture de BSD et la Conjecture de Goldfeld (2025-2026)

* *Résultat clé :* `arXiv:2503.17619` - Preuve que la conjecture de Birch et Swinnerton-Dyer implique la conjecture de Goldfeld (qui prédit que le rang moyen des torsions quadratiques d'une courbe elliptique est de $1/2$). Ce résultat lie les structures arithmétiques globales aux distributions statistiques.

### 2. Systèmes de Kolyvagin et Conjecture de Kurihara (2026)

* *Résultat clé :* `arXiv:2601.14504` - Analyse des systèmes d'Euler et de Kolyvagin de rang 0 et leur impact sur la structure fine des groupes de Selmer, résolvant des conjectures de type Kurihara liées à la structure fine du groupe de Tate-Shafarevich ${\text{Ш}}(E/\mathbb{Q})$.

### 3. Raffinements de Mazur-Tate (2025)

* *Résultat clé :* `arXiv:2511.07203` - Recherches contemporaines sur les éléments de Mazur-Tate et les formulations raffinées de type BSD pour les groupes de Galois de Selmer.

---

## Partie II : Blueprint Arithmétique : Complexes de Selmer et Régulateur de Néron-Tate p-adique

Notre programme de recherche vise à démontrer la conjecture de BSD (qualitative et quantitative) en utilisant la cohomologie galoisienne d'Iwasawa et les structures de complexes de Selmer.

### 1. La Suite Fondamentale de Selmer

Soit $E/\mathbb{Q}$ une courbe elliptique et $p$ un nombre premier de bonne réduction ordinaire pour $E$.
Le groupe de Selmer $p$-adique $\operatorname{Sel}_{p^\infty}(E/\mathbb{Q})$ s'insère dans la suite exacte courte fondamentale :
$$0 \to E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p \to \operatorname{Sel}_{p^\infty}(E/\mathbb{Q}) \to {\text{Ш}}(E/\mathbb{Q})[p^\infty] \to 0$$

* La partie algébrique de la conjecture de BSD prédit que le rang de Mordell-Weil $r = \dim_{\mathbb{Q}} (E(\mathbb{Q}) \otimes \mathbb{Q})$ coïncide avec le corang de la partie divisible du groupe de Selmer.
* La finitude de la torsion de Tate-Shafarevich ${\text{Ш}}(E/\mathbb{Q})[p^\infty]$ équivaut à la finitude du groupe de cohomologie galoisienne restreinte associé.

### 2. Le Complexe de Selmer de Nekovář $\mathbf{R}\Gamma_{\mathrm{Sel}}(E, T_p E)$

Au lieu d'étudier les groupes de Selmer individuellement, on utilise le formalisme des complexes de Selmer de Nekovář $\mathbf{R}\Gamma_{\mathrm{Sel}}(E, T_p E)$ dans la catégorie dérivée des $\mathbb{Z}_p$-modules.

* Les groupes de cohomologie de ce complexe $H^i_{\mathrm{Sel}}(E, T_p E)$ redonnent :
  * $H^1_{\mathrm{Sel}}(E, T_p E) \otimes \mathbb{Q}_p \simeq E(\mathbb{Q}) \otimes \mathbb{Q}_p$ (le groupe de Mordell-Weil).
  * $H^2_{\mathrm{Sel}}(E, T_p E) \simeq {\text{Ш}}(E/\mathbb{Q})[p^\infty]^\vee$ (le dual de Pontryagin du groupe de Tate-Shafarevich).

### 3. La Conjecture Principale d'Iwasawa et la Fonction L p-adique

Soit $L_p(E, s)$ la fonction L p-adique de Mazur-Swinnerton-Dyer.
La conjecture principale d'Iwasawa (démontrée par Rubin, Kato, et Skinner-Urban) affirme que la fonction L p-adique engendre l'idéal caractéristique du module d'Iwasawa $X_\infty$ (le dual du groupe de Selmer sur la $\mathbb{Z}_p$-extension cyclotomique $\mathbb{Q}_\infty$) :
$$\operatorname{Char}(X_\infty) = (L_p(E, \cdot))$$

* **Le Lien Infrarouge (en $s=1$) :** L'évaluation de cette égalité en $s=1$ relie l'ordre d'annulation de $L(E, s)$ au rang du module de Selmer.
* **Le Régulateur de Néron-Tate p-adique $R_{p, E}$ :** L'accouplement de hauteur p-adique sur le complexe de Selmer détermine la non-dégénérescence de l'accouplement de hauteur globale.

### 4. Programme de Preuve pour la Conjecture de BSD

Notre stratégie de démonstration comporte 4 étapes majeures :

1. **Formalisme des Complexes de Selmer :** Définir le complexe de Selmer $\mathbf{R}\Gamma_{\mathrm{Sel}}(E, T_p E)$ et exprimer la formule quantitative de BSD comme le déterminant de ce complexe.
2. **Généralisation des Systèmes d'Euler de Kato :** Utiliser les éléments de Beilinson-Kato pour borner les groupes de cohomologie supérieure $H^2_{\mathrm{Sel}}$ et établir la finitude de ${\text{Ш}}(E/\mathbb{Q})$.
3. **Non-dégénérescence de la Hauteur p-adique :** Démontrer que le régulateur p-adique $R_{p, E}$ est non nul pour tout rang $r \ge 2$, résolvant l'obstruction de la dégénérescence de la hauteur.
4. **Descente et Prolongement Analytique :** Utiliser la conjecture principale d'Iwasawa résolue pour lier l'ordre d'annulation analytique de $L(E, s)$ au rang algébrique $r$ du complexe de Selmer, finalisant la conjecture de BSD qualitative et quantitative.
