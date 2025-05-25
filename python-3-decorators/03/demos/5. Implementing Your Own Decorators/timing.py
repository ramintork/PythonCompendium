import time
from functools import wraps

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.6f} seconds to run.")
        return result
    return wrapper


@time_function
def slow_function():
    time.sleep(1)

slow_function()