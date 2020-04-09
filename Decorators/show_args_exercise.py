from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        args_tuple = tuple(arg for arg in args)
        kwargs_dict = {k: v for k, v in kwargs.items()}
        print("Here are the args: {}".format(args_tuple))
        print("Here are the kwargs: {}".format(kwargs_dict))
        return fn(*args, **kwargs)

    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass


do_nothing(1, 2, 3, a="hi", b="bye")