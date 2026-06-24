import pytest
from fix_babel import fix_babel_content

def test_fix_babel_happy_path():
    content = r"""\documentclass{article}
\addto\captionsfrench{
    \renewcommand{\abstractname}{OldResume}
    \renewcommand{\proofname}{OldDemo}
}
\addto\captionsenglish{
    \renewcommand{\abstractname}{OldAbstract}
    \renewcommand{\proofname}{OldProof}
}
\hypersetup{
    colorlinks=true
}
\begin{document}
Test
\end{document}"""

    result = fix_babel_content(content)

    # The old ones had "OldResume" etc. Those should be gone.
    assert "OldResume" not in result
    assert "OldAbstract" not in result

    # We should have exactly the newly injected \setlocalecaption
    assert r"\setlocalecaption{french}{abstract}{Résumé}" in result
    assert r"\hypersetup{" in result
    # Make sure new block is inserted exactly once before \hypersetup
    assert result.count(r"\makeatletter") == 1
    assert result.find(r"\makeatletter") < result.find(r"\hypersetup{")

def test_fix_babel_nested_braces():
    content = r"""
\addto\captionsfrench{\renewcommand{\abstractname}{NestedResume}}
\hypersetup{
}
"""
    result = fix_babel_content(content)
    assert "NestedResume" not in result
    # Check that there are no leftover braces from the nested block
    # By ensuring the output doesn't contain leftover } without a match
    # A simple check:
    assert r"\renewcommand{\abstractname}{NestedResume}" not in result

def test_fix_babel_multiple_occurrences():
    content = r"""
\addto\captionsfrench{test_multiple_f1}
\addto\captionsenglish{test_multiple_e1}
some text
\addto\captionsfrench{test_multiple_f2}
\hypersetup{
}
"""
    result = fix_babel_content(content)
    assert "test_multiple_f1" not in result
    assert "test_multiple_e1" not in result
    assert "test_multiple_f2" not in result
    assert "some text" in result

def test_fix_babel_missing_hypersetup():
    content = r"""
\addto\captionsfrench{test_missing}
just some other content
"""
    result = fix_babel_content(content)
    assert "test_missing" not in result
    assert "just some other content" in result
    # Because \hypersetup is missing, new_babel_fixes won't be added
    assert r"\makeatletter" not in result
