def combine_words(word, **kwargs):
    for k,v in kwargs.items():
        if k == 'prefix':
            return v + word
        elif k == 'suffix':
            return word + v
    return word