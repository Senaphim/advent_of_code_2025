import math


class Dial:
    def __init__(self):
        self.pointer = 50
        self.values = [x for x in range(100)]
        self.zeroes = 0

    def increment(self, inc):
        rotations = math.floor(inc / 100)
        self.zeroes += rotations

        remainder = inc % 100
        self.pointer += remainder
        if self.pointer >= 100:
            self.zeroes += 1
            self.pointer = self.pointer - 100

    def decrement(self, dec):
        rotations = math.floor(dec / 100)
        self.zeroes += rotations

        current = self.pointer
        remainder = dec % 100

        self.pointer -= remainder
        if self.pointer == 0:
            self.zeroes += 1
        elif self.pointer < 0:
            if current != 0:
                self.zeroes += 1
            self.pointer = self.pointer + 100


def main():
    dial = Dial()
    rotations = []
    # rotations = ["R50", "L50", "R50"]

    with open("../data.txt", "r") as file:
        rotations = [line for line in file]

    for rotation in rotations:
        if "L" in rotation:
            inc = int(rotation.strip("L"))
            dial.increment(inc)
        elif "R" in rotation:
            dec = int(rotation.strip("R"))
            dial.decrement(dec)
        else:
            print("Unexpected rotation")

    print(dial.zeroes)


if __name__ == "__main__":
    main()
