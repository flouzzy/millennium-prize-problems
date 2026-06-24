import unittest
from unittest.mock import patch, mock_open
import sys
import os
import importlib

class TestGenerateBilingualV2(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_bilingual(self, mock_file):
        # Resolve the directory dynamically
        current_dir = os.path.abspath(os.path.dirname(__file__))
        if current_dir not in sys.path:
            sys.path.append(current_dir)

        if 'generate_bilingual_v2' in sys.modules:
            importlib.reload(sys.modules['generate_bilingual_v2'])
        else:
            import generate_bilingual_v2

        # Verify open was called with correct arguments
        mock_file.assert_called_once_with(
            '/var/www/maths-proof/millennium-prize-problems/riemann_hypothesis/final_proof/riemann_hypothesis-proof-bilingual.tex',
            'w',
            encoding='utf-8'
        )

        # Verify that write was called
        handle = mock_file()
        handle.write.assert_called()

        # Check content written
        args, kwargs = handle.write.call_args
        content_written = args[0]
        self.assertTrue(content_written.startswith(r"\documentclass[11pt,a4paper,twoside]{article}"))
        self.assertIn(r"\selectlanguage{frenchb}", content_written)
        self.assertIn(r"\selectlanguage{english}", content_written)
        self.assertIn(r"\end{document}", content_written)


if __name__ == '__main__':
    unittest.main()
