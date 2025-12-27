# =================================================
# Generate Fibonacci series up to a certain limit
# =================================================


def generate_febonacci(num1, num2, limit):
    print("Fibonacci Series", end=":-  ")
    print(f"{num1} , {num2}", end=", ")
    while limit != 0:
        result = 0
        result = num1 + num2
        if limit == 1:
            print(f"{result}")
            break
        else:
            print(f"{result} ", end=", ")
        num1 = num2
        num2 = result
        limit -= 1


limit_num = int(input("Enter limit: "))
generate_febonacci(0, 1, limit_num)


# Generate the febonacci series different approaches
# 0,1,1,2,3,5,8,13,21,34,55,89
# Approach 1: Using Recursion
def febonacci_recursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return febonacci_recursion(n - 1) + febonacci_recursion(n - 2)


n_terms = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci series using recursion:")

for i in range(n_terms):
    print(febonacci_recursion(i), end=", " if i < n_terms - 1 else "\n")


# Approach 2: Using Iteration
def febonacci_iteration(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


n_terms_iter = int(
    input("Enter the number of terms for Fibonacci series (iteration): ")
)
print("Fibonacci series using iteration:")
print(", ".join(map(str, febonacci_iteration(n_terms_iter))))


# Approach 3: Using Dynamic Programming
def febonacci_dynamic_programming(n):
    fib = [0] * n
    if n > 0:
        fib[0] = 0
    if n > 1:
        fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


n_terms_dp = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci series using dynamic programming:")
print(", ".join(map(str, febonacci_dynamic_programming(n_terms_dp))))
