def parse_data(file_name):
    input_data = []
    with open(file_name) as file:
        for line in file:
            input_data.append(line.rstrip())
    return input_data

def part_a(input_data):
    horizontal_pos = 0
    vertical_pos = 0

    for value in input_data:
        parsed_value = value.split()
        current_direction = parsed_value[0][0]

        if current_direction == 'f':
            horizontal_pos += int(parsed_value[1])
        elif current_direction == 'u':
            vertical_pos -= int(parsed_value[1])
        elif current_direction == 'd':
            vertical_pos += int(parsed_value[1])

    return horizontal_pos * vertical_pos

def part_b(input_data):
    horizontal_pos = 0
    vertical_pos = 0
    aim = 0

    for value in input_data:
        parsed_value = value.split()
        current_direction = parsed_value[0][0]

        if current_direction == 'f':
            horizontal_pos += int(parsed_value[1])
            vertical_pos += aim * int(parsed_value[1])
        elif current_direction == 'u':
            aim -= int(parsed_value[1])
        elif current_direction == 'd':
            aim += int(parsed_value[1])

    return horizontal_pos * vertical_pos


if __name__ == '__main__':
    input_data = parse_data("input.txt")

    distance_a = part_a(input_data)
    distance_b = part_b(input_data)

    print("Part 1 : " + str(distance_a))
    print("Part 2 : " + str(distance_b))
