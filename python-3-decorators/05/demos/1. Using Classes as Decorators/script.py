from functools import wraps

class EmailDecorator:
    def __init__(self, fromWho):
        self.fromWho = fromWho

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Dear interns,")
            func(*args, **kwargs)
            print("Best regards,")
            print(f"your new {self.fromWho}")
        return wrapper

# def email_decorator(fromWho="boss"):
#     def _email_decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("Dear interns,")
#             func(*args, **kwargs)
#             print("Best regards,")
#             print(f"your new {fromWho}")
#         return wrapper
#     return _email_decorator


@EmailDecorator(fromWho="team leader")
def greeting_message(x):
    """Function displays a greeting message"""
    print(f"Welcome to your new {x}!")

greeting_message("job")