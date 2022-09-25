
import PIL
import fitz

basefile = "/py/skeat/one-time-load/input_images/3rdEditionSkeat.pdf"


doc = fitz.open(basefile)


matrix = fitz.Matrix(2.2, 2.2)

for page_num, page in enumerate(doc.pages(39, 763), start=2):
    pmap = page.get_pixmap(matrix=matrix)
    with open(f"/py/skeat/one-time-load/data/webp_pages/page_{page_num}.webp", "wb") as outf:
        pmap.pil_save(outf, format="WEBP")


