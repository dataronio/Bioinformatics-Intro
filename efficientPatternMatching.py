import sys  # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines()  # read in the input from STDIN
lines = sys.stdin.read()


def efficientPatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions


outlist = PatternMatching("CTTGATCAT", lines)

print(" ".join([str(x) for x in outlist]))
