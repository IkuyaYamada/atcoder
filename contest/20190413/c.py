#C - Coloring Colorfully
import sys
input = sys.stdin.readline
s = list(input())

cost_0, cost_1 = 0, 0

for i in s[::2]:
	if i == "1":
		cost_0 += 1
for i in s[1::2]:
	if i == "0":
		cost_0 += 1

for i in s[::2]:
	if i == "0":
		cost_1 += 1
for i in s[1::2]:
	if i == "1":
		cost_1 += 1
		 
print(min(cost_0, cost_1))