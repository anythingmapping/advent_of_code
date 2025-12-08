# Day 7: Do math homework
import numpy as np

FILE = "input.txt"
FILE = "demo.txt"


def get_beam_array():
    with open(FILE, "r") as f:
        beam_array = np.loadtxt(f, dtype=str)
        print(beam_array)
        print(beam_array.shape)
        for i in range(beam_array.shape[0]):
            print(beam_array[i])

    return beam_array


def do_math():
    with open(FILE, "r") as f:
        for line in f:
            beam = list(line.split())
            beam_array = np.array(beam)
            print(beam_array)


if __name__ == "__main__":
    beam_array = get_beam_array()
    print(f"-" * 50)
    print(f"Day 6: GRAND TOTAL: {111}")
