from pynput import keyboard
import time
import csv

timestamps = []

def on_press(key):
    timestamps.append(time.time())

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Save data
with open("data.csv", "a", newline="") as f:
    writer = csv.writer(f)
    for i in range(len(timestamps)-1):
        interval = timestamps[i+1] - timestamps[i]
        writer.writerow([interval])
