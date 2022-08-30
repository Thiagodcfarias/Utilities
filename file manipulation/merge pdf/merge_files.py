from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()
for items in os.listdir('./input'):
    if items.endswith('.pdf'):
        merger.append('./input/' + items)
        
merger.write('./output/Result.pdf')
merger.close()