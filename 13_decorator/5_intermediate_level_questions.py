# ✅ Intermediate Level Decorator Questions

# 6. Write a decorator that measures execution time of any function.
# (Hint: use time.time())
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in :- {(end_time - start_time):.3f} time")
        return result

    return wrapper


@measure_time
def function1():
    time.sleep(2)


function1()


# 7. Write a decorator that caches function results
# (similar to a simple memoization without using functools.lru_cache).


# 8. Create a decorator that logs the inputs and
# outputs of a function to a file.


# 9. Write a decorator that retries running a function 3 times if it fails.
# (Hint: use try/except inside wrapper)


# 10. Create a decorator that requires a user to be “logged in”
# before running a function.
# (Simulate a dictionary like: {"user": "Sangam", "logged_in": True})
def login_required(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            return "Access_denied !"
        return func(user, *args, **kwargs)

    return wrapper


@login_required
def dashboard(user):
    return f"Welcome {user['name']}"


user1 = {"name": "Sangam", "logged_in": True}
user2 = {"name": "Mishra", "logged_in": False}

print(dashboard(user1))
print(dashboard(user2))
