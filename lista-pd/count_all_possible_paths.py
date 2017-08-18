# # TLE
# def calc(m, n):
#    if(m == 1 or n == 1):
#         return 1
#    return  calc(m-1, n) + calc(m, n-1)


# cases = input()
# for case in range(int(cases)):
#     l = input().split()
#     print(calc(int(l[0]), int(l[1])))

def calc(m, n):
   if(m == 1 or n == 1):
        return 1
   return  calc(m-1, n) + calc(m, n-1)


cases = input()
for case in range(int(cases)):
    l = input().split()
    m = []
            
    for i in range(int(l[0])):
        m.append([])
        for j in range(int(l[1])):
            m[i].append(1)
    
    for i in range(1, int(l[0])):
        for j in range(1, int(l[1])):
            m[i][j] = m[i-1][j] + m[i][j-1]
    
    print(m)
    print(m[-1][-1]%(10**9+7))