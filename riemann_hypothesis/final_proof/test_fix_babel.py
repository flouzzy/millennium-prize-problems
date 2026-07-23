import unittest
from fix_babel import fix_babel_content

class TestFixBabel(unittest.TestCase):
    def test_fix_babel_happy_path(self):
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
        self.assertNotIn("OldResume", result)
        self.assertNotIn("OldAbstract", result)

        # We should have exactly the newly injected \setlocalecaption
        self.assertIn(r"\setlocalecaption{french}{abstract}{Résumé}", result)
        self.assertIn(r"\hypersetup{", result)
        # Make sure new block is inserted exactly once before \hypersetup
        self.assertEqual(result.count(r"\makeatletter"), 1)
        self.assertLess(result.find(r"\makeatletter"), result.find(r"\hypersetup{"))

    def test_fix_babel_nested_braces(self):
        content = r"""
\addto\captionsfrench{\renewcommand{\abstractname}{NestedResume}}
\hypersetup{
}
"""
        result = fix_babel_content(content)
        self.assertNotIn("NestedResume", result)
        self.assertNotIn(r"\renewcommand{\abstractname}{NestedResume}", result)

    def test_fix_babel_multiple_occurrences(self):
        content = r"""
\addto\captionsfrench{test_multiple_f1}
\addto\captionsenglish{test_multiple_e1}
some text
\addto\captionsfrench{test_multiple_f2}
\hypersetup{
}
"""
        result = fix_babel_content(content)
        self.assertNotIn("test_multiple_f1", result)
        self.assertNotIn("test_multiple_e1", result)
        self.assertNotIn("test_multiple_f2", result)
        self.assertIn("some text", result)

    def test_fix_babel_missing_hypersetup(self):
        content = r"""
\addto\captionsfrench{test_missing}
just some other content
"""
        result = fix_babel_content(content)
        self.assertNotIn("test_missing", result)
        self.assertIn("just some other content", result)
        # Because \hypersetup is missing, new_babel_fixes won't be added
        self.assertNotIn(r"\makeatletter", result)

if __name__ == '__main__':
    unittest.main()

