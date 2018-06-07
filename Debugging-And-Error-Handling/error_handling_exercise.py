def divide(num1,num2):
    try:
        total = num1 / num2
    except TypeError:
        return 'Please provide two integers or floats'
    except ZeroDivisionError:
        return 'Please do not divide by zero'
    return total