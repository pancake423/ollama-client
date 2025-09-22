from datetime import datetime

def fmt_timestamp(sep_chars: tuple[str, str, str] = ("-", "_", "-")):
    now = datetime.now()
    return f"{now.year:04d}{sep_chars[0]}{now.month:02d}{sep_chars[0]}{now.day:02d}{sep_chars[1]}{now.hour:02d}{sep_chars[2]}{now.minute:02d}{sep_chars[2]}{now.second:02d}"

LOG_FILE = f"logs/chat_log_{fmt_timestamp()}.txt"
LOG_CONTENTS = ""

def write_log():
    with open(LOG_FILE, "w") as f:
        f.write(LOG_CONTENTS)


def log_message(role: str, message: str):
    global LOG_CONTENTS
    LOG_CONTENTS += f"[{role}]\n"
    LOG_CONTENTS += message
    LOG_CONTENTS += "\n"

def log(txt):
    global LOG_CONTENTS
    LOG_CONTENTS += txt
    LOG_CONTENTS += "\n"
