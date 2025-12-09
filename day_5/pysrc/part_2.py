def main():
    data = []
    # data = [
    #     "3-5",
    #     "10-14",
    #     "16-20",
    #     "12-18",
    #     "",
    #     "1",
    #     "5",
    #     "8",
    #     "11",
    #     "17",
    #     "32",
    # ]

    with open("../data.txt") as file:
        data = [line for line in file]

    data = [line.strip() for line in data]
    ranges = []
    ids = []
    blank_flag = True
    for i in range(len(data)):
        if data[i] == "":
            blank_flag = False
            continue
        if blank_flag:
            ranges.append(data[i])
        else:
            ids.append(int(data[i]))

    fresh_count = 0
    for id in ids:
        for rng in ranges:
            start, stop = rng.split("-")
            start = int(start)
            stop = int(stop)
            if id >= start and id <= stop:
                fresh_count += 1
                break

    print(fresh_count)


if __name__ == "__main__":
    main()
