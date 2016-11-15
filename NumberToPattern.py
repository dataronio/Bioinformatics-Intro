import sys  # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines()  # read in the input from STDIN


def NumberToPattern(index, k):
    def NumberToSymbol(number):
        dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
        return dict[number]
    if k == 1:
        return NumberToSymbol(index)
    answer = divmod(index, 4)
    prefixIndex = answer[1]
    r = answer[2]
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex, k - 1)
    return PrefixPattern + symbol

print(NumberToPattern(lines[0], lines[1]))
