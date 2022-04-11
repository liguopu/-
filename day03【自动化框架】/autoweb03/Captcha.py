import pytesseract
from PIL import Image

image = Image.open("member_vcode.png")
vcode = pytesseract.image_to_string(image)
print(vcode)
