import sys
from .translator import translate

_original_stdout = sys.__stdout__
_enabled = False

class TranslatedStdout:
    def write(self, text):
        # Colab防衛ライン①
        if not isinstance(text, str):
            return

        # Colab防衛ライン②
        if text.strip() == "":
            _original_stdout.write(text)
            return

        # Colab防衛ライン③（printループ防止）
        if text.startswith("[console-translator]"):
            _original_stdout.write(text)
            return

        try:
            translated = translate(text)
            _original_stdout.write(translated)
        except BaseException:
            # ここで「絶対に何もしない」
            _original_stdout.write(text)

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
