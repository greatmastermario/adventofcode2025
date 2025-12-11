import re
import utils


def solve(sheet, index):
    if sheet[-1][index] == "+":
        solution = 0
        for row in range(0, len(sheet) - 1):
            solution += sheet[row][index]
    else:
        solution = 1
        for row in range(0, len(sheet) - 1):
            solution *= sheet[row][index]
    return solution


def sumsolutions(sheet):
    total = 0
    for index in range(0, len(sheet[0])):
        total += solve(sheet, index)
    return total


def splitsheet(fileinput):
    sheet = []
    for index, row in enumerate(fileinput):
        newrow = []
        for val in re.split("\\s+", row):
            if not val == "": # in case there are preceding whitespace chars
                if index == len(fileinput) - 1:
                    newrow.append(val)
                else:
                    newrow.append(int(val))
        sheet.append(newrow)
    return sheet


def solverighttoleft(fileinput):
    maxindex = -1
    for row in fileinput:
        maxindex = max(maxindex, len(row) - 1)
    solution = 0
    nums = []
    for column in range(maxindex, -1, -1):
        digits = []
        for row in fileinput:
            if column < len(row):
                if row[column] == "+":
                    if digits:
                        nums.append(int("".join(digits)))
                    for num in nums:
                        solution += num
                    nums = []
                    digits = []
                elif row[column] == "*":
                    if digits:
                        nums.append(int("".join(digits)))
                    multiply = 1
                    for num in nums:
                        multiply *= num
                    solution += multiply
                    nums = []
                    digits = []
                elif not row[column] == " ":
                    digits.append(row[column])
        if digits:
            nums.append(int("".join(digits)))
    return solution


if __name__ == "__main__":
    print(sumsolutions(splitsheet(utils.file_contents("./day6input.txt"))))
    print(solverighttoleft(utils.file_contents("./day6input.txt")))