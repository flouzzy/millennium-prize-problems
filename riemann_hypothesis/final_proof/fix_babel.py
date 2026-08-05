import os
import sys

def fix_babel_content(content):
    # Regex needs to match the \addto\captions... and its following curly brace block
    # This non-greedy match works as long as the braces are reasonably balanced for the test
    # A simple but more accurate regex for these specific tests:

    # We can match \addto\captionsfrench followed by { ... }
    # Using a loop or matching everything inside { until the closing }
    # but balancing braces in regex is hard. Let's just find and replace the block by simple string matching.

    import re
    def remove_block(text, block_name):
        escaped_block = re.escape(block_name)
        pattern = escaped_block + r'\s*\{([^\{\}]|\{[^\{\}]*\})*\}'
        return re.sub(pattern, '', text)

    content = remove_block(content, r'\addto\captionsfrench')
    content = remove_block(content, r'\addto\captionsenglish')

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

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "riemann_hypothesis-proof-bilingual.tex"), 'r', encoding='utf-8') as f:
        content = f.read()

    content = fix_babel_content(content)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "riemann_hypothesis-proof-bilingual.tex"), 'w', encoding='utf-8') as f:
        f.write(content)
