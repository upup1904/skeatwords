
import PIL
import fitz

FILEDIR="/py/skeat/one-time-load/data/images/"

for file in ['skeat_707.pdf',
             ]:
    doc = fitz.open(FILEDIR + file)

images = doc.get_page_images(0)    
len(images)     
i1 = images[0]

i2 = images[1]
i1
i2
help(doc)

img = doc.extract_image(5)
img["ext"]

type(img["image"])
img["width"]
img["height"]

with open("/tmp/big1.jpx",  "wb") as output:
    output.write(img["image"])


pix = fitz.Pixmap(doc, 5)

type(pix)

jpg_page_bytes =  pix.pil_tobytes(format="JPEG")

webp_page_bytes = pix.pil_tobytes(format="WEBP")




with open("/tmp/big1.jpg",  "wb") as output:
    output.write(jpg_page_bytes)

with open("/tmp/big1.webp",  "wb") as output:
    output.write(webp_page_bytes)
    
