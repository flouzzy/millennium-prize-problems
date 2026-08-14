# Blueprint Formel : Conjecture de Birch et Swinnerton-Dyer (BSD)

## 1. Énoncé Formel
Soit $E/\mathbb{Q}$ une courbe elliptique définie sur $\mathbb{Q}$.
1. **Partie Qualitative :** L'ordre d'annulation de la fonction $L(E, s)$ en $s=1$ est égal au rang du groupe de Mordell-Weil $E(\mathbb{Q})$ :
   $$\operatorname{ord}_{s=1} L(E, s) = \operatorname{rank}_{\mathbb{Z}} E(\mathbb{Q}) = r$$
2. **Partie Quantitative :** Le coefficient dominant de Taylor vérifie la formule du produit arithmétique :
   $$\lim_{s \to 1} \frac{L(E, s)}{(s-1)^r} = \frac{\Omega_E \cdot R_E \cdot |\text{Ш}(E/\mathbb{Q})| \cdot \prod c_p}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

## 2. Déconstruction des Barrières
1. **Théorèmes de Gross-Zagier & Kolyvagin (1986-1988) :** La conjecture est prouvée lorsque $\operatorname{ord}_{s=1} L(E, s) \le 1$. Le groupe de Shafarevich $\text{Ш}(E/\mathbb{Q})$ est alors fini.
2. **Obstruction du Rang $\ge 2$ :** Pour $r \ge 2$, les points de Heegner ne fournissent pas de points non triviaux dans $E(\mathbb{Q})$. La finitude de $\text{Ш}(E/\mathbb{Q})$ et la non-dégénérescence de la hauteur restent des conjectures ouvertes majeures.
3. **Théorie d'Iwasawa (Skinner-Urban 2014) :** La conjecture principale d'Iwasawa est démontrée pour les formes modulaires ordinaires, reliant la fonction $L$ $p$-adique au module de Selmer, mais nécessite la non-annulation du régulateur $p$-adique.

## 3. Analyse Critique de l'Ébauche Précédente
* **Faiblesse identifiée :** L'ébauche admettait la non-dégénérescence de l'accouplement de hauteur $p$-adique de Néron-Tate pour les rangs $r \ge 2$.
* **Redressement Méthodologique :** Formaliser dans Lean 4 la cohomologie galoisienne des représentations galoisiennes $T_p(E)$, la dualité de Poitou-Tate et les groupes de Selmer.

## 4. Graphe de Décomposition Modulaire (Lean 4)
- [x] Définition des courbes elliptiques sous forme de Weierstrass (`Mathlib.AlgebraicGeometry.EllipticCurve`).
- [ ] Formalisation de la loi de groupe de Mordell-Weil et du théorème de Mordell-Weil (finitude du rang).
- [ ] Définition formelle de la suite exacte de Selmer et du groupe de Shafarevich-Tate.
- [ ] Formalisation de la hauteur de Néron-Tate et de sa forme bilinéaire symétrique canonique.
