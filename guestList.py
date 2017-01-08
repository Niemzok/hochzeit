from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

drawing = svg2rlg("Inlay0.svg")
#renderPDF.drawToFile(drawing, "Inlay0.pdf")