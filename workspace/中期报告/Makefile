.PHONY: all cn en clean

all: cn en

cn: Midterm_Report_CN.pdf

en: Midterm_Report_EN.pdf

Midterm_Report_CN.pdf: Midterm_Report_CN.tex report-style.sty
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build Midterm_Report_CN.tex
	cp build/Midterm_Report_CN.pdf Midterm_Report_CN.pdf

Midterm_Report_EN.pdf: Midterm_Report_EN.tex report-style-en.sty fonts/sftt1095.pfb
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build Midterm_Report_EN.tex
	cp build/Midterm_Report_EN.pdf Midterm_Report_EN.pdf

clean:
	rm -rf build
