import utils


def countsplits(fileinput: list[str]):
    splitcount = 0
    beams = {fileinput[0].find("S"): 1}
    for row in fileinput[1:]:
        newbeams = beams.copy()
        splitter = row.find("^")
        while not splitter == -1:
            if splitter in beams:
                thiscount = newbeams[splitter]
                del newbeams[splitter]
                newbeams[splitter - 1] = thiscount if not splitter - 1 in newbeams.keys() else newbeams[splitter - 1] + thiscount
                newbeams[splitter + 1] = thiscount if not splitter + 1 in newbeams.keys() else newbeams[splitter + 1] + thiscount
                splitcount += 1
            splitter = row.find("^", splitter + 1)
        beams = newbeams
    return splitcount, sum(beams.values())


if __name__ == "__main__":
    count, quantumcount = countsplits(utils.file_contents("./day7input.txt"))
    print(count)
    print(quantumcount)