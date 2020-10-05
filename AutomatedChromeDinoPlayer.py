import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    time.sleep(0.3)
    pyautogui.keyUp(key)
def actionforblack(data):
    for i in range(380,500):
        for j in range(500,540):
            if data[i,j] <= 100 :
                return "t"
            if data[i,j-70] <= 100:
                return "f"
def actionforwhite(data):
    for i in range(380,500):
        for j in range(500,540):
            if data[i,j] >100 and data[i,j] <=255:
                return "t"
            if data[i,j-70] >100 and data[i,j-70] <=255:
                return "f"
def background():
    for i in range(1500,1550):
        for j in range(180,200):
            if data[i,j] ==255:
                return True
time.sleep(3)           
hit("up")
while True:
   
    image = ImageGrab.grab().convert("L")
    data = image.load()
    if background():
        if actionforblack(data)=="t":
            hit("up") 
        elif actionforblack(data)=="f":
            hit("down")      
    else:
        if actionforwhite(data)=="t":
            hit("up") 
        elif actionforwhite(data)=="f":
            hit("down")
    
    
    