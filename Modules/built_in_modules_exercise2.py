from keyword import iskeyword

def contains_keyword(*args):
    return any([iskeyword(arg) for arg in args])