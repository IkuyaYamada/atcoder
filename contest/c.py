# C - GCD on Blackboard
import sys

n = int(input())
n_list = list(map(int, input().split()))

def gcd(a, b):
	m = max(a, b)
	n = min(a, b)
	while True:
		if n==0:
			return m
		else:
			_=m%n
			m=n
			n=_

if len(n_list)==2:
	gcd_ = gcd(n_list[0], n_list[1])
	print(gcd_)
	sys.exit()
	
gcd_ = 0
for i in range(n):
	pop_ = n_list.pop(i)
	gcd_min = min([gcd(n_list[j], n_list[j+1]) for j in range(len(n_list)-1)])
	n_list.insert(i, pop_)
	gcd_ = max(gcd_, gcd_min)	

print(gcd_)