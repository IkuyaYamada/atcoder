#ABC088B - Card Game for Two

n = int(input())
card_list = [int(i) for i in input().split()]
card_list.sort()
alice_list, bob_list = [], []
turn = 0
while turn < n:
	alice_list.append(card_list.pop())
	turn += 1
	if turn == n: break
	bob_list.append(card_list.pop())
	turn += 1

diff = sum	(alice_list) - sum(bob_list)
print(diff)