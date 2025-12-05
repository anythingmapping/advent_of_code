# Day 4: Newspaper Delivery Routes

RANGE = "demo_range.txt"
ITEM = "demo_item.txt"
RANGE = "input_range.txt"
ITEM = "input_item.txt"


def ingredients():
    fresh_ingredients = 0
    for item in open(ITEM):
        # print(line.strip())
        print(f"Ingredient to examine: {item.strip()}")
        item_status = "Rotten"
        
        for r in open(RANGE):
            start, finish = r.split("-")
            print(f"Start: {start} Finish: {finish.strip()}")

            if (int(item) >= int(start) and int(item) <= int(finish) and item_status == "Rotten"):
                fresh_ingredients +=1
                item_status = "Fresh"
                print(f"Ingrident {item} is status {item_status}! because {r} is between {int(start)} and {finish.strip()}")
                break
            else:
                print(f"Ingrident {item.strip()} Item Status: {item_status}.")
        print("-----\n")
    
    print(f"Fresh ingredients: {fresh_ingredients}")




            

if __name__ == "__main__":
    ingredients()
   
