import time
import pynput
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()
seenWords = []

for i in range(2000):

    time.sleep(0.1)

    from PIL import ImageGrab, ImageDraw
    image = ImageGrab.grab(bbox=(450, 400, 1425, 550))
    image.save('sc.png') 
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
    text = pytesseract.image_to_string(Image.open("sc.png"))

    text = text.replace("\n", "")

    if (text in seenWords):
        mouse.position = (689, 472)
        mouse.click(Button.left)
    else:
        mouse.position = (811, 472)
        seenWords.append(text)
        mouse.click(Button.left)

    print(seenWords)