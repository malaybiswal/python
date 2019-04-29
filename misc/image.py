from PIL import Image
from pytesseract import image_to_string

#print image_to_string(Image.open('Screen-shot-2011-01-11-at-7.37.54-PM.png'))
print image_to_string(Image.open('Screen-shot-2011-01-11-at-7.37.54-PM.png'), lang='eng')
