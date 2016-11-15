import sys  # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines()  # read in the input from STDIN
''' most frequent k-mers'''


def frequentWords(Text, k):

    # add in patterncount as helper function
    def patterncount(Pattern, text):
        # this is the patterncount for replication of DNA
        count = 0
        for i in xrange(len(text)-len(Pattern)+1):
            if (text[i:i+len(Pattern)] == Pattern):
                count = count + 1
        return count

    frequentPattern = set()
    count = {}
    for i in xrange(len(Text) - k):
        count[i] = patterncount(Text[i:i+k], Text)
    maxcount = max(count.values())
    for i in xrange(len(Text) - k):
        if count[i] == maxcount:
            frequentPattern.add(Text[i:i+k])
    return frequentPattern


outlist = list(frequentWords(str(lines[0]), int(lines[1])))
print(" ".join([str(x) for x in outlist]))


def max(list):
    m = list[0]
    for item in list:
        if item > m:
            m = item
    return m
