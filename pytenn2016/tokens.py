from tokenize import tokenize


def show_tokens(source):
    """
    Convert a unicode source code string into the tokens that would generate it.
    """
    return list(tokenize(iter(source.encode('utf-8').splitlines()).__next__))

__all__ = ['show_tokens']
