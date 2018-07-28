from PIL import Image
from pytesseract import image_to_string
from wand.image import Image as Img

with Img(filename='resume.pdf', resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='out.jpg')

print(image_to_string(Image.open('out.jpg')))
