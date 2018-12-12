result_set = set()
result = 0

with open("day1_input.txt", "r") as input_txt:
    input_list = []
    for line in input_txt:
        input_list.append(line)
    while True:
        check = False
        for i in range(0, len(input_list)):
            num = int(input_list[i][1:])
            if input_list[i][0] == "+":
                result += num
            else:
                result -= num
            if set([result]).issubset(result_set):
                check = True
                print(result)
                break
            else:
                result_set.add(result)
        if check:
            break

print(result)
