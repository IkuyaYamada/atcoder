#ABC083B - Some Sums

#get a value each of N, A, B
n, a, b = list(map(int, input().split()))

#get each number of digit
def sum_digit(n, a, b):
    num_list = []
    for i in range(1 , n+1):
        num_str = str(i)
        digit_sum = sum([int(i) for i in num_str])
        if a <= digit_sum <= b:
            num_list.append(i)
    return(sum(num_list))

result = sum_digit(n, a, b)
print(result)
