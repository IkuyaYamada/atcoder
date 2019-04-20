#ABC049C_Daydream.py


s = input()
d, d_er, e, e_er = ("dream", "dreamer", "erase", "eraser")

def daydream(string):
	while len(string) > 7:
		if string[:6] == e_er and (string[6] != "a"  or string[6:] == ""):
			if string[6:] == "":
				return("YES")
			else:
				string = string[6:]		
		elif string[:7] == d_er and (string[7] != "a" or string[7:] == ""):
			if string[7:] == "":
				return("YES")
			else:
				string = string[7:]
		elif string[:5] == d or string[:5] == e:
			if string[5:] == "":
				return("YES")
			else:
				string = string[5:]
		else:
			return("NO")
	
	if string in (d, d_er, e, e_er):
		return("YES")
	else:
		return("NO")
print(daydream(string = s))

# CHECK THE PROGRAM
# import random
# def trial(iter_num = 100, word_list = [d, d_er, e, e_er]):
# 	random_str = "".join([random.choice(word_list) for i in range(iter_num)])
# 	print("str =", random_str)
# 	word_list.append("fake")
# 	random_str_f = ''.join([random.choice(word_list) for i in range(iter_num)])
# 	print("fake =", random_str_f)
# 	results = (daydream(string = random_str), daydream(string = random_str_f))
# 	return(results)
# 	
# print(trial()) 