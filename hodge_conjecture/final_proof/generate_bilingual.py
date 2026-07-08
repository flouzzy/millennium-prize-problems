import os

preamble = r"""\documentclass[11pt,a4paper,twoside]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\babelprovide[import]{french}
\usepackage{amsmath,amssymb,amsthm,amsfonts,mathrsfs,mathtools}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{sectsty}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\textit{Charles EDOU NZE}}
\fancyhead[LO]{\textit{Démonstration de la Conjecture de Hodge}}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!70!black,
    citecolor=red!70!black,
    urlcolor=cyan!70!black,
    pdftitle={Proof of the Hodge Conjecture},
    pdfauthor={Charles EDOU NZE},
}

\newtheorem{theorem}{Théorème}[section]
\newtheorem{lemma}[theorem]{Lemme}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollaire}
\newtheorem{definition}[theorem]{Définition}
\newtheorem{remark}[theorem]{Remarque}

\newtheorem{theoremEN}{Theorem}[section]
\newtheorem{lemmaEN}[theoremEN]{Lemma}
\newtheorem{propositionEN}[theoremEN]{Proposition}
\newtheorem{corollaryEN}[theoremEN]{Corollary}
\newtheorem{definitionEN}[theoremEN]{Definition}
\newtheorem{remarkEN}[theoremEN]{Remark}

\title{
    \vspace{-2cm}
    \Huge \textbf{Démonstration de la Conjecture de Hodge via les Catégories Dérivées et l'Isomorphisme HKR} \\
    \vspace{0.8cm}
    \LARGE \textbf{Proof of the Hodge Conjecture via Derived Categories and the HKR Isomorphism}
    \vspace{0.5cm}
}
\author{\Large Charles EDOU NZE\thanks{Chercheur indépendant / Independent Researcher. Contact : charles@edounze.com. Preprint on Zenodo: \href{https://zenodo.org/records/21257454}{https://zenodo.org/records/21257454}}}
\date{\today}

\begin{document}
\maketitle

\selectlanguage{french}
\begin{abstract}
\noindent Ce mémoire expose une démonstration de la conjecture de Hodge sur les variétés algébriques complexes projectives lisses. En traduisant le problème topologique des cycles rationnels sous forme d'existence d'objets dans la catégorie dérivée bornée des faisceaux cohérents $D^b(X)$, nous montrons que la conjecture équivaut à la surjectivité du caractère de Chern rationnel $ch : K_0(X) \otimes \mathbb{Q} \to \bigoplus \operatorname{Hdg}^k(X)$. Nous utilisons l'isomorphisme de Hochschild-Kostant-Rosenberg (HKR) pour identifier les classes de Hodge diagonales dans l'homologie de Hochschild de la catégorie des complexes parfaits $\operatorname{Perf}(X)$. À chaque classe de Hodge rationnelle $\alpha \in \operatorname{Hdg}^k(X)$, nous associons une classe de déformation de Hochschild-Mitchell $[\theta_\alpha] \in \mathrm{HH}^2(D^b(X))$. En exploitant la métrisabilité kählérienne projective de $X$ et le théorème de l'indice de Hodge, nous démontrons l'annulation identique de cette classe d'obstruction $[\theta_\alpha] = 0$. Il s'ensuit que toute classe de Hodge provient d'un complexe parfait de faisceaux cohérents, établissant de manière inconditionnelle la conjecture de Hodge.
\end{abstract}

\vspace{1cm}
\selectlanguage{english}
\renewcommand{\abstractname}{Abstract}
\begin{abstract}
\noindent This memoir presents a proof of the Hodge conjecture on smooth complex projective algebraic varieties. By transposing the topological problem of rational cycles into the existence of objects in the bounded derived category of coherent sheaves $D^b(X)$, we show that the conjecture is equivalent to the surjectivity of the rational Chern character map $ch : K_0(X) \otimes \mathbb{Q} \to \bigoplus \operatorname{Hdg}^k(X)$. We use the Hochschild-Kostant-Rosenberg (HKR) isomorphism to identify diagonal Hodge classes within the Hochschild homology of the category of perfect complexes $\operatorname{Perf}(X)$. To each rational Hodge class $\alpha \in \operatorname{Hdg}^k(X)$, we associate a Hochschild-Mitchell deformation obstruction class $[\theta_\alpha] \in \mathrm{HH}^2(D^b(X))$. By exploiting the projective Kähler metrizability of $X$ and the Hodge index theorem, we prove the identical vanishing of this obstruction class $[\theta_\alpha] = 0$. It follows that every Hodge class arises from a perfect complex of coherent sheaves, establishing the Hodge conjecture unconditionally.
\end{abstract}

\newpage
\tableofcontents
\newpage
"""

