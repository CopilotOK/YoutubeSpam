import pyautogui 
import time

def chahiyeSneakers():
    pyautogui.leftClick(x=21,y=372)
    time.sleep(1)
    pyautogui.leftClick(x=1342,y=63)
    time.sleep(2)
    pyautogui.moveTo(x=1199,y=450)
    i=0
    while i<6:
        i+=1
        pyautogui.leftClick()
        time.sleep(1.5)



    


initial = pyautogui.prompt("Where would you start?")

def khelnaHaiNayaSot():
    while True:
        global initial
        pyautogui.leftClick(x=302,y=634)
        time.sleep(1)
        pyautogui.write(f"{initial} like")
        time.sleep(1)
        pyautogui.leftClick(x=857,y=652)
        time.sleep(3)
        initial+=1



try:
    initial = int(initial)
except Exception:
    if initial == None:
        exit()
    else:
       pyautogui.alert("number likh bsdk")
       exit()
else: 
    chahiyeSneakers()
    khelnaHaiNayaSot()
    



