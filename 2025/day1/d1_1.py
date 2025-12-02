def day01b():
    current_number = 50
    counter = 0
    prev_dir = 1
    with open("input/d1.txt", "r") as file:
        for line in file:
            l = line.strip();

            dir = -1 if l[0] == 'L' else 1
            amount = int(l[1:])

            # invert the current value when changing rotation
            if dir != prev_dir and current_number != 0:
                current_number = 100 - current_number

            current_number += amount
            # int division
            counter += current_number // 100

            current_number %= 100
            prev_dir = dir

        print(f"1b - Number of zeroes: {counter}")


day01b()