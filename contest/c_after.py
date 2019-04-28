# C - GCD on Blackboard
import sys

n = int(input())
A = list(map(int, input().split()))

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
L = 0
R = min([gcd(i, i+1) for i in A[:n])

for i in A:
	L  = gcd(L, i)
	R_gcd = gcd(R, i)
	M = gcd(L, R)