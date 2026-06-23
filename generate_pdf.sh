#!/bin/bash

# Script to generate PDF files from markdown files using pandoc

# French version
pandoc riemann_hypothesis/inprogress/01-fibration_motivique_fr.md -o riemann_hypothesis/preuve_fibration_motivique_01_fr.pdf --pdf-engine=pdflatex -V geometry:margin=1in &

# English version
pandoc riemann_hypothesis/inprogress/01-fibration_motivique_en.md -o riemann_hypothesis/preuve_fibration_motivique_01_en.pdf --pdf-engine=pdflatex -V geometry:margin=1in &

wait

echo "PDF generation complete."
