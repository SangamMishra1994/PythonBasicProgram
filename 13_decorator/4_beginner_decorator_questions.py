# 1. Write a decorator that prints “Function is running”
# before the function starts.
def function_is_running(func):
    def wrapper(*args, **kwargs):
        print("function is running")
        return func(*args, **kwargs)

    return wrapper


@function_is_running
def call_function():
    print("Hello !")


call_function()


# 2. Write a decorator that prints the name of the function being executed.
def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"name of the function is :- {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@print_function_name
def hello_decorator():
    print("Correct !! ")


hello_decorator()


# 3. Create a decorator that prints the arguments passed to a function.
def print_argument(func):
    def wrapper(*args, **kwargs):
        print("Argument value is :- ", args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@print_argument
def check_argument(name, age):
    return f"name is {name} and age - {age}"


print(check_argument("Sangam", 33))


# 4. Write a decorator that converts the output of a function to uppercase.
# # (Works only if function returns a string.)
def convert_to_uppercase(func):
    def wrapper(*args, **kwargs):
        print("Before conversion :- ", args, kwargs)
        result = func(*args, **kwargs)
        print("After conversion :- ", end=" ")
        return result.upper()

    return wrapper


@convert_to_uppercase
def test_conversion(text1, text2):
    return text1 + " " + text2


print(test_conversion(text1="hello", text2="world!"))


# 5. Create a decorator that counts how many times a function was called.
def count_function(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function Name :- {func.__name__} and count = {count} time")
        return func(*args, **kwargs)

    return wrapper


@count_function
def function_call():
    print("Hi !!")


function_call()
function_call()
