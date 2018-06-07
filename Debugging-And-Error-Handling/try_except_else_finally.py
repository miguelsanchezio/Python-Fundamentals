while True:
    try:
        num = int(input('Enter a number: '))
    except ValueError:
        print('That\'s not a number')
    else:
        print('Good job, you entered a number')
        break
    finally:
        print('Runs no mwatter what')

def divide(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print('Error, try again')
        print(err)
    else:
        print(f'{a} divided by {b} is {result}')

divide('a', 2)