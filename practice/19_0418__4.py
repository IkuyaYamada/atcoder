#ABC085B - Kagami Mochi

num_mochi = int(input())
diam = []
for i in range(num_mochi):
	input_diam = int(input())
	if input_diam in diam: diam.remove(input_diam)
	diam.append(input_diam)
print(len(diam))