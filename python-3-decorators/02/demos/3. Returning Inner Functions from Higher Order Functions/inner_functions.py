def outer():
    
    def inner():
        print("Inner function")
    
    return inner

func = outer()
func()
print(func)