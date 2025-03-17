from functools import wraps


def log_function_call(func):
    """
    Decorator to log function calls.
    It will log the name of the function and its arguments.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
