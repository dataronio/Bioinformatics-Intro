# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text


def FrequentWords(Text, k):
    FrequentPatterns = []  # output variable
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
        FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
# HINT:   This code should be identical to when you last implemented CountDict


def CountDict(Text, k):
    Count = {}  # output variable
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last
# implemented PatternCount


def PatternCount(pattern, text):
    count = 0  # output variable
    n = len(text)
    k = len(pattern)
    for i in range(n-k+1):
        if (text[i:i+k] == pattern):
            count = count + 1
    return count


def remove_duplicates(items):
    b = []
    for i in items:
        if i not in b:
            b.append(i)
    return b


def ReverseComplement(Pattern):
    revComp = ''  # output variable
    # your code here
    dict = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    for i in Pattern:
        revComp += dict[i]
    return reverse(revComp)


# Copy your reverse function from the previous step here.
def reverse(text):
    return text[::-1]


def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions


def Skew(Genome):
    skew = []
    skew.append(0)
    Skewdict = {}
    n = len(Genome)
    for i in range(1, n+1):
        if Genome[i-1] == "G":
            skew.append(skew[i-1] + 1)
        elif Genome[i-1] == "C":
            skew.append(skew[i-1] - 1)
        else:
            skew.append(skew[i-1])
        Skewdict.update({i: skew[i]})
    Skewdict.update({0: skew[0]})
    # val = min(Skewdict.values())
    # list = [k for k, v in Skewdict.iteritems() if v == val]
    # print(list)
    return Skewdict


def MinSkew(Genome):
    def Skew(Genome):
        skew = []
        skew.append(0)
        Skewdict = {}
        n = len(Genome)
        for i in range(1, n+1):
            if Genome[i-1] == "G":
                skew.append(skew[i-1] + 1)
            elif Genome[i-1] == "C":
                skew.append(skew[i-1] - 1)
            else:
                skew.append(skew[i-1])
            Skewdict.update({i: skew[i]})
        Skewdict.update({0: skew[0]})
        return Skewdict
    val = min(Skewdict.values())
    list = [k for k, v in Skewdict.iteritems() if v == val]
    print(list)

# print(ReverseComplement("AAAACCCGGT"))
# print(PatternCount("TGT", "ACTGTACGATGATGTGTGTCAAAG"))

# crap = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
crap = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
print(FrequentWords(crap, 3))

Text = "AAACATAGGATCAAC"
pattern = "AA"
print(PatternMatching(pattern, Text))
