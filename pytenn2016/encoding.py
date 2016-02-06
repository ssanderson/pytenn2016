"""
Example of hooking the Python encoding system with a rot13 "encoding".
"""
from codecs import CodecInfo
from encodings import utf_8


def rot13(s):
    """
    rot13-encode a unicode string.
    """
    chars = []
    for c in s:
        if 'a' <= c <= 'z':
            newchar = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        elif 'A' <= c <= 'Z':
            newchar = chr((((ord(c) - ord('A')) + 13) % 26) + ord('A'))
        else:
            newchar = c
        chars.append(newchar)
    return ''.join(chars)


def rot13encode(input, errors='strict'):
    """
    Convert unicode to rot13-ed raw bytes.
    """
    return utf_8.encode(rot13(input), errors)


def rot13decode(input, errors='strict'):
    """
    Convert raw bytes to rot-13ed unicode
    """
    decoded, length = utf_8.decode(input, errors)
    return rot13(decoded), length


def search_function(encoding):

    if encoding == 'pytenn2016-rot13':
        return CodecInfo(
            name='pytenn2016-rot13',
            encode=rot13encode,
            decode=rot13decode,
        )