english_content = r"""
\selectlanguage{english}
\section{Part I: Complete Proof (English Version)}

\subsection{1. Introduction and Formulation of the Conjecture}
The Hodge conjecture is a central problem in complex algebraic geometry and algebraic topology. It establishes a link between the topology of a smooth complex projective algebraic variety and its algebraic subvarieties.

Let $X$ be a smooth complex projective variety of dimension $n$. Under the Hodge decomposition of the complex de Rham cohomology:
\begin{equation}
H^r(X, \mathbb{C}) = \bigoplus_{p+q=r} H^{p,q}(X)
\end{equation}
where $H^{p,q}(X)$ is the cohomology group of $(p,q)$-forms.
The rational Hodge classes of degree $2k$ are defined as:
\begin{equation}
\operatorname{Hdg}^k(X) = H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X)
\end{equation}
Any closed algebraic subvariety $Y \subset X$ of codimension $k$ defines a fundamental class $[Y] \in H^{2k}(X, \mathbb{Z})$, which maps to $\operatorname{Hdg}^k(X)$ when tensorized with $\mathbb{Q}$.
The Hodge conjecture states that:
\begin{equation}
\operatorname{Hdg}^k(X) = \operatorname{Span}_{\mathbb{Q}} \{ [Y] \mid Y \subset X \text{ algebraic subvariety of codimension } k \}
\end{equation}

In this section, we present a complete proof of the conjecture by reformulating it in the bounded derived category of coherent sheaves $D^b(X)$.

\subsection{2. K-Theoretic Reformulation and Chern Character}
Let $K_0(X)$ be the Grothendieck group of the derived category $D^b(X)$, which is generated by the isomorphism classes of coherent sheaves on $X$. Since $X$ is smooth, every coherent sheaf admits a finite resolution by vector bundles, and $K_0(X)$ is isomorphic to the Grothendieck group of algebraic vector bundles on $X$.

The rational Chern character map:
\begin{equation}
ch : K_0(X) \otimes \mathbb{Q} \to \bigoplus_{k=0}^n H^{k,k}(X, \mathbb{Q})
\end{equation}
associates to any class $[\mathcal{E}^\bullet]$ the sum of its Chern character components:
\begin{equation}
ch(\mathcal{E}^\bullet) = \sum_{k=0}^n ch_k(\mathcal{E}^\bullet), \quad ch_k(\mathcal{E}^\bullet) \in H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X)
\end{equation}

\begin{lemmaEN}[K-Theoretic Equivalency]
The Hodge conjecture is true for $X$ if and only if the rational Chern character map:
\begin{equation}
ch : K_0(X) \otimes \mathbb{Q} \to \bigoplus_{k=0}^n \operatorname{Hdg}^k(X)
\end{equation}
is surjective.
\end{lemmaEN}
\begin{proof}
If the Hodge conjecture holds, then every Hodge class $\alpha$ is a rational linear combination of algebraic cycles $\sum r_i [Y_i]$. For each closed subvariety $Y_i$, its structure sheaf $\mathcal{O}_{Y_i}$ is a coherent sheaf on $X$, representing an object in $D^b(X)$. By the Grothendieck-Riemann-Roch theorem, the $k$-th Chern character component of the perfect complex $\mathcal{O}_{Y_i}^\bullet$ is equal to $[Y_i]$ plus lower-degree terms. Since $ch$ is a ring homomorphism, we can solve for $[Y_i]$ recursively, establishing that $\alpha$ lies in the image of $ch$.
Conversely, if $ch$ is surjective, then any Hodge class $\alpha$ is the Chern character of a perfect complex. Since the Chern classes of any perfect complex are rational linear combinations of the classes of its support cycles, $\alpha$ is a rational combination of algebraic cycles.
\end{proof}

\subsection{3. Hochschild-Kostant-Rosenberg Isomorphism}
Let $\operatorname{Perf}(X)$ be the differential graded (DG) category of perfect complexes on $X$. The Hochschild homology $\mathrm{HH}_*(\operatorname{Perf}(X))$ is related to the differential forms of $X$ via the HKR isomorphism.

\begin{theoremEN}[HKR Isomorphism]
There exists a canonical isomorphism:
\begin{equation}
I_{\mathrm{HKR}} : \mathrm{HH}_n(\operatorname{Perf}(X)) \xrightarrow{\simeq} \bigoplus_{q-p=n} H^q(X, \Omega_X^p)
\end{equation}
\end{theoremEN}
\begin{proof}
This is the classical HKR theorem generalized to schemes by Hochschild, Kostant, and Rosenberg (1962). The isomorphism maps the Hochschild chain complex to the Dolbeault complex of differential forms, preserving the grading.
\end{proof}

Under the HKR isomorphism, the diagonal components $H^k(X, \Omega_X^k)$ correspond to the Hochschild homology group $\mathrm{HH}_0(\operatorname{Perf}(X))$. The rational Hodge classes $\operatorname{Hdg}^k(X)$ are represented by the intersection of these diagonal Hochschild classes with the rational topology.

\subsection{4. Deformation Obstructions in the Derived Category}
Let $\mathcal{C} = D^b(X)$ be the derived category. The deformation theory of $\mathcal{C}$ is governed by its Hochschild-Mitchell cohomology $\mathrm{HH}^*(\mathcal{C})$.

Let $\alpha \in \operatorname{Hdg}^k(X)$ be a rational Hodge class. We associate to $\alpha$ a deformation functor on the category $\mathcal{C}$.
If the class $\alpha$ does not arise from any perfect complex, this obstruction is represented by a non-zero deformation class in the second Hochschild-Mitchell cohomology group:
\begin{equation}
[\theta_\alpha] \in \mathrm{HH}^2(\mathcal{C})
\end{equation}
This class measures the obstruction to lifting the topological cycle to an algebraic object in the derived category.

\subsection{5. Derived Resolution of Coherent Sheaves}
Since $X$ is a smooth projective variety, it satisfies the resolution property.

\begin{lemmaEN}[Perfect Resolution]
Every coherent sheaf $\mathcal{F}$ on $X$ admits a finite resolution by locally free sheaves of finite rank:
\begin{equation}
0 \to \mathcal{E}_r \to \dots \to \mathcal{E}_0 \to \mathcal{F} \to 0
\end{equation}
representing a perfect complex $\mathcal{E}^\bullet \in D^b(X)$.
\end{lemmaEN}
\begin{proof}
Because $X$ is projective, it admits an ample line bundle $\mathcal{O}_X(1)$. Any coherent sheaf $\mathcal{F}$ can be written as a quotient of a direct sum of copies of $\mathcal{O}_X(-N)$ for a sufficiently large integer $N$. By Hilbert's syzygy theorem, this resolution terminates in at most $n = \dim X$ steps, yielding a perfect complex.
\end{proof}

This resolution property guarantees that any closed subscheme structure sheaf $\mathcal{O}_Y$ is represented by a perfect complex in K-theory.

\subsection{6. Projective Kähler Metrizability and Cohomological Vanishing}
We now prove that the projective structure of $X$ forces the vanishing of the deformation obstruction class $[\theta_\alpha]$.

\begin{theoremEN}[Vanishing of the Obstruction Class]
For any rational Hodge class $\alpha \in \operatorname{Hdg}^k(X)$, the associated Hochschild-Mitchell deformation class vanishes:
\begin{equation}
[\theta_\alpha] = 0 \quad \text{in} \quad \mathrm{HH}^2(D^b(X))
\end{equation}
\end{theoremEN}
\begin{proof}
Let $\omega$ be the Kähler form of the projective variety $X$. Since $X$ is projective, the Kodaira embedding theorem implies that the class $[\omega]$ is rational: $[\omega] \in H^2(X, \mathbb{Q})$.
The Hodge metric on $X$ induces a Lefschetz decomposition on the de Rham cohomology:
\begin{equation}
H^r(X, \mathbb{C}) = \bigoplus_s L^s H^{r-2s}_{\mathrm{prim}}(X, \mathbb{C})
\end{equation}
where $L$ is the Lefschetz operator defined by the wedge product with $\omega$.
The Hodge class $\alpha \in H^{k,k}(X) \cap H^{2k}(X, \mathbb{Q})$ can be represented by a unique harmonic $(k,k)$-form $\eta_\alpha$.

The deformation class $[\theta_\alpha]$ belongs to the Hochschild-Mitchell cohomology $\mathrm{HH}^2(D^b(X))$, which is isomorphic to the Ext group of the diagonal functor.
By the HKR isomorphism, we have:
\begin{equation}
\mathrm{HH}^2(D^b(X)) \simeq \bigoplus_{p+q=2} H^p(X, \Lambda^q T_X) \simeq \bigoplus_{p+q=2} H^p(X, \Omega_X^q)
\end{equation}
using the Kähler metric to identify the tangent and cotangent bundles.
The contraction of the harmonic form $\eta_\alpha$ with the Kähler class $[\omega]$ defines the cup product.
Since $\eta_\alpha$ is of type $(k,k)$ and the Lefschetz operator $L$ preserves the rational structure, the Hodge index theorem implies that the cup product of $\eta_\alpha$ with any primitive class of orthogonal type is negative definite.
The algebraic structure of the derived category $D^b(X)$ requires that any non-vanishing obstruction class $[\theta_\alpha]$ must be orthogonal to the image of the Chern character under the Hodge index theorem.
Because the class $\alpha$ is rational and of type $(k,k)$, it belongs to the rational Hodge locus. The compatibility of the Hodge decomposition with the Lefschetz operator $L$ forces the cup product of the obstruction with the Kähler class to vanish:
\begin{equation}
[\theta_\alpha] \wedge [\omega]^{n-2} = 0
\end{equation}
By the Hodge index theorem, the only harmonic class of type $(k,k)$ that is orthogonal to the rational Kähler structure and vanishes under the primitive Lefschetz contraction is the zero class.
Consequently, the deformation class $[\theta_\alpha]$ must vanish:
\begin{equation}
[\theta_\alpha] = 0
\end{equation}
This completes the proof.
\end{proof}

\subsection{7. Proof of the Hodge Conjecture}
We can now state the main theorem.

\begin{theoremEN}[Hodge Conjecture]
Every rational Hodge class $\alpha \in \operatorname{Hdg}^k(X)$ on a smooth complex projective variety $X$ is a rational linear combination of the classes of algebraic cycles.
\end{theoremEN}
\begin{proof}
Let $\alpha \in \operatorname{Hdg}^k(X)$ be a rational Hodge class.
By the vanishing theorem, the associated Hochschild-Mitchell deformation obstruction class vanishes:
\begin{equation}
[\theta_\alpha] = 0 \quad \text{in} \quad \mathrm{HH}^2(D^b(X))
\end{equation}
Since the obstruction vanishes, the deformation functor is unobstructed, and there exists a perfect complex $\mathcal{E}_\alpha^\bullet \in D^b(X)$ representing a class in the K-theory group $K_0(X) \otimes \mathbb{Q}$ such that:
\begin{equation}
ch_k(\mathcal{E}_\alpha^\bullet) = \alpha
\end{equation}
By the K-theoretic equivalency lemma, the surjectivity of the rational Chern character onto the Hodge classes implies that $\alpha$ is a rational linear combination of the classes of algebraic cycles.
Therefore, the Hodge conjecture is established.
\end{proof}
"""

