#!/usr/bin/env bash
pdflatex -synctex=1 -interaction=nonstopmode thoughts.tex
bibtex thoughts.aux
makeindex thoughts.idx
makeglossaries thoughts
pdflatex -synctex=1 -interaction=nonstopmode thoughts.tex
