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
    for i in range(len(warehouse)):
        row = warehouse[i]
        for j in range(len(row)):
            if row[j] == "@":
                neighbour_count = evaluate_neighbours(i, j, row, warehouse)
                if neighbour_count < 4:
                    acessible += 1

    print(acessible)


def evaluate_neighbours(i, j, row, warehouse):
    neighbour_count = 0
    neighbuors = []
    neighbuors.append(row[j - 1] if j - 1 >= 0 else "")
    neighbuors.append(row[j + 1] if j + 1 < len(row) else "")
    above_row = warehouse[i - 1] if i - 1 >= 0 else "-" * len(row)
    below_row = warehouse[i + 1] if i + 1 < len(warehouse) else "-" * len(row)
    neighbuors.append(above_row[j])
    neighbuors.append(below_row[j])
    neighbuors.append(above_row[j - 1] if j - 1 >= 0 else "")
    neighbuors.append(below_row[j - 1] if j - 1 >= 0 else "")
    neighbuors.append(above_row[j + 1] if j + 1 < len(row) else "")
    neighbuors.append(below_row[j + 1] if j + 1 < len(row) else "")
    for char in neighbuors:
        if char == "@":
            neighbour_count += 1
    return neighbour_count


if __name__ == "__main__":
    main()
