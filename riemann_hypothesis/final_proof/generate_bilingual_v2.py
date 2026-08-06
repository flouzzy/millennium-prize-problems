import os

def generate_bilingual():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(base_dir, "riemann_hypothesis-proof-bilingual.tex")

    fr_path = os.path.join(base_dir, "riemann_hypothesis-proof-fr.tex")
    en_path = os.path.join(base_dir, "riemann_hypothesis-proof.tex")

    with open(fr_path, "r", encoding="utf-8") as f:
        fr_content = f.read()
    with open(en_path, "r", encoding="utf-8") as f:
        en_content = f.read()

    preamble_end = en_content.find("\\begin{document}") + len("\\begin{document}")
    preamble = en_content[:preamble_end]

    if "\\usepackage[english]{babel}" in preamble:
        preamble = preamble.replace("\\usepackage[english]{babel}", "\\usepackage[english, french]{babel}")
    elif "\\usepackage[english, french]{babel}" not in preamble:
        preamble = preamble.replace("\\usepackage[utf8]{inputenc}", "\\usepackage[utf8]{inputenc}\n\\usepackage[english, french]{babel}")

    en_body_start = preamble_end
    en_body_end = en_content.find("\\begin{thebibliography}")
    en_body = en_content[en_body_start:en_body_end].replace("\\maketitle", "").replace("\\selectlanguage{english}", "")

    fr_body_start = fr_content.find("\\begin{document}") + len("\\begin{document}")
    fr_body_end = fr_content.find("\\begin{thebibliography}")
    fr_body = fr_content[fr_body_start:fr_body_end].replace("\\maketitle", "").replace("\\selectlanguage{french}", "")

    bib_start = en_content.find("\\begin{thebibliography}")
    bibliography = en_content[bib_start:]

    bilingual_content = preamble + "\n\\maketitle\n\\tableofcontents\n\\newpage\n\\selectlanguage{english}\n\\section*{Part I: Complete Proof (English)}\n" + en_body + "\n\\newpage\n\\selectlanguage{french}\n\\section*{Partie II : Démonstration Complète (Français)}\n" + fr_body + "\n\\newpage\n" + bibliography

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(bilingual_content)

if __name__ == "__main__":
    generate_bilingual()
