class Node():
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0

def find(node):
    if node.parent.value == node.value:
        return node.value
    return find(node.parent)

def union(n1, n2):
    if n1.rank > n2.rank:
        n2.parent = n1
        n1.rank += 1
    else:
        n1.parent = n2
        n2.rank += 1

n, k = map(int, raw_input().split())

l = []
for node in xrange(k):
    l.append(Node(node))

for i in xrange(k):
    c , n1, n2 = raw_input().split()
    if c == 'C':
        res = 'S' if find(l[int(n1)]) == find(l[int(n2)]) else 'N'
        print res
    else:
        union(l[int(n1)], l[int(n2)])

         
