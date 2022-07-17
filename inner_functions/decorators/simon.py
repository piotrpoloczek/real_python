from functools import wraps


def who_says(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if name.lower() == "simon":
                return func(*args, **kwargs)
            else:
                raise AttributeError("Simon did't say")

            return wrapper
        return decorator
