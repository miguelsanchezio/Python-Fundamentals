from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "role" in kwargs and "admin" in kwargs.values():
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper

