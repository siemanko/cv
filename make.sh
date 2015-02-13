cd build/
cp ../*.tex ../*.py ./ &&
cp ../images/* ./ &&
xelatex cv.tex &&
pythontex --interpreter=python:/usr/bin/python3 cv.tex &&
xelatex cv.tex &&
cp cv.pdf ../

 cd ..
