registry = {}

def register_class(cls):
    registry[cls.__name__] = cls
    return cls

@register_class
class SomeClass:
    pass