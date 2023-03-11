import codecs
import os

def obfuscate(string: str) -> str:
    return codecs.encode(string.encode(), 'hex').decode(encoding="utf-8")


def deobfuscate(string: str) -> str:
    return codecs.decode(string.encode(), 'hex').decode(encoding="utf-8")
