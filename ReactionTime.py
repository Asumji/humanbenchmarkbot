import time
import pynput

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller

keyboard = Controller()
mouse = MouseController()


for i in range(1000):
    from PIL import ImageGrab, ImageDraw
    image = ImageGrab.grab(bbox=(600, 450, 1200, 600))
    image.save('sc.png') 
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
    text = pytesseract.image_to_string(Image.open("sc.png"))

    text = text.replace("\n", "")
    print(text)

    if (text == "Click!"):
        mouse.click(Button.left)