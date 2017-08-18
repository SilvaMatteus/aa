count = 0
def fib_c(n):
    global count
    count += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_c(n -1) + fib_c(n -2)

cases = int(raw_input())

for case in xrange(cases):
    count = -1
    x = raw_input()
    res = fib_c(int(x))
    print 'fib(' + x + ') = ' + str(count) + ' calls = ' + str(res)

