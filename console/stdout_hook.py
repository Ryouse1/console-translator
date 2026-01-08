import sys
from .translator import translate

_original_stdout = sys.__stdout__

class TranslatedStdout:
    def write(self, text):
        debug("write() called")

        if not isinstance(text, str):
            debug("not str")
            return

        if text.strip() == "":
            debug("empty or whitespace")
            _original_stdout.write(text)
            _original_stdout.flush()
            return

        try:
            debug(f"before translate: {repr(text)}")
            translated = translate(text)
            debug(f"after translate: {repr(translated)}")

            _original_stdout.write(translated)
            _original_stdout.flush()
        except Exception as e:
            debug(f"exception in write: {e}")
            _original_stdout.write(text)
            _original_stdout.flush()

    def flush(self):
        try:
            _original_stdout.flush()
        except Exception:
            pass
