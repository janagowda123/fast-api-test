print("Hello World")

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# Example usage
n = 5
result = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms: {result}")
