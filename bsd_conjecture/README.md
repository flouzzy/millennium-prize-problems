# La Conjecture de Birch et Swinnerton-Dyer (BSD)

Dossier dédié à l'investigation et à la résolution de la **Conjecture de Birch et Swinnerton-Dyer (BSD)**.

---

## 🔗 Ressources et Documents

| Document | Description |
| :--- | :--- |
| [**Tableau de Bord**](../dashboard.md) | Suivi général de l'avancement des problèmes du millénaire. |
| [**Notes de Recherche**](notes.md) | Synthèse des barrières et des pistes formelles. |

---

## 1. Présentation du Problème

La conjecture de Birch et Swinnerton-Dyer (BSD) est l'un des problèmes ouverts les plus importants de la théorie des nombres et de la géométrie arithmétique. Elle relie des objets analytiques (la fonction $L$ d'une courbe elliptique) à des objets algébriques (le groupe des points rationnels de cette courbe).

Soit $E$ une courbe elliptique définie sur le corps des nombres rationnels $\mathbb{Q}$.
D'après le théorème de Mordell-Weil, le groupe des points rationnels $E(\mathbb{Q})$ est un groupe abélien de type fini :
$$E(\mathbb{Q}) \simeq \mathbb{Z}^r \oplus E(\mathbb{Q})_{\mathrm{tors}}$$
où $r \ge 0$ est le **rang** de la courbe elliptique, et $E(\mathbb{Q})_{\mathrm{tors}}$ est le sous-groupe de torsion (qui est fini).

Soit $L(E, s)$ la fonction $L$ de Hasse-Weil associée à $E$, définie pour $\Re(s) > 3/2$ par un produit d'Euler sur les nombres premiers. Grâce au théorème de modularité (démontré par Wiles, Taylor, Breuil, Conrad, Diamond), $L(E, s)$ admet un prolongement analytique sur tout le plan complexe $\mathbb{C}$ et satisfait une équation fonctionnelle reliant $s$ et $2-s$.

La conjecture de Birch et Swinnerton-Dyer s'énonce en deux parties :

1. **La Conjecture de BSD Qualitative :** Le rang $r$ de $E(\mathbb{Q})$ est égal à l'ordre d'annulation de la fonction $L(E, s)$ au point central $s=1$ :
   $$\operatorname{ord}_{s=1} L(E, s) = r$$
2. **La Conjecture de BSD Quantitative :** Le premier coefficient non nul de la série de Taylor de $L(E, s)$ en $s=1$ est donné par :
   $$\lim_{s \to 1} \frac{L(E, s)}{(s-1)^r} = \frac{\Omega_E \cdot R_E \cdot |{\text{Ш}}(E/\mathbb{Q})| \cdot \prod_p c_p}{|E(\mathbb{Q})_{\mathrm{tors}}|^2}$$
   où $\Omega_E$ est la période réelle de la courbe, $R_E$ est son régulateur de Néron-Tate, $c_p$ sont les nombres de Tamagawa locaux, et ${\text{Ш}}(E/\mathbb{Q})$ désigne le groupe de Tate-Shafarevich de $E$.

---

## 2. Obstacles et Résultats Fondamentaux (Les Barrières)

### A. Le Théorème de Gross-Zagier et Kolyvagin

La conjecture est démontrée pour les courbes elliptiques d'ordre d'annulation $\le 1$ :

* Si $\operatorname{ord}_{s=1} L(E, s) = 0$, alors le rang de $E(\mathbb{Q})$ est 0 et le groupe de Tate-Shafarevich ${\text{Ш}}(E/\mathbb{Q})$ est fini.
* Si $\operatorname{ord}_{s=1} L(E, s) = 1$, alors le rang de $E(\mathbb{Q})$ est 1 et ${\text{Ш}}(E/\mathbb{Q})$ est fini.
* **Le verrou :** Pour les rangs supérieurs ($r \ge 2$), les systèmes d'Euler d'Heegner utilisés par Kolyvagin s'effondrent car il n'existe pas de théorie systématique pour construire des points d'Heegner de rang supérieur.

### B. La Finitude du Groupe de Tate-Shafarevich ${\text{Ш}}(E/\mathbb{Q})$

Le groupe de Tate-Shafarevich mesure l'obstruction au principe de Hasse (local-global) pour les espaces homogènes sous $E$.

* **Le verrou :** La finitude de ${\text{Ш}}(E/\mathbb{Q})$ est elle-même une conjecture majeure et non démontrée pour $r \ge 2$. La présence éventuelle d'éléments de torsion infinie ou de structures non finies empêche le contrôle du terme de droite de la formule quantitative.

### C. La Barrière p-adique

La plupart des outils modernes (théorie d'Iwasawa, fonctions L p-adiques) dépendent du choix d'un nombre premier $p$.

* **Le verrou :** Le passage des résultats p-adiques locaux au résultat rationnel global global requiert de faire varier $p$ et de contrôler les obstructions de Selmer de manière uniforme, ce qui se heurte aux sauts de rang.

---

## 3. Stratégies et Programme de Recherche

Pour surmonter ces verrous, nous allons suivre les axes de recherche suivants :

1. **Axe 1 : Théorie d'Iwasawa de K-théorie et Conjecture de BSD p-adique**
   Formuler la conjecture de BSD à l'aide de la K-théorie et de l'homologie cyclique des algèbres d'Iwasawa. Relier le groupe de Selmer aux invariants de Fitting des modules d'Iwasawa.

2. **Axe 2 : Systèmes d'Euler Supérieurs et Cycles Motiviques**
   Généraliser les systèmes d'Euler classiques à des familles de cycles motiviques de codimension supérieure dans des produits de variétés modulaires (cycles de Beilinson-Kato-Flach).

3. **Axe 3 : Finitude de ${\text{Ш}}(E/\mathbb{Q})$ via Cohomologie Galoisienne Non-Abélienne**
   Démontrer la finitude de ${\text{Ш}}(E/\mathbb{Q})$ pour toute courbe elliptique régulière en formulant une suite spectrale reliant la cohomologie galoisienne à l'algèbre des opérateurs de Hecke de poids 2.
