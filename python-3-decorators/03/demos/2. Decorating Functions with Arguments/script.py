def email_decorator(func):
    def wrapper(*args, **kwargs):
        # args = ("desk",)
        # kwargs = {}
        print("Dear interns,")
        func(*args, **kwargs)
        # func("desk")
        print("Best regards,")
        print("your new boss")
    return wrapper

@email_decorator
def greeting_message(x):
    print(f"Welcome to your new {x}!")


greeting_message("desk")