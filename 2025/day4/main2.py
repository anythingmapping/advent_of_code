# Day 4: Newspaper Delivery Routes


FILE = "input.txt"
FILE = "demo.txt"

def replace_at(s, index, value):
    return s[:index] + value + s[index+1:]


def paper_locations():
    with open(FILE) as f:
        lines = [line.strip() for line in f]
        print(lines)
        new_lines = []
        for line in lines:
            print(f"Line value {line}")
            for index, char in enumerate(line):
                # print(f"Index: {index} - Char: {char}")
                # if char == "@":
                #     print("BOOM")
                new_line = line
                right = list(line[index+1:index+5])
                left = list(line[index-5:index])
                total = right
                # print(f"v_range: {left,char,right, total}")
                if char == "@":
                    paper_count = right.count("@")
                    print(f"index position is: {index} total: {right} + {paper_count}" )
                    # print(f"Paper count at index {index}: {paper_count} Line: {line}")
                    if paper_count < 4:
                        new_line = replace_at(new_line, index, "x")

                        # print("BOOM")  
            new_lines.append(new_line)
            
            # break  # Remove this break to process all lines
    return new_lines, lines

if __name__ == "__main__":
    new_lines, lines = paper_locations()
    
    print(f"Day 4: How many rolls of newspaper can be accessed: {sum(paper.count('X') for paper in new_lines)}")
    print(f"work: {new_lines}")
    print(f"demo: {lines}")
