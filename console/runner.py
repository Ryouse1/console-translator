import subprocess
from .translate import translate_text
from .keywords import should_translate

def run(cmd: list):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    buffer = []
    in_error = False

    for line in process.stdout:
        lower = line.lower()

        if "traceback" in lower or "error" in lower:
            in_error = True

        if in_error:
            buffer.append(line)
            if line.strip() == "" or "error" in lower:
                joined = "".join(buffer)
                print(translate_text(joined))
                buffer.clear()
                in_error = False
        else:
            if should_translate(line):
                print(translate_text(line), end="")
            else:
                print(line, end="")
