import itertools
from itertools import combinations


FILE = "input.txt"
FILE = "demo.txt"

def get_largest_joltage(line):
    combos = itertools.combinations(line, 12)
    highest_joltage = 0
    # for combo in combos:
    #     print(combo)
    for i in combos:
        string_value = (str(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]+i[10]+i[11]))
        # print(string_value)
        string_value.strip()
        # print(int(string_value))
        if int(string_value) > highest_joltage:
            highest_joltage = int(string_value)
    return(highest_joltage)


def review_batteries():
    line_counter = 0
    total_joltage = 0
    with open(FILE) as f:
        lines = [line.strip() for line in f]
        for line in lines:
            line_counter += 1
            line = line.strip()
            # print(line)
            line_counter += 1
            largest_line_joltage = get_largest_joltage(line)
            total_joltage += largest_line_joltage
            print(f"Line {line_counter}: - Line value {line}-  Largest Joltage: {largest_line_joltage}")
            # break  # Remove this break to process all lines
    return total_joltage

if __name__ == "__main__":
    total_joltage = review_batteries()
    print(f"Day 3: Voltage Output is: {total_joltage}")