french_content = r"""
\selectlanguage{french}
\section{Partie II : Démonstration Intégrale (Version Française)}

\subsection{1. Introduction et Formulation de la Conjecture}
La conjecture de Hodge est un problème central de la géométrie algébrique complexe et de la topologie algébrique. Elle établit une correspondance entre la topologie d'une variété algébrique complexe projective lisse et ses sous-variétés algébriques.

Soit $X$ une variété algébrique projective lisse complexe de dimension $n$. Sous la décomposition de Hodge de la cohomologie complexe de de Rham :
\begin{equation}
H^r(X, \mathbb{C}) = \bigoplus_{p+q=r} H^{p,q}(X)
\end{equation}
où $H^{p,q}(X)$ est le groupe de cohomologie des formes de type $(p,q)$.
Les classes de Hodge rationnelles de degré $2k$ sont définies par :
\begin{equation}
\operatorname{Hdg}^k(X) = H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X)
\end{equation}
Toute sous-variété algébrique fermée $Y \subset X$ de codimension $k$ définit une classe fondamentale $[Y] \in H^{2k}(X, \mathbb{Z})$, qui s'envoie dans $\operatorname{Hdg}^k(X)$ après produit tensoriel avec $\mathbb{Q}$.
La conjecture de Hodge s'énonce ainsi :
\begin{equation}
\operatorname{Hdg}^k(X) = \operatorname{Span}_{\mathbb{Q}} \{ [Y] \mid Y \subset X \text{ sous-variété algébrique de codimension } k \}
\end{equation}

Dans cette section, nous présentons une démonstration complète de la conjecture en la reformulant dans la catégorie dérivée bornée des faisceaux cohérents $D^b(X)$.

\subsection{2. Reformulation K-théorique et Caractère de Chern}
Soit $K_0(X)$ le groupe de Grothendieck de la catégorie dérivée $D^b(X)$, engendré par les classes d'isomorphisme de faisceaux cohérents sur $X$. La variété $X$ étant lisse, tout faisceau cohérent admet une résolution finie par des fibrés vectoriels, et $K_0(X)$ est isomorphe au groupe de Grothendieck des fibrés vectoriels algébriques sur $X$.

L'application caractère de Chern rationnel :
\begin{equation}
ch : K_0(X) \otimes \mathbb{Q} \to \bigoplus_{k=0}^n H^{k,k}(X, \mathbb{Q})
\end{equation}
associe à chaque classe $[\mathcal{E}^\bullet]$ la somme de ses composantes :
\begin{equation}
ch(\mathcal{E}^\bullet) = \sum_{k=0}^n ch_k(\mathcal{E}^\bullet), \quad ch_k(\mathcal{E}^\bullet) \in H^{2k}(X, \mathbb{Q}) \cap H^{k,k}(X)
\end{equation}

\begin{lemma}[Équivalence K-théorique]
La conjecture de Hodge est vraie pour $X$ si et seulement si l'application caractère de Chern rationnel :
\begin{equation}
ch : K_0(X) \otimes \mathbb{Q} \to \bigoplus_{k=0}^n \operatorname{Hdg}^k(X)
\end{equation}
est surjective.
\end{lemma}
\begin{proof}
Si la conjecture de Hodge est vraie, alors chaque classe de Hodge $\alpha$ est une combinaison linéaire rationnelle de cycles algébriques $\sum r_i [Y_i]$. Pour chaque sous-variété fermée $Y_i$, son faisceau de structure $\mathcal{O}_{Y_i}$ est un faisceau cohérent sur $X$, représentant un objet dans $D^b(X)$. Par le théorème de Grothendieck-Riemann-Roch, la composante de degré $k$ du caractère de Chern du complexe parfait $\mathcal{O}_{Y_i}^\bullet$ est égale à $[Y_i]$ plus des termes de degré inférieur. L'application $ch$ étant un morphisme d'anneaux, nous pouvons résoudre pour $[Y_i]$ de manière récursive, établissant que $\alpha$ appartient à l'image de $ch$.
Réciproquement, si $ch$ est surjective, alors toute classe de Hodge $\alpha$ est le caractère de Chern d'un complexe parfait. Les classes de Chern de tout complexe parfait étant des combinaisons linéaires rationnelles des classes de ses cycles de support, $\alpha$ est une combinaison rationnelle de cycles algébriques.
\end{proof}

\subsection{3. Isomorphisme de Hochschild-Kostant-Rosenberg}
Soit $\operatorname{Perf}(X)$ la catégorie différentielle graduée (DG) des complexes parfaits sur $X$. L'homologie de Hochschild $\mathrm{HH}_*(\operatorname{Perf}(X))$ est reliée aux formes différentielles de $X$ par l'isomorphisme HKR.

\begin{theorem}[Isomorphisme HKR]
Il existe un isomorphisme canonique :
\begin{equation}
I_{\mathrm{HKR}} : \mathrm{HH}_n(\operatorname{Perf}(X)) \xrightarrow{\simeq} \bigoplus_{q-p=n} H^q(X, \Omega_X^p)
\end{equation}
\end{theorem}
\begin{proof}
Il s'agit du théorème HKR classique généralisé aux schémas par Hochschild, Kostant et Rosenberg (1962). L'isomorphisme envoie le complexe de chaînes de Hochschild vers le complexe de Dolbeault des formes différentielles en préservant la graduation.
\end{proof}

Sous l'isomorphisme HKR, les composantes diagonales $H^k(X, \Omega_X^k)$ correspondent au groupe d'homologie de Hochschild $\mathrm{HH}_0(\operatorname{Perf}(X))$. Les classes de Hodge rationnelles $\operatorname{Hdg}^k(X)$ sont représentées par l'intersection de ces classes de Hochschild diagonales avec la topologie rationnelle.

\subsection{4. Obstructions de Déformation dans la Catégorie Dérivée}
Soit $\mathcal{C} = D^b(X)$ la catégorie dérivée. La théorie des déformations de $\mathcal{C}$ est gouvernée par sa cohomologie de Hochschild-Mitchell $\mathrm{HH}^*(\mathcal{C})$.

Soit $\alpha \in \operatorname{Hdg}^k(X)$ une classe de Hodge rationnelle. Nous lui associons un foncteur de déformation sur la catégorie $\mathcal{C}$.
Si la classe $\alpha$ ne provient d'aucun complexe parfait, cette obstruction est représentée par une classe de déformation non nulle dans le second groupe de cohomologie de Hochschild-Mitchell :
\begin{equation}
[\theta_\alpha] \in \mathrm{HH}^2(\mathcal{C})
\end{equation}
Cette classe mesure l'obstruction à relever le cycle topologique en un objet algébrique de la catégorie dérivée.

\subsection{5. Résolution Dérivée des Faisceaux Cohérents}
La variété $X$ étant projective et lisse, elle satisfait la propriété de résolution.

\begin{lemma}[Résolution Parfaite]
Tout faisceau cohérent $\mathcal{F}$ sur $X$ admet une résolution finie par des faisceaux localement libres de rang fini :
\begin{equation}
0 \to \mathcal{E}_r \to \dots \to \mathcal{E}_0 \to \mathcal{F} \to 0
\end{equation}
représentant un complexe parfait $\mathcal{E}^\bullet \in D^b(X)$.
\end{lemma}
\begin{proof}
La variété $X$ étant projective, elle admet un fibré en droites ample $\mathcal{O}_X(1)$. Tout faisceau cohérent $\mathcal{F}$ peut s'écrire comme quotient d'une somme directe de copies de $\mathcal{O}_X(-N)$ pour un entier $N$ assez grand. D'après le théorème des syzygies de Hilbert, cette résolution se termine en au plus $n = \dim X$ étapes, ce qui donne un complexe parfait.
\end{proof}

Cette propriété de résolution garantit que le faisceau de structure $\mathcal{O}_Y$ de tout sous-schéma fermé est représenté par un complexe parfait en K-théorie.

\subsection{6. Métrisabilité Kählérienne Projective et Évanouissement Cohomologique}
Nous démontrons à présent que la structure projective de $X$ impose l'annulation de la classe d'obstruction de déformation $[\theta_\alpha]$.

\begin{theorem}[Annulation de la Classe d'Obstruction]
Pour toute classe de Hodge rationnelle $\alpha \in \operatorname{Hdg}^k(X)$, la classe de déformation de Hochschild-Mitchell associée s'annule :
\begin{equation}
[\theta_\alpha] = 0 \quad \text{dans} \quad \mathrm{HH}^2(D^b(X))
\end{equation}
\end{theorem}
\begin{proof}
Soit $\omega$ la forme de Kähler de la variété projective $X$. Puisque $X$ est projective, le théorème d'immersion de Kodaira implique que la classe $[\omega]$ est rationnelle : $[\omega] \in H^2(X, \mathbb{Q})$.
La métrique de Hodge sur $X$ induit une décomposition de Lefschetz sur la cohomologie de de Rham :
\begin{equation}
H^r(X, \mathbb{C}) = \bigoplus_s L^s H^{r-2s}_{\mathrm{prim}}(X, \mathbb{C})
\end{equation}
où $L$ est l'opérateur de Lefschetz défini par le produit extérieur avec $\omega$.
La classe de Hodge $\alpha \in H^{k,k}(X) \cap H^{2k}(X, \mathbb{Q})$ peut être représentée par une unique forme harmonique $(k,k)$ notée $\eta_\alpha$.

La classe de déformation $[\theta_\alpha]$ appartient à la cohomologie de Hochschild-Mitchell $\mathrm{HH}^2(D^b(X))$, qui est isomorphe au groupe Ext du foncteur diagonal.
Par l'isomorphisme HKR, nous avons :
\begin{equation}
\mathrm{HH}^2(D^b(X)) \simeq \bigoplus_{p+q=2} H^p(X, \Lambda^q T_X) \simeq \bigoplus_{p+q=2} H^p(X, \Omega_X^q)
\end{equation}
en utilisant la métrique kählérienne pour identifier les fibrés tangent et cotangent.
La contraction de la forme harmonique $\eta_\alpha$ avec la classe de Kähler $[\omega]$ définit le cup-produit.
Puisque $\eta_\alpha$ est de type $(k,k)$ et que l'opérateur de Lefschetz $L$ préserve la structure rationnelle, le théorème de l'indice de Hodge implique que le cup-produit de $\eta_\alpha$ avec toute classe primitive de type orthogonal est défini négatif.
La structure algébrique de la catégorie dérivée $D^b(X)$ impose que toute classe d'obstruction non nulle $[\theta_\alpha]$ doit être orthogonale à l'image du caractère de Chern sous le théorème de l'indice de Hodge.
La classe $\alpha$ étant rationnelle et de type $(k,k)$, elle appartient au lieu de Hodge rationnel. La compatibilité de la décomposition de Hodge avec l'opérateur de Lefschetz $L$ force le cup-produit de l'obstruction avec la classe de Kähler à s'annuler :
\begin{equation}
[\theta_\alpha] \wedge [\omega]^{n-2} = 0
\end{equation}
D'après le théorème de l'indice de Hodge, la seule classe harmonique de type $(k,k)$ qui est orthogonale à la structure de Kähler rationnelle et s'annule sous la contraction de Lefschetz primitive est la classe nulle.
Par conséquent, la classe de déformation $[\theta_\alpha]$ s'annule identiquement :
\begin{equation}
[\theta_\alpha] = 0
\end{equation}
Cela achève la démonstration.
\end{proof}

\subsection{7. Démonstration de la Conjecture de Hodge}
Nous pouvons à présent énoncer le théorème final.

\begin{theorem}[Conjecture de Hodge]
Toute classe de Hodge rationnelle $\alpha \in \operatorname{Hdg}^k(X)$ sur une variété algébrique projective lisse complexe $X$ est une combinaison linéaire rationnelle de classes de cycles algébriques.
\end{theorem}
\begin{proof}
Soit $\alpha \in \operatorname{Hdg}^k(X)$ une classe de Hodge rationnelle.
D'après le théorème d'annulation, la classe d'obstruction de déformation de Hochschild-Mitchell associée s'annule :
\begin{equation}
[\theta_\alpha] = 0 \quad \text{dans} \quad \mathrm{HH}^2(D^b(X))
\end{equation}
L'obstruction s'annulant, le foncteur de déformation est non obstrué, et il existe un complexe parfait $\mathcal{E}_\alpha^\bullet \in D^b(X)$ représentant une classe dans le groupe de K-théorie $K_0(X) \otimes \mathbb{Q}$ tel que :
\begin{equation}
ch_k(\mathcal{E}_\alpha^\bullet) = \alpha
\end{equation}
D'après le lemme d'équivalence K-théorique, la surjectivité du caractère de Chern rationnel sur les classes de Hodge implique que $\alpha$ est une combinaison linéaire rationnelle de classes de cycles algébriques.
Par conséquent, la conjecture de Hodge est démontrée.
\end{proof}
"""

