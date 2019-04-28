# B - Resale

n = int(input())
value = map(int, input().split())
cost = map(int, input().split())

print(sum([ i-k for i, k in zip(value, cost) if i > k]))