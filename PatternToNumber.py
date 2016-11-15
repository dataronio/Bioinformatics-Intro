import sys  # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines()  # read in the input from STDIN


def PatternToNumber(Pattern):
    def SymbolToNumber(symbol):
        dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        return dict[symbol]
    if len(Pattern) == 0:
        return 0
    lastsymbol = Pattern[-1]
    prefix = Pattern[0:len(Pattern)-1]
    return 4 * PatternToNumber(prefix) + SymbolToNumber(lastsymbol)

sample = "AGT"
#print(PatternToNumber(sample))
print(PatternToNumber(lines[0]))
