result = 0
with open('day1_part1_input.txt', 'r') as input_txt:
	for line in input_txt:
		num = int(line[1:])
		if line[0] == '+':
			result += num
		else:
			result -= num

print(result)
