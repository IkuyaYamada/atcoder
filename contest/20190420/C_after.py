#C 
#毎回関数を呼ぶとおそくなる
n = int(input())
stones = input()
score = stones.count(".")
r = score
for i in range(n):
	if stones[i] == ".":
		r -= 1
	else:
		r += 1
	score = min(r, score)
print(score)	