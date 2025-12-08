# Day 6: Do math homework
import numpy as np

FILE = "input.txt"
# FILE = "demo.txt"


def do_np_load():
    grand_total = 0
    # arr = arr.reshape(-1, 3)
    arr = np.loadtxt(FILE, dtype=str)
    col_count = arr.shape[0]
    row_count = arr.shape[1]
    opperator = arr[col_count - 1, 1]

    #

    for i in range(row_count):
        opperator = arr[col_count - 1, i]

        print(
            f"The array has {col_count} columns and {row_count} rows with the opperator {opperator}"
        )
        # print(f"Column {i} is {col}")
        col = arr[0:-1, i]
        if opperator == "+":
            col_sum = int(col[0]) + int(col[1]) + int(col[2]) + int(col[3])
        else:
            print("Invalid opperator")
            col_sum = int(col[0]) * int(col[1]) * int(col[2]) * int(col[3])
        grand_total += col_sum
        print(f"Column sum is {col_sum}")
        print(f"-" * 50)

    print(f"The grand total is {grand_total}")


def do_math():
    with open(FILE, "r") as f:
        for line in f:
            all_homework_list = list(line.split())
            arr = np.array(all_homework_list)
            arr = arr.reshape(-1, 4)

            print(arr[0, 0])
            print(arr[0, 1])
            print(arr[0, 2])
            print(arr[0, 3])


if __name__ == "__main__":
    # grand_total = do_math()
    do_np_load()

    print(f"-" * 50)
    print(f"Day 6: GRAND TOTAL:")
