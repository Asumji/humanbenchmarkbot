import time
import pynput
from PIL import Image
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

keyboard = Controller()
mouse = MouseController()

print(mouse.position)

lword = input("Last word: ")
from PIL import ImageGrab, ImageDraw
image = ImageGrab.grab(bbox=(300, 400, 1700, 800))
image.save('sc.png')

import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
text = pytesseract.image_to_string(Image.open("sc.png"))

lwordc = text.count(lword)

text = text.strip()
text = text.replace("\n", " ")
text = text.replace("|", "I")
text = text.replace("1", "I")
text = text.split(" ")
print(text)
for word in text:
    time.sleep(0.01)
    keyboard.type(word)
    if (word == lword and lwordc == 1):
        print("End of Sentence")
        break
    elif (word == lword):
        lwordc -= 1
        keyboard.type(" ")
    else:
        keyboard.type(" ")