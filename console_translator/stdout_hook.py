import sys
from .translator import translate

_original_stdout = sys.__stdout__
_enabled = False

class TranslatedStdout:
    def write(self, text):
        if not isinstance(text, str):
            return

        if text.strip() == "":
            _original_stdout.write(text)
            _original_stdout.flush()
            return

        try:
            translated = translate(text)
            _original_stdout.write(translated)
            _original_stdout.flush()
        except Exception:
            _original_stdout.write(text)
            _original_stdout.flush()

    def flush(self):
        try:
            _original_stdout.flush()
        except Exception:
            pass


def enable_stdout_translation():
    global _enabled
    if _enabled:
        return

    sys.stdout = TranslatedStdout()
    _enabled = True
