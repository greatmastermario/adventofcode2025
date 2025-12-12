import utils


def coords(fileinput: list[str]) -> list[tuple[int, ...]]:
    return [tuple(int(coord) for coord in coords.split(",")) for coords in fileinput]


def distances(coordlist: list[tuple[int, ...]]) -> list[tuple[int, tuple[tuple[int, ...], tuple[int, ...]]]]:
    distanceset = set()
    for coord1 in range(0, len(coordlist) - 1):
        for coord2 in range(coord1 + 1, len(coordlist)):
            #distanceset is (distance, coord)
            distanceset.add((((coordlist[coord1][0] - coordlist[coord2][0]) ** 2) + \
                             ((coordlist[coord1][1] - coordlist[coord2][1]) ** 2) + \
                             ((coordlist[coord1][2] - coordlist[coord2][2]) ** 2),
                             (coordlist[coord1], coordlist[coord2])))
    return sorted(list(distanceset))


def smallestconnections(coordlist: list[tuple[int, ...]], maxconnections: int):
    distancelist = distances(coordlist)
    coordsset = {frozenset({coord}) for coord in coordlist}
    for index in range(maxconnections):
        toremove = set()
        found = set()
        distance, distcoords = distancelist[index]
        for coordset in coordsset:
            if distcoords[0] in coordset:
                found = found.union(coordset)
                toremove.add(coordset)
                if len(toremove) == 2:
                    break
            if distcoords[1] in coordset:
                found = found.union(coordset)
                toremove.add(coordset)
                if len(toremove) == 2:
                    break
        for removal in toremove:
            coordsset.remove(removal)
        coordsset.add(frozenset(found))
    sortedcircuitsizes = sorted([len(coordset) for coordset in coordsset], reverse=True)
    return sortedcircuitsizes[0] * sortedcircuitsizes[1] * sortedcircuitsizes[2]


def singlecircuitdistance(coordlist: list[tuple[int, ...]]):
    distancelist = distances(coordlist)
    coordsset = {frozenset({coord}) for coord in coordlist}
    for index in range(len(distancelist)):
        toremove = set()
        found = set()
        distance, distcoords = distancelist[index]
        for coordset in coordsset:
            if distcoords[0] in coordset:
                found = found.union(coordset)
                toremove.add(coordset)
                if len(toremove) == 2:
                    break
            if distcoords[1] in coordset:
                found = found.union(coordset)
                toremove.add(coordset)
                if len(toremove) == 2:
                    break
        for removal in toremove:
            coordsset.remove(removal)
        coordsset.add(frozenset(found))
        if len(coordsset) == 1:
            break
    return distcoords[0][0] * distcoords[1][0]

if __name__ == "__main__":
    print(smallestconnections(coords(utils.file_contents("./day8input.txt")), 1000))
    print(singlecircuitdistance(coords(utils.file_contents("./day8input.txt"))))