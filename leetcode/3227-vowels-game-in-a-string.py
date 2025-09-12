def doesAliceWin(s: str) -> bool:
    v = "aeiou"
    for c in s:
        if c in v:
            return True
    else:
        return False