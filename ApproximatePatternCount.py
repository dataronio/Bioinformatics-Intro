def ApproximatePatternCount(Pattern, Text, d):
    def HammingDistance(p, q):
        n = len(p)
        m = len(q)
        count = 0
        if (n != m):
            return 0
        else:
            for i in range(n):
                if (p[i] != q[i]):
                    count = count + 1
        return count
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
                count = count + 1
    return count

print(ApproximatePatternCount("GAGG", "TTTAGAGCCTTCAGAGG", 2))
