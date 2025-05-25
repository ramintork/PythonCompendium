from functools import wraps

def company_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("CompanyName (LLC) Street 22 company@mail.com")
    return wrapper

def email_decorator(fromWho):
    def _email_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Dear interns,")
            func(*args, **kwargs)
            print("Best regards,")
            print(f"your new {fromWho}")
        return wrapper
    return _email_decorator

@company_info
@email_decorator(fromWho="team leader")
def greeting_message(x):
    """Function displays a greeting message"""
    print(f"Welcome to your new {x}!")

greeting_message("job")