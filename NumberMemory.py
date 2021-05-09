#currently broken due to it reading 7s often as 1s

import time
import pynput
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller

keyboard = Controller()
mouse = MouseController()
print(mouse.position)

for i in range(20):

    time.sleep(0.5)

    from PIL import ImageGrab, ImageDraw
    image = ImageGrab.grab(bbox=(450, 400, 1425, 550))
    image.save('sc.png') 
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files (x86)\Tesseract-OCR\tesseract")
    text = pytesseract.image_to_string(Image.open("sc.png"), config="--psm 6 digits")
    print(text)
    text = text.replace("\n", "")
    text = text.replace("A", "4")
    text = text.replace("ce", "5")
    text = text.replace("L", "1")
    text = text.replace("C", "9")
    text = text.replace(" (", "7")
    text = text.replace("/", "7")
    text = text.replace("[", "7")

    time.sleep(6)
    print(text)
    keyboard.type(text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.01)
    mouse.position = (766, 530)
    mouse.click(Button.left)
