import sys  # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines()  # read in the input from STDIN
# input = lines[0]
# pat = lines[1]


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
