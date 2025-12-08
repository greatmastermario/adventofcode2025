import utils


def data(fileinput):
    addingredients = False
    ingredients = set()
    fresh = set()
    for line in fileinput:
        if line == "":
            addingredients = True
        elif addingredients:
            ingredients.add(int(line))
        else:
            freshrange = line.split("-")
            fresh.add((int(freshrange[0]), int(freshrange[1])))
    return fresh, ingredients


def countfresh(fresh, ingredients):
    count = 0
    for ingredient in ingredients:
        count = count + 1 if isfresh(ingredient, fresh) else count
    return count


def isfresh(ingredient, fresh):
    for freshrange in fresh:
        if ingredient >= freshrange[0] and ingredient <= freshrange[1]:
            return True
    return False


def overlap(freshrange, otherfreshrange):
    first = freshrange if freshrange[0] < otherfreshrange[0] else otherfreshrange
    second = otherfreshrange if first == freshrange else freshrange
    if first[1] >= second[0]:
        return True, (first[0], max(first[1], second[1]))
    else:
        return False, None


def countfreshrange(fresh):
    for freshrange in fresh:
        for other in fresh:
            if freshrange == other:
                continue
            isoverlap, newrange = overlap(freshrange, other)
            if isoverlap:
                newfresh = fresh.difference({freshrange, other})
                newfresh.add(newrange)
                return countfreshrange(newfresh)
    count = 0
    for freshrange in fresh:
        count += freshrange[1] - freshrange[0] + 1
    return count


if __name__ == "__main__":
    fresh, ingredients = data(utils.file_contents("./day5input.txt"))
    print(countfresh(fresh, ingredients))
    print(countfreshrange(fresh))