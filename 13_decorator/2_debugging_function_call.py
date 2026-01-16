def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(
            f"Calling {func.__name__} with args {args_value} "
            f"and kwargs {kwargs_value}"
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def say_hello():
    print("hello")


@debug
def debug_example(name, greeting="Hello!"):
    print(f"{greeting}, {name}")


say_hello()
debug_example("Chai", greeting="hanji")
