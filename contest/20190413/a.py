 # A - Buttons
a, b = list(map(int, input().split()))
first = max(a, b)
if a == first:
	a -= 1
else:
 	b -= 1
second = max(a, b)
print(first + second)