import utils


def splitranges(fileinput):
    return [idrange.split("-") for idrange in fileinput[0].split(",")]


def suminvalid(idranges):
    invalidsum = 0
    for idrange in idranges:
        if len(idrange[0]) == len(idrange[1]) and len(idrange[0]) % 2 == 1 and len(idrange[1]) % 2 == 1:
            continue
        current = idrange[0]
        max = int(idrange[1])
        while int(current) <= max:
            if len(current) % 2 == 1:
                current = str(10 ** (len(current)))
            else:
                first, second = halves(current)
                if first == second:
                    invalidsum += int(current)
                if int(first) > int(second):
                    new = str(int(first)) * 2
                elif first == str(10 ** len(first) - 1):
                    new = str(10 ** len(first)) * 2
                else:
                    new = str(int(first) + 1) * 2
                if new == current:
                    if first == str(10 ** len(first) - 1):
                        current = str(10 ** len(first)) * 2
                    else:
                        current = str(int(first) + 1) * 2
                else:
                    current = new
    return invalidsum


def sumcomplexinvalid(idranges):
    invalidsum = 0
    for idrange in idranges:
        maxlength = len(idrange[1]) // 2
        invalids = set()
        for length in range(1, maxlength + 1):
            invalids = invalids.union(checkinvalidbysize(idrange, length))
        for invalid in invalids:
            invalidsum += invalid
    return invalidsum


def checkinvalidbysize(idrange, length):
    invalid = set()
    current = idrange[0]
    multiplier = len(current) // length if len(current) % length == 0 and not len(current) == length else len(current) // length + 1
    if len(current) // 2 < length or not len(current) % length == 0:
        checkdigits = 10 ** (length - 1)
    elif int(current[0:length] * multiplier) < int(current):
        checkdigits = int(current[0:length]) + 1
    else:
        checkdigits = int(current[0:length])
    current = int(str(checkdigits) * multiplier)
    max = int(idrange[1])
    while current <= max and multiplier * length <= len(idrange[1]):
        invalid.add(current)
        checkdigits += 1
        if checkdigits == 10 ** length:
            multiplier += 1
            checkdigits = 10 ** (length - 1)
        current = int(str(checkdigits) * multiplier)
    return invalid


def halves(strnum):
    return strnum[0:len(strnum)//2], strnum[len(strnum)//2:]


if __name__ == "__main__":
    ranges = splitranges(utils.file_contents("./day2input.txt"))
    print(suminvalid(ranges))
    print(sumcomplexinvalid(ranges))