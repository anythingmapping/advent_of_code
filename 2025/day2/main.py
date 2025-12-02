
FILE = "input.txt"
# FILE = "demo.txt"

def check_validity(i):
    # print(f"Analyzing number: {i}")
    if len(str(i)) % 2 == 0:
        # print(f"INVALID NUMBER")
        # print(f"Not divisible by two:{i} {len(i) % 2}")
        return True




def has_repeating_pattern(beginning, end):
    returned_values = []
    beginning = int(beginning)
    end = int(end)
    for i in range(beginning, end + 1):
        # i = str(i)
        if check_validity(i):
            print(f"    - {i}")
                        
            half = len(str(i)) // 2
            # print(f"halfway point {half}")
            first_half = str(i)[:half]
            # print(first_half)
            second_half = str(i)[half:]
            # print(second_half)
            if first_half == second_half:
                print(f"    - BOOM: {i}")
                returned_values.append(i)
    return returned_values


        

        
        

        # if first_half == second_half:
        #     print(f"Found repeating pattern in number: {i}")
        #     return True
        # else: return False
   
    # return beginning, end


def extract_lines():
    """ 
    Extract lines from demo.txt and analyze each entry.
    """
    total = 0
    total_of_errors = []
    with open(FILE) as f:
        full_line = f.readlines()
        entry = full_line[0].split(",")
        for i in entry:
            print(f"Next Entry: {i}")
            a,b = i.split("-")
            print(f"Analyzing Range: a:{a} to b:{b}")
            total_of_errors.append(has_repeating_pattern(a, b))
            total += 1
            
            

        return total, total_of_errors
        

if __name__ == "__main__":
    # print("Day 2")
    total, total_of_errors = extract_lines()
    print(f"Total Records Processed: {total}")
    print(f"Total Errors Found: {total_of_errors}")
    flattened = [x for inner in total_of_errors for x in inner]
    total = sum(flattened)
    print(f"Final Total of Errors: {total}")
