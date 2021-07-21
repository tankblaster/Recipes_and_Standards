import csv


# globally used variables
recipes = []


def load_data(filename="Recipes.csv", ):
    # recipe format - {Creator_credits},{Title},{Ingredient_tag1;Ingredient_tag2;...},
    # {Required_capability1;Required_capability2;..."}, {Instruction1;Instruction2;...}
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            recipes.append([row[0], row[1], row[2].split(';'), row[3].split(';'), row[4].split(';')])


def print_num(print_list):
    for idx, item in enumerate(print_list):
        print(f"{idx+1}: {item}")


# prints the given recipe in a standard format
def fancy_print(recipe):
    print(f"Made by: {recipe[0]}\n")
    print(f"{recipe[1]}\n")

    print("Ingredients:")
    print_num(recipe[2])

    print("\nCapabilities: ")
    print_num(recipe[3])

    print("\nInstructions:")
    print_num(recipe[4])


if __name__ == '__main__':
    load_data()
    fancy_print(recipes[0])
