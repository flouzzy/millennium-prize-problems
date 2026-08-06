import sys

def replace_in_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    target = 'os.path.join(os.path.dirname(os.path.abspath(__file__)), "riemann_hypothesis-proof-bilingual.tex")'
    target2 = "os.path.join(os.path.dirname(os.path.abspath(__file__)), 'riemann_hypothesis-proof-bilingual.tex')"

    if target in content or target2 in content:
        if 'import os' in content and 'from utils import get_tex_path' not in content:
            content = content.replace('import os', 'import os\nfrom utils import get_tex_path', 1)

        content = content.replace(target, 'get_tex_path("riemann_hypothesis-proof-bilingual.tex")')
        content = content.replace(target2, 'get_tex_path("riemann_hypothesis-proof-bilingual.tex")')

        with open(filename, 'w') as f:
            f.write(content)

for f in sys.argv[1:]:
    replace_in_file(f)
