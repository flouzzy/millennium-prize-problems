import unittest
from unittest.mock import patch, mock_open
import sys
import os
import importlib

class TestUpdateManuscript(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_update_manuscript_generates_files(self, mock_file):
        # Resolve the directory dynamically
        current_dir = os.path.abspath(os.path.dirname(__file__))
        if current_dir not in sys.path:
            sys.path.append(current_dir)

        # Mock print to prevent output during tests
        with patch('builtins.print') as mock_print:
            # We import the module which executes its top-level code (generating files)
            if 'update_manuscript' in sys.modules:
                importlib.reload(sys.modules['update_manuscript'])
            else:
                importlib.import_module('update_manuscript')

            # Verify that print was called at the end of the script
            mock_print.assert_called_with("Updated manuscript, generator, and README successfully.")

        handle = mock_file()

        # update_manuscript.py opens 3 files: tex_path, py_path, readme_path
        # Let's check that write was called
        self.assertTrue(handle.write.called)

        # We will iterate through the writes and verify the py file generates generate_bilingual
        wrote_py_file = False
        wrote_tex_file = False
        wrote_readme_file = False

        for call in handle.write.call_args_list:
            content = call[0][0]
            if "def generate_bilingual():" in content:
                wrote_py_file = True
                self.assertIn("import os", content)
                self.assertIn("target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"riemann_hypothesis-proof-bilingual.tex\")", content)
                self.assertIn("f.write(content)", content)
                self.assertIn("generate_bilingual()", content)
            if "\\documentclass[11pt,a4paper,twoside]{article}" in content:
                wrote_tex_file = True
            if "Programme Cohomologique pour l'Hypothèse de Riemann via les Fibrations Motiviques" in content:
                wrote_readme_file = True

        self.assertTrue(wrote_py_file, "Failed to generate python code with generate_bilingual()")
        self.assertTrue(wrote_tex_file, "Failed to generate tex file content")
        self.assertTrue(wrote_readme_file, "Failed to generate README content")

if __name__ == '__main__':
    unittest.main()
