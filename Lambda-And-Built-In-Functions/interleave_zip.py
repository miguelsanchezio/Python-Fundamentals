def interleave(str1,str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))