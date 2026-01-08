import sys
from .translator import translate

class TranslatedStdout:
    def write(self, text):
        sys.__stdout__.write(translate(text))
    def flush(self):
        pass

def enable_stdout_translation():
    sys.stdout = TranslatedStdout()
