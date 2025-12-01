class Dial:
    def __init__(self):
        self.pointer = 50
        self.values = [x for x in range(100)]

    def increment(self, inc):
        self.pointer = self.pointer + inc
        if self.pointer >= 100:
            self.pointer = self.pointer % 100

        return self.values[self.pointer]

    def decrement(self, dec):
        inc = 100 - (dec % 100)
        _ = self.increment(inc)

        return self.values[self.pointer]


def main():
    dial = Dial()
    rotations = []
    zero_count = 0

    with open("../data.txt", "r") as file:
        rotations = [line for line in file]

    for rotation in rotations:
        if "L" in rotation:
            inc = int(rotation.strip("L"))
            val = dial.increment(inc)
            if val == 0:
                zero_count += 1
        elif "R" in rotation:
            dec = int(rotation.strip("R"))
            val = dial.decrement(dec)
            if val == 0:
                zero_count += 1
        else:
            print("Unexpected rotation")

    print(zero_count)


if __name__ == "__main__":
    main()
