# C Five Transportations
# これだと時間オーバー
import numpy as np
n = int(input())
time = [int(input()) for i in range(5)]
time = np.array(time, dtype="int64").reshape(5,1)
tempo = np.array([n, 0, 0, 0, 0], dtype="int64").reshape(5,1)
zeros = np.zeros([5,1], dtype="int64")
num = 1
arrive = 0
while arrive < n:
	_ = tempo - time
	_ = np.amax(np.hstack([_, zeros]), axis=1).reshape(5,1)
	movement = np.delete((tempo-_ ), 4)
	movement = np.insert(movement, 0, 0).reshape(5,1)
	tempo = _ + movement
	num += 1	# count #iterates
	arrive += tempo[4]
	if num%100000==0: print(arrive)
print(num)