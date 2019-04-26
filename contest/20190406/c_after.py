# こんなに短くかけるとは
import math
n = int(input())
time = [int(input()) for i in range(5)]
print(math.ceil(n / min(time) + 4))