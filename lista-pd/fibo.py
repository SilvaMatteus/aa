#code
def fib(n):
    prev_1 = 0
    prev_2 = 1

    if n == 0:
        return 0

    i = 2
    while i < n:
        temp =  prev_2
        prev_2 = prev_1 + prev_2
        prev_1 = temp
        i += 1

    return prev_2 + prev_1

cases = int(input())

for case in range(cases):
    n = int(input())
    print (fib(n)%1000000007)