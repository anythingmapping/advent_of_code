# the number of times the dial is left pointing at 0 after any rotation in the sequence

START = 50
CURRENT = START
input_counter = 0
zero_hits = 0

def rotate_dial(CURRENT, rotate, value):
    if rotate =="R":
        if CURRENT + int(value) > 100:
            CURRENT = CURRENT+ int(value) - 100
        CURRENT += int(value)
    elif rotate == "L":
        if CURRENT - int(value) < 0:
            CURRENT = 100 + (CURRENT - int(value))
        CURRENT -= int(value)
    return CURRENT

with open("input/d1.txt", "r", encoding="utf-8") as file:
    for line in file:
        # print(f"CURERENT before: {CURRENT}")
        input_counter += 1
        CURRENT = rotate_dial(CURRENT, line[0], line[1:3])
        if CURRENT == 0:
            print(f"Hit zero at line {input_counter}")
            zero_hits += 1



        
        # print(f"CURRENT: {CURRENT} and {line[0]} and value: {line[1:3]}")



print("Total zero hits:", zero_hits)
print("Final value:", CURRENT)
print("Total lines processed:", input_counter)
