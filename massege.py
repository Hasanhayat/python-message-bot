import pyautogui as auto
from time import sleep
import keyboard  

try:
    while True:
        
        auto.write('ASSALAM O ALIKUM')
        auto.press('enter')
        auto.write('WARAHMATULLAHI WABARAKATU')
        auto.press('enter')
        auto.write('kya haal hai')
        auto.press('enter')
        auto.write('theek ho')
        auto.press('enter')
        auto.write('kesi tabyat hai')
        auto.press('enter')
        sleep(0.75)
        if keyboard.is_pressed('q'):  
            print("Loop interrupted by user.")
            break
except KeyboardInterrupt:
    print("Loop interrupted by user.")


