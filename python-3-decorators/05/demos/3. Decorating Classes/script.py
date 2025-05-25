def add_speech(cls):
    cls.speak = lambda self: f"Hello, I'm a {self.__class__.__name__} instance"
    return cls

@add_speech
class SomeClass:
    pass

# SomeClass = add_speech(SomeClass)

obj = SomeClass()
print(obj.speak())