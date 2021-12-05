def parse_data(file_name):
    input_data = []
    with open(file_name) as file:
        for line in file:
            input_data.append(int(line.rstrip()))
    return input_data


def part_a(input_data):
    nb_depth_increase_a = 0
    previous_depth = 1000000

    for value in input_data:
        if value > previous_depth:
            nb_depth_increase_a += 1
        previous_depth = value
    return nb_depth_increase_a


def part_b(input_data):
    nb_depth_increase_b = 0
    previous_depth = 1000000

    for i in range(len(input_data) - 2):
        current_depth = input_data[i] + input_data[i + 1] + input_data[i + 2]
        if current_depth > previous_depth:
            nb_depth_increase_b += 1
        previous_depth = current_depth
    return nb_depth_increase_b


if __name__ == '__main__':
    input_data = parse_data("input.txt")

    nb_depth_increase_a = part_a(input_data)
    nb_depth_increase_b = part_b(input_data)

    print("Part 1 : " + str(nb_depth_increase_a))
    print("Part 2 : " + str(nb_depth_increase_b))
