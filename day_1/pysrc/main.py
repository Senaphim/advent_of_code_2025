class Dial:
    def __init__(self):
        self.pointer = 50
        self.values = [x for x in range(100)]

    def increment(self, inc):
        self.pointer = self.pointer + inc
        if self.pointer >= 100:
            self.pointer -= 100

        return self.values[self.pointer]

    def decrement(self, dec):
        self.pointer = self.pointer - dec
        if self.pointer < 0:
            self.pointer += 100

        return self.values[self.pointer]


def main():
    dial = Dial()
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    zero_count = 0

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
