def email_decorator(func):
    def wrapper():
        print("Dear interns,")
        func()
        print("Best regards,")
        print("your new boss")
    return wrapper

@email_decorator
def greeting_message():
    print("Welcome to your new job!")


print(greeting_message.__closure__)
print(greeting_message.__closure__[0])
print(greeting_message.__closure__[0].cell_contents)

# The wrapper function memory address
print(f"0x{id(greeting_message):x}")