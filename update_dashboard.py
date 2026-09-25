with open("dashboard.md", "r", encoding="utf-8") as f:
    content = f.read()

target = "### 2026-09-23-14h\n\n- [[#2026-09-23-14h|2026-09-23 14:00]] : [Red Teaming & Prototypage] - Problème: L'hypothèse de Riemann. Résistance du blueprint validée face aux contre-exemples classiques. Cadre symbolique figé dans draft_setup.tex. Statut : Prêt.\n"

if "2026-09-24-14h" not in content:
    replacement = "### 2026-09-24-14h\n\n- [[#2026-09-24-14h|2026-09-24 14:00]] : [Red Teaming & Prototypage] - Problème: L'hypothèse de Riemann. Résistance du blueprint validée face aux contre-exemples classiques. Cadre symbolique figé dans draft_setup.tex. Statut : Prêt.\n\n" + target
    new_content = content.replace(target, replacement)

    with open("dashboard.md", "w", encoding="utf-8") as f:
        f.write(new_content)

print("Done")
