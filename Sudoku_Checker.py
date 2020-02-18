__all__ = ["solved", "checkRow", "checkColumn", "checkGridN"]


def solved(grid):
    """
    Checks if the sudoku is solved
    :param grid: the grid of the sudoku
    :return: boolean -> true iff sudoku is valid and solved
    """

    if not checkRow(grid):
        print("Failed Row Check")
        return False

    if not checkColumn(grid):
        print("Failed Column Check")
        return False

    for n in range(len(grid)):
        if not checkGridN(n, grid):
            print("Failed grid Check")
            return False

    return True


def checkRow(grid):
    """
    Checks every row of the grid to see if the sudoku is valid or not
    :param grid: the grid of the sudoku
    :return: boolean -> true iff sudoku is valid in each row
    """

    for a in grid:
        for b in range(1,len(a)+1):
            if a.count(b) != 1:
                return False
    return True


def checkColumn(grid):
    """
    Checks every column of the grid to see if the sudoku is valid or not
    :param grid: the grid of the sudoku
    :return: boolean -> true iff sudoku is valid in each column
    """

    for a in range(len(grid)):
        vg = [i[a] for i in grid]
        for b in range(1,len(vg)+1):
            if vg.count(b) != 1:
                return False
    return True


def checkGridN(n, grid):
    """
    Checks the validity of grid with number n
    where n is:
    0 | 1 | 2
    ----------
    3 | 4 | 5
    ----------
    6 | 7 | 8
    :param n: the grid number in which user wants to check the validity
    :param grid: the grid of the sudoku
    :return: boolean -> true iff sudoku is valid in each column
    """

    numbers = []
    for a in range((n%3)*3, (n%3 + 1)*3):
        for b in range((n//3)*3, (n//3 + 1)*3):
            numbers.append(grid[b][a])

    for num in range(1,10):
        if numbers.count(num) != 1:
            return False
    return True


###############################
# Used for fail tests
###############################
# n = int(input())
# grid = [list(map(int, input().split())) for a in range(n)]
# print(solved(grid))