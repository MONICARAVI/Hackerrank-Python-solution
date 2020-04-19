from collections import Counter
n = int(input())
shoe_size = list(map(int,input().split()))
shoe_count = Counter(shoe_size)
customers = int(input())
totalcost = 0
for _ in range(customers):
    size,amount = map(int,input().split())
    if size in shoe_count.keys() and shoe_count[size]!=0:
        totalcost+=amount
        shoe_count[size] -=1 
print(totalcost)
