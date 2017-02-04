#!/usr/bin/python
import sys
from reportlab.pdfgen import canvas

"""
Usage:
pip install -r reqs.txt
chmod +x py2pdf.py
./py2pdf (name of the pdf) (text of the new pdf)
"""

name = str(sys.argv[1:3])
content =str(sys.argv[3:])

def add_extension(name):
    if (lambda name: name.rfind('.pdf', -4)) == -1:
        name += '.pdf'
    return name 

def line_loop(content, index):
    max_line = 0
    output = ""
    while max_line < 80:
        output += content[index]
        index += 1
        max_line += 1
    output += "\n"
    max_line = 0

def format_with_linebreaks(content):
    index = 0
    line_loop(content=content, index=index)


canvas = canvas.Canvas(name)

canvas.drawString(100, 100, content)
canvas.showPage()
canvas.save()
