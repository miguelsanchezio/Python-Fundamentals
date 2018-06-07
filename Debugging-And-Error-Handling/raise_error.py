def colorize(text, color):
    colors = ('cyan', 'yellow', 'green')
    if type(text) is not str:
        raise TypeError('Text must be instance of str')
    if color not in colors:
        raise ValueError('Color is invalid')

    print(f'Printed {text} in {color}')

colorize('hello', 'red')