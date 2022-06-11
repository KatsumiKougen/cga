from sys import argv

integer_list, nth = argv[1].split(","), int(argv[2])
integer_len = len(integer_list)

nth_sum = sum([int(integer_list[i]) for i in range(nth-1, integer_len, nth)])
print(nth_sum)
