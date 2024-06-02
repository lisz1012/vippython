# Author: lisz1012
# Creation date and time: 6/1/24 4:27 PM

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 7):
    print(fib(i))
