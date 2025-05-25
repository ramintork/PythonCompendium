import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_function_call
def add(a, b):
    return a + b

print(add(2, 3))