def ApproximatePatternMatching(Pattern, text, d):
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
    Patterns = []
    for i in range(len(text) - len(Pattern) + 1):
        if HammingDistance(Pattern, text[i:i+len(Pattern)]) <= d:
                Patterns.append(i)
    return Patterns

# print(ApproximatePatternMatching("ATTCTGGA", "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT", 3))
