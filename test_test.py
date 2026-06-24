import os
import sys
import subprocess
import unittest

class TestTestScript(unittest.TestCase):
    def test_missing_dashboard(self):
        # temporarily move dashboard.md
        if os.path.exists('dashboard.md'):
            os.rename('dashboard.md', 'dashboard.md.bak')
        try:
            result = subprocess.run([sys.executable, 'test.py'], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue('FileNotFoundError' in result.stderr or 'No such file or directory' in result.stderr)
        finally:
            if os.path.exists('dashboard.md.bak'):
                os.rename('dashboard.md.bak', 'dashboard.md')

if __name__ == '__main__':
    unittest.main()
