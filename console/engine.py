def translate_text(text: str, target: str):
    from langdetect import detect
    from deep_translator import GoogleTranslator

    if not text.strip():
        return text

    src = detect(text)
    if src == target:
        return text

    return GoogleTranslator(source="auto", target=target).translate(text)
