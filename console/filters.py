import re

_CONTROL = re.compile(r"[\x00-\x1f\x7f]")

def should_translate(text: str) -> bool:
    if not isinstance(text, str):
        return False

    if text.strip() == "":
        return False

    # 制御文字だけのやつは弾く
    if _CONTROL.sub("", text).strip() == "":
        return False

    return True
