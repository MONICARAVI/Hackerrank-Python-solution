from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    letter = input()
    d[letter].append(1+i)

for i in range(m):
    query = input()
    if query not in d.keys():
        print(-1)
    else:
        for i in d[query]:
            print(i,end=' ')
        print()
