def CountDict(Text, k):
    Count = {}
    # fill in the rest of the CountDict function here.
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Copy your PatternCount function from Replication.py into the line below.


def PatternCount(pattern, text):
    # this is the patterncount for replication of DNA
    count = 0
    n = len(text)
    k = len(pattern)
    for i in range(n-k+1):
        if (text[i:i+k] == pattern):
            count = count + 1
    return count
