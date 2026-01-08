import sys
from .translator import translate

_original_stdout = sys.__stdout__
_enabled = False

class TranslatedStdout:
    def write(self, text):
        if not text:
            return
        try:
            translated = translate(text)
            _original_stdout.write(translated)
        except Exception:
            # 翻訳が死んでも表示は殺さない
            _original_stdout.write(text)
        _original_stdout.flush()

    def flush(self):
        _original_stdout.flush()

def enable_stdout_translation():
    global _enabled
    if _enabled:
        return  # 二重起動防止
    sys.stdout = TranslatedStdout()
    _enabled = True
