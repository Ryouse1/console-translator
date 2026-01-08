TRANSLATE_KEYWORDS = [
    "downloading",
    "installing",
    "collecting",
    "building",
    "successfully",
    "error",
    "failed",
    "exception",
    "traceback"
]

def should_translate(text: str) -> bool:
    lower = text.lower()
    return any(k in lower for k in TRANSLATE_KEYWORDS)
