def main():
    banks = []

    with open("../data.txt", "r") as file:
        banks = [line for line in file]

    total_power = 0

    for bank in banks:
        bank = bank.strip()
        if bank == "":
            continue

        bank_list = [int(x) for x in list(bank)]
        max_value = max(bank_list[:-1])
        max_value_index = bank_list.index(max_value)
        secondary_max = max(bank_list[max_value_index + 1 :])
        output_power = int(str(max_value) + str(secondary_max))
        total_power += output_power

    print(total_power)


if __name__ == "__main__":
    main()
