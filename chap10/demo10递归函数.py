# Author: lisz1012
# Creation date and time: 6/1/24 4:20 PM

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(6))