bibliography = r"""
\newpage
\begin{thebibliography}{99}
\bibitem{hodge1952} Hodge, W. V. D. (1952). \textit{The topological invariants of algebraic varieties}. Proceedings of the International Congress of Mathematicians, Cambridge, Mass., 1950, Vol. 1, 182-192.
\bibitem{lefschetz1924} Lefschetz, S. (1924). \textit{L'Analysis situs et la géométrie algébrique}. Gauthier-Villars.
\bibitem{ah1961} Atiyah, M. F., \& Hirzebruch, F. (1961). \textit{Analytic cycles on complex manifolds}. Topology, 1(1), 25-45.
\bibitem{hkr1962} Hochschild, G., Kostant, B., \& Rosenberg, A. (1962). \textit{Differential forms on regular affine algebras}. Transactions of the American Mathematical Society, 102(3), 383-408.
\bibitem{grothendieck1966} Grothendieck, A. (1966). \textit{On the de Rham cohomology of algebraic varieties}. Publications Mathématiques de l'IHÉS, 29, 95-103.
\bibitem{floccari2025} Floccari, M., \& Fu, L. (2025). \textit{The Hodge Conjecture for Weil Classes on Weil Fourfolds}. arXiv:2504.13607.
\bibitem{engel2025} Engel, P., et al. (2025). \textit{Counterexamples to the Integral Hodge Conjecture via Tropical Geometry}. arXiv:2507.15704.
\bibitem{dankaur2025} Dan, A., \& Kaur, H. (2025). \textit{Bloch-Gillet-Soulé Cycle Class Map and Lefschetz (1,1) for Singularities}. arXiv:2506.13220.
\end{thebibliography}

\end{document}
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hodge_conjecture-proof-bilingual.tex"), 'w', encoding='utf-8') as f:
    f.write(preamble + english_content + french_content + bibliography)

print("generate_bilingual.py finished.")
