"""
Examples for hooking the Python encoding system.
"""
import codecs
from codecs import CodecInfo, StreamReader, StreamWriter
from encodings import utf_8
from io import StringIO


def rot13(s):
    """
    rot13-encode a unicode string.
    """
    chars = []
    for c in s:
        if 'a' <= c <= 'z':
            newchar = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        elif 'A' <= c <= 'Z':
            newchar = chr((((ord(c) - ord('A')) + 13) % 26) + ord('a'))
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


class Rot13IncrementalEncoder(utf_8.IncrementalEncoder):
    def encode(self, input, final=False):
        return rot13encode(input, self.errors)[0]


class Rot13IncrementalDecoder(utf_8.IncrementalDecoder):
    def decode(self, input, final=False):
        return rot13decode(super().decode(input, self.errors))


class Rot13StreamWriter(utf_8.StreamWriter):
    encode = rot13encode


class Rot13StreamReader(utf_8.StreamReader):
    decode = rot13decode


def search_function(encoding):

    if encoding != 'pytenn2016-rot13':
        return None

    return CodecInfo(
        name='pytenn2016-rot13',
        encode=rot13encode,
        decode=rot13decode,
        incrementalencoder=Rot13IncrementalEncoder,
        incrementaldecoder=Rot13IncrementalDecoder,
        streamreader=Rot13StreamReader,
        streamwriter=Rot13StreamWriter,
    )

