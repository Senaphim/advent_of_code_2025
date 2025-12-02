import math
import re


def main():
    data_string = ""
    all_invalid_ids = []

    with open("../data.txt", "r") as file:
        data_string = file.read()

    spans = data_string.split(",")
    for span in spans:
        start, stop = span.split("-")
        all_ids = [str(x) for x in range(int(start), int(stop) + 1)]
        invalid_ids = find_invalid(all_ids)
        all_invalid_ids += invalid_ids

    total = 0
    for id in all_invalid_ids:
        total += int(id)

    print(total)


def find_invalid(ids):
    invalid_ids = []

    for id in ids:
        factor_list = factorise(len(id))
        prefix_list = []
        for factor in factor_list:
            prefix_list.append(id[:factor])

        if prefix_match(prefix_list, id):
            invalid_ids.append(id)

    return invalid_ids


def factorise(num):
    factor_list = []
    for i in range(1, math.floor(num / 2) + 1):
        if num % i == 0:
            factor_list.append(i)

    return factor_list


def prefix_match(prefix_list, id):
    for prefix in prefix_list:
        match_count = len(re.findall(prefix, id))
        if match_count == len(id) / len(prefix) and match_count == 2:
            # print(f"{prefix=} {id=} {match_count=}, Yes")
            return True

    # print(f"{prefix=} {id=} {match_count=}, No")
    return False


if __name__ == "__main__":
    main()
