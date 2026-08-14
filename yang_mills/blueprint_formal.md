# Blueprint Formel : Théorie Quantique de Yang-Mills et Gap de Masse

## 1. Énoncé Formel
Pour tout groupe de Lie compact simple $G$ (ex. $SU(3)$), construire une théorie quantique des champs non-abélienne de Yang-Mills sur $\mathbb{R}^4$ satisfaisant les axiomes d'Osterwalder-Schrader (ou de Wightman), et prouver l'existence d'un gap de masse $\Delta > 0$, c'est-à-dire que le spectre du Hamiltonien vérifie :
$$\operatorname{Spec}(H) \subseteq \{0\} \cup [\Delta, \infty)$$

## 2. Déconstruction des Barrières
1. **Théorème de Singer (1978) & Copies de Gribov :** Il n'existe pas de fixation de jauge globale continue dans l'espace des connexions $\mathcal{A}/\mathcal{G}$.
2. **Limite Continue (Haag's Theorem & Renormalisation) :** La théorie sur réseau (Wilson lattice gauge theory) possède un gap de masse à couplage fort, mais la limite d'échelle continue $a \to 0$ (liberté asymptotique) requiert des estimations non perturbatives uniformes.

## 3. Analyse Critique de l'Ébauche Précédente
* **Faiblesse identifiée :** L'ébauche déduisait le gap de masse directement de pôles complexes dans le propagateur de Gribov-Zwanziger à l'ordre d'un arbre, ce qui ne constitue pas une preuve constructive au sens des axiomes OS.
* **Redressement Méthodologique :** Développer le cadre formel des théories de jauge sur réseau (Wilson loops, Haar measure sur $SU(N)$) et formaliser les bornes de Cao-Chatterjee (2025) dans la limite grand $N$.

## 4. Graphe de Décomposition Modulaire (Lean 4)
- [ ] Formalisation de l'intégration de Haar sur les groupes de Lie compacts $SU(N)$.
- [ ] Définition de l'action de jauge de Wilson sur le réseau discret $\mathbb{Z}^4$.
- [ ] Formalisation de l'inégalité de corrélation de Griffiths / Ginibre pour les boucles de Wilson.
- [ ] Preuve formelle de la décroissance exponentielle des fonctions de corrélation (trou spectral) à couplage fort $\beta \ll 1$.
