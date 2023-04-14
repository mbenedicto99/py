import time
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

start_time = time.perf_counter()
print(fibonacci(5))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")