def enforce(*types):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return fn(*newargs, **kwargs)
        return wrapper
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    print(a / b)


repeat_msg("Hey", "7")
divide(1, "3")
