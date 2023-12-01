import csv

def arbitary_point_update(choice):
    """everything should be contained in a terrible if else loop!"""
    if choice == 'X':
        return 1
    elif choice == 'Y':
        return 2
    elif choice == 'Z':
        return 3
    else:
        return 0

def elf_fight(elf_choice, human_choice):
    """here is where the epic throwdown begins"""
    #Rock = A, X
    #Paper = B, Y
    #Scissors = C, Z

    game = {"A": {"X": 3, "Y": 6, "Z": 0},
            "B": {"X": 0, "Y": 3, "Z": 6}, 
            "C": {"X": 6, "Y": 0, "Z": 3}
            }
    
    return game[elf_choice][human_choice]


def main_elf_camping_fight_func():
    """a container for this craziness"""
    arbitary_score = 0
    elf_fight_score = 0

    with open('input.csv') as csv_file:
        psychic_elf = csv.reader(csv_file, delimiter=' ')
        for psychic_read in psychic_elf:
            # print(psychic_read)
            arbitary_score += arbitary_point_update(psychic_read[1])
            elf_fight_score += elf_fight(psychic_read[0], psychic_read[1])
        
        return arbitary_score + elf_fight_score

score = main_elf_camping_fight_func()
print("the score is: {}".format(score))