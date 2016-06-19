def fib(pos):
    if pos == 0 or pos == 1:
        return pos
    return fib(pos - 1) + fib(pos - 2)
