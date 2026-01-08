EXCLUDE_KEYWORDS = {
    "print", "import", "from", "pip", "python",
    "def", "class", "return", "for", "while",
    "==", "!=", "::", "/", "\\"
}

def should_translate(text: str) -> bool:
    lower = text.lower()
    for k in EXCLUDE_KEYWORDS:
        if k in lower:
            return False
    return True
