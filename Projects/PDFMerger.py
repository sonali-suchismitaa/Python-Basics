import PyPDF2

pdfFiles = [r"C:\Users\KIIT\Downloads\10165643_2022_010 (2).pdf",r"C:\Users\KIIT\Downloads\10165643_2022_020 (2).pdf"]

merger = PyPDF2.PdfMerger()

for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write("Merged.pdf")