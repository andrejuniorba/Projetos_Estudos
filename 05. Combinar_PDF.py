#pip install pypdf
from pypdf import PdfWriter

merger = PdfWriter()

lista = ('arquivo1.pdf', 'arquivo2.pdf', 'arquivo3.pdf')

for pdf in lista:
    merger.append(pdf)

merger.write("novo_nome.pdf")
merger.close()






