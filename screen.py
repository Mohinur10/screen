import pyautogui
import keyboard
import time

def start_screenshot():
    print("Dastur ishga tushdi...")
    print("Screenshot qilish uchun '1' raqamini bosing.")
    print("Dastur to'xtashi uchun '0' raqamini bosing.")
    while True:
        if keyboard.is_pressed("1"):
            file_name = f"screen_{int(time.time())}.png"
            screenshot = pyautogui.screenshot()
            screenshot.save(file_name)
            print(f"Screenshot saqlandi: {file_name}")
            time.sleep(0.3) 
        if keyboard.is_pressed("0"):
            print("Dastur to'xtadi")
            break
if __name__ == "__main__":
    start_screenshot()