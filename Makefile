.PHONY: all clean cleanall

TARGET=0-0-main.tex

all:
	@rubber -I /usr/local/texlive/2022/texmf-dist/tex --pdf -W all --module biber $(TARGET)

clean:
	@rubber -I /usr/local/texlive/2022/texmf-dist/tex --clean $(TARGET)

cleanall:
	@rubber -I /usr/local/texlive/2022/texmf-dist/tex --clean --pdf $(TARGET)

