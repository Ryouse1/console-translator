from .engine import translate_text
from .filters import should_translate

language = "ja"
fallback_prefix = "[UNTRANSLATED] "

def translate(text: str) -> str:
    if not should_translate(text):
        return text

    try:
        result = translate_text(text, language)
        return result if result else fallback_prefix + text
    except Exception:
        return fallback_prefix + text
