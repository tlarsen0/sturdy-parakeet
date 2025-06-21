import sys

def fibonacci(fib_to: int):
    if fib_to < 0:
        return "Cannot fibonacci a negative number!"
    elif fib_to == 0:
        return 0
    elif fib_to == 1:
        return 1
    else:
        return fibonacci(fib_to - 1) + fibonacci(fib_to - 2)

if len(sys.argv) < 2:
    print("fibonacci needs at least 1 argument")
    sys.exit()

print(f"Time to fibonacci: {sys.argv[1]}!")
fib = fibonacci(int(sys.argv[1]))
print(f"Answer: {fib}")

