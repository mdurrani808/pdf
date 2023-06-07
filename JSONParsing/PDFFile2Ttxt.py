import pypdfium2 as pdfium
from pypdf import PdfReader
from pathlib import Path
import os

# Set the directory you want to start from
root_dir = 'input'
pdf_files = []
for file_name in os.listdir(root_dir):
    if file_name.endswith('.pdf'):
        pdf_files.append(os.path.join(root_dir, file_name))

content = []
for filePath in pdf_files:
    #pdf = pdfium.PdfDocument(filePath)
    reader = PdfReader(filePath)
    for page in reader.pages:
        #textpage = page.get_textpage()
        #content.append(textpage.get_text_range())
        content.append(page.extract_text())
    fileWriter = open("GenericPDFOutput\\" +
                      Path(filePath).stem+".txt", 'w', encoding="utf-16")
    fileWriter.writelines(content)
    fileWriter.close()
    content.clear()
