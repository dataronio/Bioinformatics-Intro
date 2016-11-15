import sys  # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines()  # read in the input from STDIN
input = lines[0]
pat = lines[1]


def patterncount(Pattern, text):
    # this is the patterncount for replication of DNA
    count = 0
    n = len(text)
    k = len(Pattern)
    for i in range(n-k+1):
        if (text[i:i+k] == Pattern):
            count = count + 1
    return count
print(patterncount(pat, input))
