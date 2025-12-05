def main():
    banks = []
    # banks = [
    #     "987654321111111",
    #     "811111111111119",
    #     "234234234234278",
    #     "818181911112111",
    # ]

    with open("../data.txt", "r") as file:
        banks = [line for line in file]

    total_power = 0

    for bank in banks:
        bank = bank.strip()
        if bank == "":
            continue

        bank_list = [int(x) for x in list(bank)]
        max_string = ""
        start_index = 0
        for i in range(12):
            if i == 11:
                max_value = max(bank_list)
            else:
                max_value = max(bank_list[: i - 11])
            start_index = bank_list.index(max_value) + 1
            bank_list = bank_list[start_index:]
            max_string += str(max_value)
        print(max_string)
        output_power = int(max_string)
        total_power += output_power

    print(total_power)


if __name__ == "__main__":
    main()
