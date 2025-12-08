import utils


def totaljoltages(input, digits):
    total = 0
    for line in input:
        total += int(maxjoltage(line, digits, 0)[1])
    return total


def maxjoltage(line, digits, index):
    for digit in range(9, -1, -1):
        foundindex = line[index:].find(str(digit))
        if foundindex != -1 and foundindex + index <= len(line) - digits:
            if digits == 1:
                return True, str(digit)
            found, remainingdigits = maxjoltage(line, digits - 1, foundindex + index + 1)
            if found:
                return True, line[foundindex + index] + remainingdigits
    return False, None


if __name__ == "__main__":
    print(totaljoltages(utils.file_contents("./day3input.txt"), 2))
    print(totaljoltages(utils.file_contents("./day3input.txt"), 12))