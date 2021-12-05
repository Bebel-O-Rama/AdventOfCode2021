def parse_data(file_name):
    input_data = []
    with open(file_name) as file:
        for line in file:
            input_data.append(line.rstrip())
    return input_data



def part_a(input_data):
    return 0

def part_b(input_data):
    return 0


if __name__ == '__main__':
    input_data = parse_data("input.txt")

    ret_a = part_a(input_data)
    ret_b = part_b(input_data)

    print("Part 1 : " + str(ret_a))
    print("Part 2 : " + str(ret_b))
