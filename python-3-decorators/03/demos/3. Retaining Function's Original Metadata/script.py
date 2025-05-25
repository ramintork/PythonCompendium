from functools import wraps

def email_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Dear interns,")
        func(*args, **kwargs)
        print("Best regards,")
        print("your new boss")
    return wrapper

@email_decorator
def greeting_message(x):
    """Function displays a greeting message"""
    print(f"Welcome to your new {x}!")


print(greeting_message.__name__)
print(greeting_message.__doc__)