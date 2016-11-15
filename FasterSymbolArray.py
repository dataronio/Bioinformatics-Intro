import sys  # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines()  # read in the input from STDIN
# input = lines[0]
# pat = lines[1]


def FasterSymbolArray(Genome, symbol):
    def patterncount(Pattern, text):
        # this is the patterncount for replication of DNA
        count = 0
        n = len(text)
        k = len(Pattern)
        for i in range(n-k+1):
            if (text[i:i+k] == Pattern):
                count = count + 1
        return count

    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0: n//2]
    array[0] = patterncount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i] + 1
    return array

# print(FasterSymbolArray("AAAAGGGG", "A"))
