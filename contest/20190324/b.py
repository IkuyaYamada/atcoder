# B - ATCoder
s = input()
agct = ["A", "G", "C", "T"]
r = re = 0
for i in s:
	if i in agct:
		r += 1
	else:
		re = max(re, r)
		r =0
print(max(re, r))