# this is to handle extract of pages 1 at a time
# STEP1 breaks the document into single pages
# STEP2 chops off the top 70 bits
# STEP3 reads that with tesseract

from PyPDF2 import PdfFileReader, PdfFileWriter
import subprocess

pdf_file_path = '/py/skeat/input_images/3rdEditionSkeat.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfFileReader(pdf_file_path)

import fitz

PAGE_OFFSET = 37


for page_num in range(300, 802):
    pdfWriter = PdfFileWriter()
    pdfWriter.addPage(pdf.getPage(page_num))
    page_name = f'skeat_{page_num - PAGE_OFFSET}.pdf'
    with open(page_name, 'wb') as f:
        pdfWriter.write(f)


    with fitz.open(page_name) as doc:
        a = next(doc.pages())
        clip = fitz.Rect(0, 0, 800, 70)
        pix = a.get_pixmap(clip=clip, matrix=fitz.Matrix(4, 4))
        png_file = f"{page_name.split('.')[0]}.png"
        pix.save(png_file)

    subprocess.run(["tesseract", png_file, f"{png_file.split('.')[0]}"])


