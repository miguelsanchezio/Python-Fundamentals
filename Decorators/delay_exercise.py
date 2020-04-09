from functools import wraps
from time import sleep


def delay(time):
    def inner(fn):
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(time, fn.__name__))
            sleep(time)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hi():
    return "hi"

say_hi = delay(say_hi)

say_hi()
