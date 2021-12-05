def parse_data(file_name):
    input_data = []
    with open(file_name) as file:
        for line in file:
            input_data.append(line.rstrip())
    return input_data



def part_a(input_data):
    mean_tracker = [0] * 12
    gamma_rate = 0
    epsilon_rate = 0

    for value in input_data:
        for i in range(12):
            if int(value[i]):
                mean_tracker[i] += 1
            else:
                mean_tracker[i] -= 1

    for i in range(12):
        if int(mean_tracker[i]) > 0:
            gamma_rate += pow(2, 11-i)
        else:
            epsilon_rate += pow(2, 11 - i)

    return gamma_rate * epsilon_rate


def part_b(input_data):
    return 0


if __name__ == '__main__':
    input_data = parse_data("input.txt")

    ret_a = part_a(input_data)
    ret_b = part_b(input_data)

    print("Part 1 : " + str(ret_a))
    print("Part 2 : " + str(ret_b))
