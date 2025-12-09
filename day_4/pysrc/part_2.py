def main():
    warehouse = []
    # warehouse = [
    #     "..@@.@@@@.",
    #     "@@@.@.@.@@",
    #     "@@@@@.@.@@",
    #     "@.@@@@..@.",
    #     "@@.@@@@.@@",
    #     ".@@@@@@@.@",
    #     ".@.@.@.@@@",
    #     "@.@@@.@@@@",
    #     ".@@@@@@@@.",
    #     "@.@.@@@.@.",
    # ]

    with open("../data.txt", "r") as file:
        warehouse = [line for line in file]

    warehouse = [line.strip() for line in warehouse]

    acessible = 0
    difference = 1
    while difference != 0:
        warehouse, new_acessible = calc_accessible(warehouse, acessible)
        difference = new_acessible - acessible
        acessible = new_acessible
        warehouse = replace_blanks(warehouse)

    print(acessible)
    for row in warehouse:
        print(row)


def calc_accessible(warehouse, acessible):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            row = warehouse[i]
            if row[j] == "@":
                neighbour_count = evaluate_neighbours(i, j, row, warehouse)
                if neighbour_count < 4:
                    acessible += 1
                    row_list = [char for char in row]
                    row_list[j] = "-"
                    new_row = "".join(char for char in row_list)
                    warehouse[i] = new_row
    return warehouse, acessible


def evaluate_neighbours(i, j, row, warehouse):
    neighbour_count = 0
    neighbuors = []
    neighbuors.append(row[j - 1] if j - 1 >= 0 else ".")
    neighbuors.append(row[j + 1] if j + 1 < len(row) else ".")
    above_row = warehouse[i - 1] if i - 1 >= 0 else "." * len(row)
    below_row = warehouse[i + 1] if i + 1 < len(warehouse) else "." * len(row)
    neighbuors.append(above_row[j])
    neighbuors.append(below_row[j])
    neighbuors.append(above_row[j - 1] if j - 1 >= 0 else ".")
    neighbuors.append(below_row[j - 1] if j - 1 >= 0 else ".")
    neighbuors.append(above_row[j + 1] if j + 1 < len(row) else ".")
    neighbuors.append(below_row[j + 1] if j + 1 < len(row) else ".")
    for char in neighbuors:
        if char == "@" or char == "-":
            neighbour_count += 1
    return neighbour_count


def replace_blanks(warehouse):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            row = warehouse[i]
            if row[j] == "-":
                row_list = [char for char in row]
                row_list[j] = "."
                new_row = "".join(char for char in row_list)
                warehouse[i] = new_row
    return warehouse


if __name__ == "__main__":
    main()
