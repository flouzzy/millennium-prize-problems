import os

def get_tex_path(filename="riemann_hypothesis-proof-bilingual.tex"):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
