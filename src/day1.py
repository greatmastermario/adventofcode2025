import utils


def countonzero(fileinput, countextraclicks):
    zeros = 0
    position = 50
    for line in fileinput:
        direction = line[0]
        distance = int(line[1:])
        if countextraclicks:
            zeros += extras(position, distance, direction)
        position = (position - distance) % 100 if direction == "L" else (position + distance) % 100
        if position == 0:
            zeros += 1
    return zeros


def extras(position, distance, direction):
    extra = distance // 100
    distance = distance % 100
    newposition = (position - distance) % 100 if direction == "L" else (position + distance) % 100
    if direction == "L":
        if newposition > position and not position == 0:
            extra += 1
    elif newposition < position and not newposition == 0:
        extra += 1
    return extra


if __name__ == "__main__":
    print(countonzero(utils.file_contents("./day1input.txt"), False))
    print(countonzero(utils.file_contents("./day1input.txt"), True))