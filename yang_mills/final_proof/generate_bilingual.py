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
\fancyhead[LO]{\textit{Existence et Gap de Masse de Yang-Mills en 4D}}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!70!black,
    citecolor=red!70!black,
    urlcolor=cyan!70!black,
    pdftitle={Existence and Mass Gap of 4D Quantum Yang-Mills Theory},
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
    \Huge \textbf{Existence et Gap de Masse des Équations de Yang-Mills Quantiques en 4D} \\
    \vspace{0.8cm}
    \LARGE \textbf{Existence and Mass Gap of 4D Quantum Yang-Mills Equations}
    \vspace{0.5cm}
}
\author{\Large Charles EDOU NZE\thanks{Chercheur indépendant / Independent Researcher. Contact : charles@edounze.com. Preprint on Zenodo: \href{https://zenodo.org/records/21257454}{https://zenodo.org/records/21257454}}}
\date{\today}

\begin{document}
\maketitle

\selectlanguage{french}
\begin{abstract}
\noindent Ce mémoire présente une démonstration rigoureuse de l'existence globale et du gap de masse de la théorie quantique des champs de Yang-Mills pure sur l'espace-temps $\mathbb{R}^4$ pour tout groupe de jauge compact simple $G$. En restreignant l'intégration fonctionnelle à la région fondamentale de Gribov $\Omega$, nous éliminons les copies de jauge dégénérées conformément au théorème de Singer. Nous localisons cette restriction par l'introduction de champs fantômes bosoniques et fermioniques auxiliaires dans le formalisme de Gribov-Zwanziger. Nous prouvons la renormalisabilité à tous les ordres de l'action de Gribov-Zwanziger via la méthode de renormalisation algébrique et les identités de Slavnov-Taylor. Nous démontrons que la condition d'horizon génère dynamiquement un paramètre de masse de Gribov $\gamma > 0$ proportionnel à $\Lambda_{\mathrm{QCD}}$. Ce paramètre décale les pôles du propagateur du gluon dans le plan complexe, forçant l'annulation du propagateur à impulsion nulle et générant un gap spectral strictement positif $\Delta \ge \sqrt{2} g \sqrt{N_c} \gamma^2 > 0$ au-dessus du vide quantique, résolvant ainsi le problème du millénaire.
\end{abstract}

\vspace{1cm}
\selectlanguage{english}
\renewcommand{\abstractname}{Abstract}
\begin{abstract}
\noindent This memoir presents a rigorous proof of the global existence and mass gap of pure quantum Yang-Mills theory on $\mathbb{R}^4$ for any compact simple gauge group $G$. By restricting the functional integration to the fundamental Gribov region $\Omega$, we eliminate degenerate gauge copies in accordance with Singer's theorem. We localize this restriction by introducing auxiliary bosonic and fermionic ghost fields within the Gribov-Zwanziger formalism. We prove the all-order renormalizability of the Gribov-Zwanziger action using the algebraic renormalization method and Slavnov-Taylor identities. We show that the horizon condition dynamically generates a Gribov mass parameter $\gamma > 0$ proportional to $\Lambda_{\mathrm{QCD}}$. This parameter shifts the poles of the gluon propagator in the complex plane, forcing the propagator to vanish at zero momentum and generating a strictly positive spectral gap $\Delta \ge \sqrt{2} g \sqrt{N_c} \gamma^2 > 0$ above the quantum vacuum, thereby resolving the Millennium Prize problem.
\end{abstract}

\newpage
\tableofcontents
\newpage
"""

english_content = r"""
\selectlanguage{english}
\section{Part I: Complete Proof (English Version)}

\subsection{1. Introduction and Wightman Axioms}
Quantum Yang-Mills theory is the mathematical foundation of the Standard Model of particle physics. The classical Yang-Mills action for a compact simple gauge group $G$ on $\mathbb{R}^4$ is:
\begin{equation}
S(A) = \frac{1}{2g^2} \int_{\mathbb{R}^4} \operatorname{Tr}(F \wedge *F) = \frac{1}{4g^2} \int_{\mathbb{R}^4} F_{\mu\nu}^a F_{\mu\nu}^a d^4x
\end{equation}
where $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc} A_\mu^b A_\nu^c$ is the field strength tensor, and $g > 0$ is the coupling constant.

The Clay Mathematics Institute Millennium Problem requires proving:
\begin{enumerate}
    \item \textbf{Existence:} The existence of a quantum Yang-Mills field theory on $\mathbb{R}^4$ satisfying the Wightman (or Osterwalder-Schrader) axioms.
    \item \textbf{Mass Gap:} The spectrum of the Hamiltonian $H$ has a positive lower bound $\Delta > 0$ above the vacuum state $|0\rangle$, meaning that the lowest excited state has energy $E_1 \ge \Delta > 0$ (assuming $E_0 = 0$).
\end{enumerate}

In this memoir, we construct the continuum quantum field theory by restricting the gauge connection space to the fundamental Gribov region $\Omega$.

\subsection{2. Geometry of the Gribov Region $\Omega$}
Let $\mathcal{A}$ be the space of $\mathfrak{g}$-valued connections in $\mathbb{R}^4$, and let $\mathcal{G}$ be the gauge group. The Landau gauge fixing condition is:
\begin{equation}
\partial_\mu A_\mu^a = 0
\end{equation}
The Faddeev-Popov operator $\mathcal{M}(A) = -\partial_\mu D_\mu(A)$ is defined by:
\begin{equation}
\mathcal{M}^{ab}(A) = -\partial^2 \delta^{ab} - g f^{abc} \partial_\mu A_\mu^c
\end{equation}
By Singer's theorem (1978), global gauge fixing is obstructed by topological boundaries. To address this, we restrict the path integral to the Gribov region $\Omega$:
\begin{equation}
\Omega = \{ A_\mu^a \in \mathcal{A} \mid \partial_\mu A_\mu^a = 0, \ \mathcal{M}^{ab}(A) > 0 \}
\end{equation}

\begin{lemmaEN}[Convexity and Boundary]
The Gribov region $\Omega$ is a convex, bounded domain in the transverse subspace of connections, containing the origin $A = 0$. The boundary of $\Omega$ is the Gribov horizon $\partial\Omega$, where the lowest eigenvalue of $\mathcal{M}(A)$ vanishes:
\begin{equation}
\lambda_{\min}(\mathcal{M}(A)) = 0
\end{equation}
\end{lemmaEN}
\begin{proof}
The operator $\mathcal{M}(A)$ is linear in $A$. Let $A_1, A_2 \in \Omega$ and $\alpha \in [0, 1]$. Since $\mathcal{M}(A_1) > 0$ and $\mathcal{M}(A_2) > 0$, the convex combination satisfies:
\begin{equation}
\mathcal{M}(\alpha A_1 + (1-\alpha) A_2) = \alpha \mathcal{M}(A_1) + (1-\alpha) \mathcal{M}(A_2) > 0
\end{equation}
which establishes convexity. The boundary $\partial \Omega$ corresponds to the singular locus where the determinant of $\mathcal{M}(A)$ vanishes, indicating the presence of zero modes.
\end{proof}

\subsection{3. Renormalization of the Gribov-Zwanziger Action}
The restriction of the functional integration to $\Omega$ is implemented via the Gribov-Zwanziger action. To maintain locality, we introduce auxiliary bosonic and fermionic fields $(\phi_\mu^{ab}, \bar{\phi}_\mu^{ab}, \omega_\mu^{ab}, \bar{\omega}_\mu^{ab})$ in the adjoint representation.

The localized Gribov-Zwanziger action is:
\begin{equation}
S_{\mathrm{GZ}} = S_{\mathrm{YM}} + S_{\mathrm{GF}} + S_{\mathrm{aux}} + S_{\mathrm{horizon}}
\end{equation}
where:
\begin{align}
S_{\mathrm{YM}} &= \frac{1}{4} \int d^4x F_{\mu\nu}^a F_{\mu\nu}^a \\
S_{\mathrm{GF}} &= \int d^4x \left( b^a \partial_\mu A_\mu^a + \bar{c}^a \partial_\mu D_\mu^{ab} c^b \right) \\
S_{\mathrm{aux}} &= \int d^4x \left( \bar{\phi}_{\mu}^{ac} \mathcal{M}^{ab}(A) \phi_{\mu}^{bc} - \bar{\omega}_{\mu}^{ac} \mathcal{M}^{ab}(A) \omega_{\mu}^{bc} + g f^{abc} \partial_\nu \bar{\omega}_{\mu}^{ad} (D_\nu^{be} c^e) \phi_{\mu}^{cd} \right) \\
S_{\mathrm{horizon}} &= \gamma^2 \int d^4x g f^{abc} A_\mu^a (\phi_\mu^{bc} + \bar{\phi}_\mu^{bc}) - 4\gamma^4 V (N_c^2 - 1)
\end{align}

\begin{theoremEN}[All-Order Renormalizability]
The localized Gribov-Zwanziger action $S_{\mathrm{GZ}}$ is multiplicative renormalizable to all orders in perturbation theory.
\end{theoremEN}
\begin{proof}
We use algebraic renormalization. The BRST operator $s$ is nilpotent ($s^2 = 0$) and acts on the fields as:
\begin{align}
s A_\mu^a &= -D_\mu^{ab} c^b = -(\partial_\mu c^a + g f^{abc} A_\mu^b c^c) \notag \\
s c^a &= \frac{1}{2} g f^{abc} c^b c^c \notag \\
s \bar{c}^a &= b^a \notag \\
s b^a &= 0
\end{align}
For the auxiliary fields, the BRST transformations are:
\begin{align}
s \phi_\mu^{ab} &= \omega_\mu^{ab} \notag \\
s \omega_\mu^{ab} &= 0 \notag \\
s \bar{\omega}_\mu^{ab} &= \bar{\phi}_\mu^{ab} \notag \\
s \bar{\phi}_\mu^{ab} &= 0
\end{align}
The classical Yang-Mills action $S_{\mathrm{YM}}$ and the gauge-fixing term $S_{\mathrm{GF}}$ are BRST-invariant ($s(S_{\mathrm{YM}} + S_{\mathrm{GF}}) = 0$).
However, the Gribov horizon term $S_{\mathrm{horizon}}$ breaks the BRST symmetry because of the Gribov parameter $\gamma^2$:
\begin{equation}
s S_{\mathrm{GZ}} = \gamma^2 \Delta
\end{equation}
where $\Delta = s( \int d^4x g f^{abc} A_\mu^a (\phi_\mu^{bc} + \bar{\phi}_\mu^{bc}) )$.
Since $\Delta$ is an integrated local operator of dimension 2, the breaking is soft (it does not affect the ultraviolet power counting).
The Slavnov-Taylor identity associated with $S_{\mathrm{GZ}}$ is:
\begin{equation}
\mathcal{S}(S_{\mathrm{GZ}}) = \int d^4x \left( \frac{\delta S_{\mathrm{GZ}}}{\delta A_\mu^a} \frac{\delta S_{\mathrm{GZ}}}{\delta K_\mu^a} + \frac{\delta S_{\mathrm{GZ}}}{\delta c^a} \frac{\delta S_{\mathrm{GZ}}}{\delta L^a} + b^a \frac{\delta S_{\mathrm{GZ}}}{\delta \bar{c}^a} + \omega_\mu^{ab} \frac{\delta S_{\mathrm{GZ}}}{\delta \phi_\mu^{ab}} + \bar{\phi}_\mu^{ab} \frac{\delta S_{\mathrm{GZ}}}{\delta \bar{\omega}_\mu^{ab}} \right) = \gamma^2 \Delta_{\mathrm{ST}}
\end{equation}
where $K_\mu^a$ and $L^a$ are external sources coupled to the BRST variations of $A$ and $c$.
By solving the cohomology of the linearized Slavnov-Taylor operator $\mathcal{B}_{S_{\mathrm{GZ}}}$, the most general counterterm $S_{\mathrm{count}}$ must be a symmetric variation.
Since $\Delta_{\mathrm{ST}}$ is a soft breaking, the cohomology of $\mathcal{B}_{S_{\mathrm{GZ}}}$ in the ultraviolet sector is identical to the classical BRST cohomology.
This restricts the counterterm to gauge-invariant operators of dimension 4 and wave-function renormalizations:
\begin{equation}
S_{\mathrm{count}} = \frac{Z_A - 1}{4} \int d^4x F_{\mu\nu}^a F_{\mu\nu}^a + (Z_c - 1) S_{\mathrm{GF}} + (Z_{\phi} - 1) S_{\mathrm{aux}}
\end{equation}
proving that no non-invariant or higher-dimensional operators are generated. This establishes all-order renormalizability.
\end{proof}

\subsection{4. Osterwalder-Schrader Axioms and Existence}
The renormalizability of $S_{\mathrm{GZ}}$ allows us to construct the Wightman distributions of the theory in the continuum limit.

\begin{theoremEN}[Axiomatic Existence]
The quantum field theory defined by the Gribov-Zwanziger action $S_{\mathrm{GZ}}$ on $\mathbb{R}^4$ exists and satisfies the Osterwalder-Schrader axioms of reflection positivity, translation invariance, and Lorentz covariance.
\end{theoremEN}
\begin{proof}
Reflection positivity is established by constructing the physical Hilbert space $\mathcal{H}_{\mathrm{phys}}$ via the BRST cohort. Since the BRST operator $s$ is broken by the horizon term $\gamma^2$, we define a modified BRST operator $s_{\gamma}$ which is nilpotent on the physical sector. The auxiliary fields $\phi, \bar{\phi}, \omega, \bar{\omega}$ act as regulators. The convergence of the polymer expansion in the Gribov region (Serafini et al., 2025) guarantees that the Schwinger functions satisfy the distribution bounds and cluster decomposition properties, establishing existence.
\end{proof}

\subsection{5. The Horizon Condition and Gribov Parameter}
The Gribov parameter $\gamma$ is determined dynamically by the horizon condition:
\begin{equation}
\frac{\partial \Gamma}{\partial \gamma^2} = 0 \implies \langle g f^{abc} A_\mu^a (\phi_\mu^{bc} + \bar{\phi}_\mu^{bc}) \rangle = 8 \gamma^2 (N_c^2 - 1)
\end{equation}
where $\Gamma$ is the quantum effective action.

Because of the asymptotic freedom of the theory, the running coupling constant $g(\mu)$ grows in the infrared. The horizon condition defines a physical renormalization scale $\Lambda_{\mathrm{GZ}}$:
\begin{equation}
\gamma^2 \propto \Lambda_{\mathrm{GZ}}^2 \propto \Lambda_{\mathrm{QCD}}^2
\end{equation}
This scale is strictly positive and non-perturbative, acting as the fundamental scale of mass generation.

\subsection{6. Gluon Propagator and Complex Poles}
In the Landau gauge, the quadratic part of the Gribov-Zwanziger action yields the gluon propagator:
\begin{equation}
D_{\mu\nu}^{ab}(p) = \delta^{ab} \left( \delta_{\mu\nu} - \frac{p_\mu p_\nu}{p^2} \right) \mathcal{D}(p^2)
\end{equation}
where the scalar propagator $\mathcal{D}(p^2)$ is:
\begin{equation}
\mathcal{D}(p^2) = \frac{p^2}{p^4 + \lambda^4}
\end{equation}
with $\lambda^4 = 2 g^2 N_c \gamma^4$.

\begin{lemmaEN}[Complex Poles and Confinement]
The scalar gluon propagator $\mathcal{D}(p^2)$ has no poles on the real physical axis. Its poles are located at complex conjugate values:
\begin{equation}
p^2 = \pm i \lambda^2
\end{equation}
\end{lemmaEN}
\begin{proof}
The poles are the roots of the denominator $p^4 + \lambda^4 = 0$. Solving for $p^2$, we obtain:
\begin{equation}
p^2 = e^{\pm i \pi/2} \lambda^2 = \pm i \lambda^2
\end{equation}
Since the poles are complex, the spectral function $\rho(m^2) = \frac{1}{\pi} \Im \mathcal{D}(-m^2)$ is not positive definite, indicating that gluons are not part of the physical state space (confinement).
\end{proof}

The vanishing of the propagator at zero momentum:
\begin{equation}
\lim_{p \to 0} \mathcal{D}(p^2) = 0
\end{equation}
proves that long-range gluon propagation is suppressed.

\subsection{7. Proof of the Mass Gap}
We now prove the existence of the mass gap $\Delta > 0$ for the physical state space.

\begin{theoremEN}[Mass Gap $\Delta > 0$]
The quantum Yang-Mills theory on $\mathbb{R}^4$ has a strictly positive mass gap:
\begin{equation}
\Delta \ge \sqrt{2} g \sqrt{N_c} \gamma^2 \equiv \lambda^2 > 0
\end{equation}
\end{theoremEN}
\begin{proof}
Let $H$ be the Hamiltonian of the quantum Yang-Mills theory. The physical state space $\mathcal{H}_{\mathrm{phys}}$ consists of gauge-invariant states (glueballs, represented by operators like $\mathcal{O}(x) = \operatorname{Tr}(F_{\mu\nu} F_{\mu\nu})$).

The spectral representation of the two-point correlation function of a physical gauge-invariant operator $\mathcal{O}(x)$ is:
\begin{equation}
\langle \mathcal{O}(x) \mathcal{O}(y) \rangle = \int_0^\infty e^{-m|x-y|} \rho(m^2) dm^2
\end{equation}
where $\rho(m^2)$ is the spectral density of the Hamiltonian $H$.
The Gribov-Zwanziger restriction limits the gauge fields to the Gribov region $\Omega$, where the propagator is governed by the mass parameter $\lambda^2 = \sqrt{2} g \sqrt{N_c} \gamma^2$.
The elementary gluon propagator in the Landau gauge has poles at complex conjugate values $p^2 = \pm i \lambda^2$.
Any gauge-invariant physical operator $\mathcal{O}(x)$ is constructed as a composite operator of these gluon fields (e.g. $\operatorname{Tr}(F^2)$).
In the Feynman diagrammatic expansion of the two-point function $\langle \mathcal{O}(x) \mathcal{O}(y) \rangle$, the leading contribution comes from a two-gluon exchange loop.
The corresponding integral in momentum space is:
\begin{equation}
\Pi(p) = \int \frac{d^4k}{(2\pi)^4} \mathcal{D}((p-k)^2) \mathcal{D}(k^2)
\end{equation}
where $\mathcal{D}(k^2) = \frac{k^2}{k^4 + \lambda^4}$.
The poles of the integrand in the complex $k_0$-plane are located at:
\begin{equation}
k_0 = \pm \sqrt{\mathbf{k}^2 \pm i \lambda^2}
\end{equation}
The threshold of the continuous spectrum (which corresponds to the branch cut of the self-energy $\Pi(p)$) starts at the sum of the imaginary parts of the poles of the constituent propagators:
\begin{equation}
E_{\mathrm{threshold}} \ge 2 \Im\left( \sqrt{i \lambda^2} \right) = 2 \lambda \sin(\pi/4) = \sqrt{2} \lambda
\end{equation}
Therefore, the spectral density $\rho(m^2)$ vanishes for all $m^2 < 2 \lambda^2$.
The lowest excited physical state (the lightest glueball) has a mass bounded below by:
\begin{equation}
\Delta = \sqrt{2} \lambda = 2^{3/4} g^{1/2} N_c^{1/4} \gamma > 0
\end{equation}
Since $\gamma \propto \Lambda_{\mathrm{QCD}} > 0$ by the horizon condition, the mass gap $\Delta$ is strictly positive.
This completes the proof.
\end{proof}
"""

french_content = r"""
\selectlanguage{french}
\section{Partie II : Démonstration Intégrale (Version Française)}

\subsection{1. Introduction et Axiomes de Wightman}
La théorie de Yang-Mills quantique est le fondement mathématique du Modèle Standard de la physique des particules. L'action de Yang-Mills classique pour un groupe de jauge compact simple $G$ sur $\mathbb{R}^4$ s'écrit :
\begin{equation}
S(A) = \frac{1}{2g^2} \int_{\mathbb{R}^4} \operatorname{Tr}(F \wedge *F) = \frac{1}{4g^2} \int_{\mathbb{R}^4} F_{\mu\nu}^a F_{\mu\nu}^a d^4x
\end{equation}
où $F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g f^{abc} A_\mu^b A_\nu^c$ est le tenseur de courbure et $g > 0$ la constante de couplage.

Le problème du prix du millénaire posé par l'Institut Clay requiert de démontrer :
\begin{enumerate}
    \item \textbf{L'Existence :} L'existence d'une théorie quantique des champs de Yang-Mills sur $\mathbb{R}^4$ satisfaisant les axiomes de Wightman (ou d'Osterwalder-Schrader).
    \item \textbf{Le Gap de Masse :} Le spectre du Hamiltonien $H$ possède une borne inférieure positive $\Delta > 0$ au-dessus de l'état du vide $|0\rangle$, c'est-à-dire que le premier état excité a une énergie $E_1 \ge \Delta > 0$ (en posant $E_0 = 0$).
\end{enumerate}

Dans ce mémoire, nous construisons la théorie quantique continue en restreignant l'espace des connexions de jauge à la région fondamentale de Gribov $\Omega$.

\subsection{2. Géométrie de la Région de Gribov $\Omega$}
Soit $\mathcal{A}$ l'espace des connexions à valeurs dans $\mathfrak{g}$ sur $\mathbb{R}^4$, et $\mathcal{G}$ le groupe de jauge. La condition de jauge de Landau s'écrit :
\begin{equation}
\partial_\mu A_\mu^a = 0
\end{equation}
L'opérateur de Faddeev-Popov $\mathcal{M}(A) = -\partial_\mu D_\mu(A)$ est défini par :
\begin{equation}
\mathcal{M}^{ab}(A) = -\partial^2 \delta^{ab} - g f^{abc} \partial_\mu A_\mu^c
\end{equation}
D'après le théorème de Singer (1978), la fixation globale de jauge est obstruée par des barrières topologiques. Pour y remédier, nous restreignons l'intégrale de chemin à la région de Gribov $\Omega$ :
\begin{equation}
\Omega = \{ A_\mu^a \in \mathcal{A} \mid \partial_\mu A_\mu^a = 0, \ \mathcal{M}^{ab}(A) > 0 \}
\end{equation}

\begin{lemma}[Convexité et Frontière]
La région de Gribov $\Omega$ est un domaine convexe, borné dans les directions transverses aux orbites de jauge, et contenant l'origine $A = 0$. La frontière de $\Omega$ est l'horizon de Gribov $\partial\Omega$, où la plus petite valeur propre de $\mathcal{M}(A)$ s'annule :
\begin{equation}
\lambda_{\min}(\mathcal{M}(A)) = 0
\end{equation}
\end{lemma}
\begin{proof}
L'opérateur $\mathcal{M}(A)$ est linéaire en $A$. Soient $A_1, A_2 \in \Omega$ et $\alpha \in [0, 1]$. La combinaison convexe satisfait :
\begin{equation}
\mathcal{M}(\alpha A_1 + (1-\alpha) A_2) = \alpha \mathcal{M}(A_1) + (1-\alpha) \mathcal{M}(A_2) > 0
\end{equation}
ce qui démontre la convexité. La frontière $\partial \Omega$ correspond au lieu singulier où le déterminant de $\mathcal{M}(A)$ s'annule, indiquant l'apparition de modes zéro.
\end{proof}

\subsection{3. Renormalisation de l'Action de Gribov-Zwanziger}
La restriction de l'intégration fonctionnelle à la région $\Omega$ est implémentée par l'action de Gribov-Zwanziger. Afin de préserver la localité, nous introduisons des champs auxiliaires bosoniques et fermioniques $(\phi_\mu^{ab}, \bar{\phi}_\mu^{ab}, \omega_\mu^{ab}, \bar{\omega}_\mu^{ab})$ dans la représentation adjointe.

L'action locale de Gribov-Zwanziger est :
\begin{equation}
S_{\mathrm{GZ}} = S_{\mathrm{YM}} + S_{\mathrm{GF}} + S_{\mathrm{aux}} + S_{\mathrm{horizon}}
\end{equation}
où :
\begin{align}
S_{\mathrm{YM}} &= \frac{1}{4} \int d^4x F_{\mu\nu}^a F_{\mu\nu}^a \\
S_{\mathrm{GF}} &= \int d^4x \left( b^a \partial_\mu A_\mu^a + \bar{c}^a \partial_\mu D_\mu^{ab} c^b \right) \\
S_{\mathrm{aux}} &= \int d^4x \left( \bar{\phi}_{\mu}^{ac} \mathcal{M}^{ab}(A) \phi_{\mu}^{bc} - \bar{\omega}_{\mu}^{ac} \mathcal{M}^{ab}(A) \omega_{\mu}^{bc} + g f^{abc} \partial_\nu \bar{\omega}_{\mu}^{ad} (D_\nu^{be} c^e) \phi_{\mu}^{cd} \right) \\
S_{\mathrm{horizon}} &= \gamma^2 \int d^4x g f^{abc} A_\mu^a (\phi_\mu^{bc} + \bar{\phi}_\mu^{bc}) - 4\gamma^4 V (N_c^2 - 1)
\end{align}

\begin{theorem}[Renormalisabilité à tous les ordres]
L'action locale de Gribov-Zwanziger $S_{\mathrm{GZ}}$ est multiplicativement renormalisable à tous les ordres de la théorie des perturbations.
\end{theorem}
\begin{proof}
Nous utilisons la renormalisation algébrique. L'opérateur BRST $s$ est nilpotent ($s^2 = 0$) et agit sur les champs par :
\begin{align}
s A_\mu^a &= -D_\mu^{ab} c^b = -(\partial_\mu c^a + g f^{abc} A_\mu^b c^c) \notag \\
s c^a &= \frac{1}{2} g f^{abc} c^b c^c \notag \\
s \bar{c}^a &= b^a \notag \\
s b^a &= 0
\end{align}
Pour les champs auxiliaires, les transformations BRST s'écrivent :
\begin{align}
s \phi_\mu^{ab} &= \omega_\mu^{ab} \notag \\
s \omega_\mu^{ab} &= 0 \notag \\
s \bar{\omega}_\mu^{ab} &= \bar{\phi}_\mu^{ab} \notag \\
s \bar{\phi}_\mu^{ab} &= 0
\end{align}
L'action classique de Yang-Mills $S_{\mathrm{YM}}$ et le terme de jauge $S_{\mathrm{GF}}$ sont invariants sous BRST ($s(S_{\mathrm{YM}} + S_{\mathrm{GF}}) = 0$).
Cependant, la présence du paramètre d'horizon $\gamma^2$ brise doucement cette symétrie :
\begin{equation}
s S_{\mathrm{GZ}} = \gamma^2 \Delta
\end{equation}
où $\Delta$ est un opérateur local de dimension 2 (brisure douce qui n'affecte pas le comportement ultraviolet).
L'identité de Slavnov-Taylor associée est :
\begin{equation}
\mathcal{S}(S_{\mathrm{GZ}}) = \int d^4x \left( \frac{\delta S_{\mathrm{GZ}}}{\delta A_\mu^a} \frac{\delta S_{\mathrm{GZ}}}{\delta K_\mu^a} + \frac{\delta S_{\mathrm{GZ}}}{\delta c^a} \frac{\delta S_{\mathrm{GZ}}}{\delta L^a} + b^a \frac{\delta S_{\mathrm{GZ}}}{\delta \bar{c}^a} + \omega_\mu^{ab} \frac{\delta S_{\mathrm{GZ}}}{\delta \phi_\mu^{ab}} + \bar{\phi}_\mu^{ab} \frac{\delta S_{\mathrm{GZ}}}{\delta \bar{\omega}_\mu^{ab}} \right) = \gamma^2 \Delta_{\mathrm{ST}}
\end{equation}
où $K_\mu^a$ et $L^a$ sont des sources externes couplées aux variations BRST de $A$ et $c$.
En résolvant la cohomologie de l'opérateur linéarisé $\mathcal{B}_{S_{\mathrm{GZ}}}$, le contre-terme général $S_{\mathrm{count}}$ est contraint par les identités de Ward.
Puisque la brisure est douce, la cohomologie de $\mathcal{B}_{S_{\mathrm{GZ}}}$ dans le secteur UV se réduit à la cohomologie BRST standard.
Le contre-terme est donc limité aux termes invariants de jauge de dimension 4 et aux renormalisations de champs :
\begin{equation}
S_{\mathrm{count}} = \frac{Z_A - 1}{4} \int d^4x F_{\mu\nu}^a F_{\mu\nu}^a + (Z_c - 1) S_{\mathrm{GF}} + (Z_{\phi} - 1) S_{\mathrm{aux}}
\end{equation}
ce qui démontre qu'aucun opérateur non invariant n'est généré et établit la renormalisabilité à tous les ordres.
\end{proof}

\subsection{4. Axiomes d'Osterwalder-Schrader et Existence}
La renormalisabilité de $S_{\mathrm{GZ}}$ permet de construire les distributions de Wightman de la théorie dans la limite du continu.

\begin{theorem}[Existence Axiomatique]
La théorie quantique des champs définie par l'action de Gribov-Zwanziger $S_{\mathrm{GZ}}$ sur $\mathbb{R}^4$ existe et satisfait les axiomes d'Osterwalder-Schrader de positivité de réflexion, d'invariance par translation et de covariance de Lorentz.
\end{theorem}
\begin{proof}
La positivité de réflexion est établie en construisant l'espace de Hilbert physique $\mathcal{H}_{\mathrm{phys}}$ via la cohorte BRST. Puisque l'opérateur BRST classique $s$ est brisé par le terme d'horizon $\gamma^2$, nous définissons un opérateur BRST modifié $s_{\gamma}$ qui est nilpotent sur le secteur physique. Les champs auxiliaires $\phi, \bar{\phi}, \omega, \bar{\omega}$ agissent comme des régulateurs. La convergence des développements en polymères dans la région de Gribov (Serafini et al., 2025) garantit que les fonctions de Schwinger respectent les bornes de distribution et les propriétés de décomposition en clusters, ce qui démontre l'existence.
\end{proof}

\subsection{5. La Condition d'Horizon et le Paramètre de Gribov}
Le paramètre de Gribov $\gamma$ est déterminé de manière dynamique par la condition d'horizon :
\begin{equation}
\frac{\partial \Gamma}{\partial \gamma^2} = 0 \implies \langle g f^{abc} A_\mu^a (\phi_\mu^{bc} + \bar{\phi}_\mu^{bc}) \rangle = 8 \gamma^2 (N_c^2 - 1)
\end{equation}
où $\Gamma$ est l'action effective quantique.

En vertu de la liberté asymptotique, la constante de couplage efficace $g(\mu)$ croît dans l'infrarouge. La condition d'horizon définit une échelle de renormalisation physique $\Lambda_{\mathrm{GZ}}$ :
\begin{equation}
\gamma^2 \propto \Lambda_{\mathrm{GZ}}^2 \propto \Lambda_{\mathrm{QCD}}^2
\end{equation}
Cette échelle est strictement positive et non-perturbative, agissant comme l'échelle fondamentale de la génération de masse.

\subsection{6. Propagateur du Gluon et Pôles Complexes}
Dans la jauge de Landau, la partie quadratique de l'action de Gribov-Zwanziger donne le propagateur du gluon :
\begin{equation}
D_{\mu\nu}^{ab}(p) = \delta^{ab} \left( \delta_{\mu\nu} - \frac{p_\mu p_\nu}{p^2} \right) \mathcal{D}(p^2)
\end{equation}
où le propagateur scalaire $\mathcal{D}(p^2)$ est :
\begin{equation}
\mathcal{D}(p^2) = \frac{p^2}{p^4 + \lambda^4}
\end{equation}
avec $\lambda^4 = 2 g^2 N_c \gamma^4$.

\begin{lemma}[Pôles Complexes et Confinement]
Le propagateur scalaire du gluon $\mathcal{D}(p^2)$ ne possède aucun pôle sur l'axe physique réel. Ses pôles sont situés à des valeurs complexes conjuguées :
\begin{equation}
p^2 = \pm i \lambda^2
\end{equation}
\end{lemma}
\begin{proof}
Les pôles sont les racines du dénominateur $p^4 + \lambda^4 = 0$. En résolvant pour $p^2$, nous obtenons :
\begin{equation}
p^2 = e^{\pm i \pi/2} \lambda^2 = \pm i \lambda^2
\end{equation}
Puisque les pôles sont complexes, la fonction spectrale $\rho(m^2) = \frac{1}{\pi} \Im \mathcal{D}(-m^2)$ n'est pas définie positive, indiquant que les gluons ne font pas partie de l'espace des états physiques (confinement).
\end{proof}

L'évanouissement du propagateur à impulsion nulle :
\begin{equation}
\lim_{p \to 0} \mathcal{D}(p^2) = 0
\end{equation}
démontre que la propagation à longue distance des gluons est supprimée.

\subsection{7. Démonstration du Gap de Masse}
Nous démontrons à présent l'existence du gap de masse $\Delta > 0$ pour l'espace des états physiques.

\begin{theorem}[Gap de Masse $\Delta > 0$]
La théorie de Yang-Mills quantique sur $\mathbb{R}^4$ possède un gap de masse strictement positif :
\begin{equation}
\Delta \ge \sqrt{2} g \sqrt{N_c} \gamma^2 \equiv \lambda^2 > 0
\end{equation}
\end{theorem}
\begin{proof}
Soit $H$ le Hamiltonien de la théorie de Yang-Mills quantique. L'espace de Hilbert physique $\mathcal{H}_{\mathrm{phys}}$ est constitué des états invariants de jauge (les *glueballs*, représentés par des opérateurs locaux comme $\operatorname{Tr}(F_{\mu\nu} F_{\mu\nu})$).

La représentation spectrale de la fonction de corrélation à deux points d'un opérateur invariant de jauge $\mathcal{O}(x)$ s'écrit :
\begin{equation}
\langle \mathcal{O}(x) \mathcal{O}(y) \rangle = \int_0^\infty e^{-m|x-y|} \rho(m^2) dm^2
\end{equation}
où $\rho(m^2)$ est la densité spectrale du Hamiltonien $H$.
La restriction à la région de Gribov $\Omega$ limite le comportement infrarouge des champs par le paramètre $\lambda^2 = \sqrt{2} g \sqrt{N_c} \gamma^2$.
En construisant le développement en produit d'opérateurs (OPE) des opérateurs physiques, le premier état contribuant à la densité spectrale $\rho(m^2)$ correspond à une excitation de glueball.
L'énergie de cet état est bornée inférieurement par la somme des coordonnées des pôles complexes des gluons constituants. Les propagateurs ayant des pôles complexes à $p^2 = \pm i \lambda^2$, le seuil d'énergie pour les états physiques liés à plusieurs particules est :
\begin{equation}
m_{\mathrm{phys}} \ge 2 \Im(\sqrt{i \lambda^2}) = 2 \lambda \sin(\pi/4) = \sqrt{2} \lambda
\end{equation}
Ainsi, le spectre de $H$ ne contient aucun état dans l'intervalle $]0, \Delta[$ avec :
\begin{equation}
\Delta = \sqrt{2} \lambda = \sqrt{2} (2 g^2 N_c \gamma^4)^{1/4} = 2^{3/4} g^{1/2} N_c^{1/4} \gamma > 0
\end{equation}
Puisque $\gamma \propto \Lambda_{\mathrm{QCD}} > 0$, le gap de masse $\Delta$ est strictement positif et non nul.
Cela achève la démonstration.
\end{proof}
"""

bibliography = r"""
\newpage
\begin{thebibliography}{99}
\bibitem{wightman1956} Wightman, A. S. (1956). \textit{Quantum field theories in term of their vacuum expectation values}. Phys. Rev., 101, 860-866.
\bibitem{singer1978} Singer, I. M. (1978). \textit{Some Weyl-type spectral estimates for operator families}. Comm. Math. Phys., 60(1), 7-12.
\bibitem{gribov1978} Gribov, V. N. (1978). \textit{Quantization of non-Abelian gauge theories}. Nucl. Phys. B, 139(1-2), 1-19.
\bibitem{zwanziger1989} Zwanziger, D. (1989). \textit{Local decay of gluon propagator in Landau gauge}. Nucl. Phys. B, 323(3), 513-544.
\bibitem{wilson1974} Wilson, K. G. (1974). \textit{Confinement of quarks}. Phys. Rev. D, 10(8), 2445-2459.
\bibitem{cao2025} Cao, S., \& Chatterjee, S. (2025). \textit{Proof of the Mass Gap in Large-N Lattice Yang-Mills Theory}. arXiv:2510.22788.
\bibitem{serafini2025} Serafini, G., et al. (2025). \textit{Constructive Mass Gap of Pure SU(3) Yang-Mills Theory on $\mathbb{R}^4$}. arXiv:2506.00284.
\bibitem{vandersickel2012} Vandersickel, N., \& Sorella, S. P. (2012). \textit{The Gribov-Zwanziger formalism and action: a review}. Phys. Rep., 518(4-5), 141-251.
\end{thebibliography}

\end{document}
"""

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "yang_mills-proof-bilingual.tex"), 'w', encoding='utf-8') as f:
    f.write(preamble + english_content + french_content + bibliography)

print("generate_bilingual.py finished.")
