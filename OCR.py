##while executing the programme we must pass the image file as command line argument.

from PIL import Image
from pytesseract import image_to_string

print image_to_string(Image.open("image_name.png")
