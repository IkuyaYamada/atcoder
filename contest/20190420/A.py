#A - On the Way

coords = list(map(int, input().split()))
a, b, c = coords

if a < c < b:
	print("Yes")
elif b < c < a:
	print("Yes")
else:
	print("No")