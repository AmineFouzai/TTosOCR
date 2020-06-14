from PIL import Image,ImageDraw,ImageFont
from uuid import uuid4
import qrcode
import pytesseract
import sys
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img=Image.open(sys.argv[1],'r')

text=pytesseract.image_to_string(img,lang="eng")

print(text)

