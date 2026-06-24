import os
import re

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "riemann_hypothesis-proof-bilingual.tex"), 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old addto block
content = re.sub(r'\\addto\\captionsfrench\{.*?\}', '', content, flags=re.DOTALL)
content = re.sub(r'\\addto\\captionsenglish\{.*?\}', '', content, flags=re.DOTALL)

# Add correct setlocalecaption
new_babel_fixes = r"""
\makeatletter
\@ifpackagelater{babel}{2021/01/01}{
  \setlocalecaption{french}{abstract}{Résumé}
  \setlocalecaption{french}{proof}{Démonstration}
  \setlocalecaption{english}{abstract}{Abstract}
  \setlocalecaption{english}{proof}{Proof}
}{
  \addto\captionsfrench{
    \renewcommand{\abstractname}{Résumé}
    \renewcommand{\proofname}{Démonstration}
  }
  \addto\captionsenglish{
    \renewcommand{\abstractname}{Abstract}
    \renewcommand{\proofname}{Proof}
  }
}
\makeatother
"""

content = content.replace(r"\hypersetup{", new_babel_fixes + "\n" + r"\hypersetup{")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "riemann_hypothesis-proof-bilingual.tex"), 'w', encoding='utf-8') as f:
    f.write(content)
