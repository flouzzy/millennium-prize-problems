import re
import sys

def fix_babel_content(content: str) -> str:
    # Remove old addto block, handling one level of nested braces
    # e.g. \addto\captionsfrench{\renewcommand{\abstractname}{Résumé} ...}
    nested_braces_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'

    content = re.sub(r'\\addto\\captionsfrench' + nested_braces_pattern, '', content, flags=re.DOTALL)
    content = re.sub(r'\\addto\\captionsenglish' + nested_braces_pattern, '', content, flags=re.DOTALL)

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

    if r"\hypersetup{" in content:
        content = content.replace(r"\hypersetup{", new_babel_fixes + "\n" + r"\hypersetup{")

    return content

def main():
    file_path = '/var/www/maths-proof/millennium-prize-problems/riemann_hypothesis/final_proof/riemann_hypothesis-proof-bilingual.tex'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        content = fix_babel_content(content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
