from tokenize import tokenize


def show_tokens(source):
    """
    Tokenize a Unicode string.
    """
    return list(tokenize(iter(source.encode('utf-8').splitlines()).__next__))


__all__ = ['show_tokens']
