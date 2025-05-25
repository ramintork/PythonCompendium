def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator(operation, a, b):
    return operation(a, b)


print(calculator(add, 2, 3))
print(calculator(subtract, 2, 3))
