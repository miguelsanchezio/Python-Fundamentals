def exponent(num, power=2):
    return num ** power

print(exponent(2, 3)) # 8
print(exponent(3)) # 9
print(exponent(7)) # 49

def speak(animal='dog'):
    if animal == 'pig':
        return 'oink'
    elif animal == 'duck':
        return 'quack'
    elif animal == 'cat':
        return 'meow'
    elif animal == 'dog':
        return 'woof'
    else:
        return '?'