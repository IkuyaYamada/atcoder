# C - GeT AC
n, q = map(int, input().split())
s = input()
t = [0] * (n + 1)
for i in range(n):
	t[i + 1] = t[i] + (1 if s[i : i + 2] == 'AC' else 0)
for i in range(q):
	l, r = map(int, input().split())
	print(t[r-1] - t[l-1])
  

""" over limit
for i in q_range:
	s_ = s[i[0]-1:i[1]]
	r= 0
	for i in range(len(s_)-1):
		if s_[i] == "A" and s_[i+1] == "C":
			r += 1
	print(r)
"""