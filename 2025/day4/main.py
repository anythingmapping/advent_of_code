# Day 4: Newspaper Delivery Routes

FILE = "input.txt"
# FILE = "demo.txt"

# Offsets for the 8 neighbors in 2D
NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1), (1, 0),  (1, 1)
]

def paper_locations():
    accessible_paper = []
    with open(FILE) as f:
        map_of_paper = [line.rstrip("\n") for line in f]

    rows = len(map_of_paper)
    cols = len(map_of_paper[0])

    for r in range(rows):
        result_line = ""
        for c in range(cols):
            char = map_of_paper[r][c]

            if char != "@":
                result_line += "."
                continue

            # Count adjacent @
            count_adj = 0
            for dr, dc in NEIGHBORS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if map_of_paper[nr][nc] == "@":
                        count_adj += 1

            # Accessible if fewer than 4 neighbors
            if count_adj < 4:
                result_line += "x"
            else:
                result_line += "@"

        accessible_paper.append(result_line)

    return accessible_paper, map_of_paper

if __name__ == "__main__":
    accessible_paper, map_of_paper = paper_locations()
    total = sum(row.count("x") for row in accessible_paper)

    print(f"Day 4: Accessible rolls: {total}")
    print("\n".join(accessible_paper))
