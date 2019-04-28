# C - Snuke the Wizard
n, q = map(int, input().split())
seq = list(input())
seq = [(i, 0)for i in seq]
for i in range(q):
	input_ = input().split()
	seq = [(i, k-1) if i==input_[0] else (i,k) for (i, k) in seq ] 
	#seq = [(i, k+1) if i==input_[0] else (i,k) for (i, k) in seq ]
print(seq)

