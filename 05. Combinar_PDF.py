#pip install pypdf
from pypdf import PdfMerger

merger = PdfMerger()

lista = ['arquivo1.pdf', 'arquivo2.pdf', 'arquivo3.pdf']

for pdf in lista:
    merger.append(pdf)

merger.write("novo_nome.pdf")
merger.close()






