import pytesseract
import sys
from pprint import pprint
pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe'

img=Image.open(sys.argv[1],'r')

text=pytesseract.image_to_string(img,lang="eng")

pprint(text)

