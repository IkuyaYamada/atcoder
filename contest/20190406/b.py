# B - Five Dishes
# sys.stdin.readline()
# import sys
import math
# input = sys.stdin.readline
each_time = [int(input()) for i in range(5)]
wait_time = [10*math.ceil(i/10)-i for i in each_time]
result = [i + k for i,k in zip(each_time, wait_time)]
result[wait_time.index(max(wait_time))] = each_time[wait_time.index(max(wait_time))]
print(sum(result))