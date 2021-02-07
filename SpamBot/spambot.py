import pyautogui, time, keyboard

frase = 'tu que crees' #
time.sleep(5)

while True:
    if keyboard.is_pressed('q'):
        break
    # f = open('archivo.txt', 'r')
    pyautogui.typewrite(frase)
    pyautogui.press('enter')
    # f.close()
    