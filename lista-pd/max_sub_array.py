cases = int(input())

for case in range(cases):
    size = int(input())
    arr = input().split()
    resp = []
    curr = []

    for e in range(size):
        arr[e] = int(arr[e])
    for i in range(size):
        if arr[i] >= 0:
            curr.append(arr[i])
        else:
            if sum(curr) > sum(resp) or (sum(curr) == sum(resp) and len(curr) > len(resp)):
                resp = curr
            curr = []
            

    if sum(curr) > sum(resp) or (sum(curr) == sum(resp) and len(curr) > len(resp)):
        for j in range(len(curr)-1):
            print(curr[j], end=' ')
        print(curr[-1])
    else:
        for k in range(len(resp)-1):
            print(resp[k], end=' ')
        print(resp[-1])