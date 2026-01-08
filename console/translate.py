from googletrans import Translator

translator = Translator()
language = "ja"

def translate_text(text: str) -> str:
    try:
        return translator.translate(text, dest=language).text
    except:
        return text
