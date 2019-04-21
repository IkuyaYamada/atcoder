#C - Stones
#黒い石のすぐ右に白い石があるような箇所がないようにしたいです。 

n = int(input())
state = input()
state_list = list(state)
state_list.append(" ")

#specify the locate causing problem
prob_locate = []
prob_num = 0
for i in range(n):
	if state_list[i] == "#" and state_list[i+1] == ".":
		prob_locate.append(i)
		prob_num += 1
if prob_num == 0:
		print(0)
		exit()

#finding optimal position
import random
while prob_num > 0:
	for i in prob_locate:
		r_0 = random.randint(0,1)
		r_1 = random.randint(0,1)
		state_list[(i + r_0)] = ["#", "."][r_1]
	prob_locate = []
	prob_num = 0
	for i in range(n):
		if state_list[i] == "#" and state_list[i+1] == ".":
			prob_locate.append(i)
			prob_num += 1

#checking the difference
state_list.remove(" ")
diff = 0
for i, j in zip(state_list, list(state)):
	if i != j: diff += 1

print(diff)
		
		