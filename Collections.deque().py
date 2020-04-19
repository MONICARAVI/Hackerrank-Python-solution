from collections import deque
arr = deque()
queries = int(input())
for _ in range(queries):
    type = input().split()
    
    if(type[0]=='append'):
        arr.append(type[1])
    elif(type[0]=='pop'):
        arr.pop()
    elif(type[0]=='popleft'):
        arr.popleft()
    else:
        arr.appendleft(type[1])
print(*arr,sep=' ') #to print the elements in arr
