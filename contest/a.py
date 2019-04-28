 # A - Biscuit Generator
 
a, b, t = map(int, input().split())
a_ = a
cookie=0
while a_ < t+0.5:
	cookie += b
	a_  += a

print(cookie) 