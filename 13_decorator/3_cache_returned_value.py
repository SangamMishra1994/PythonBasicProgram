# Implement a decorator that cache the return value of a function
# so that when it is called with the same arguments, the cached value
# is returned instead of re-executing the function
import time


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def time_rrunning_fucntion(a, b):
    time.sleep(4)
    return a + b


print(time_rrunning_fucntion(2, 3))
print(time_rrunning_fucntion(2, 3))
print(time_rrunning_fucntion(5, 3))
