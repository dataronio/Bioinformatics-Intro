import random
import sys  # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines()  # read in the input from STDIN
# =input = lines[0]
# pat = lines[1]


ex1 = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
text = "ACGGGGATTACC"
row1 = [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0]
row2 = [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6]
row3 = [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
row4 = [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
pro = {'A': row1, 'C': row2, 'G': row3, 'T': row4}
text1 = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
pro1 = {'A': [0.2, 0.2, 0.3, 0.2, 0.3], 'C': [0.4, 0.3, 0.1, 0.5, 0.1], 'G': [0.3, 0.3, 0.5, 0.2, 0.4], 'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
text2 = "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA"
pro2 = {'A': [0.2, 0.2, 0.3, 0.2, 0.3], 'C': [0.4, 0.3, 0.1, 0.5, 0.1], 'G': [0.3, 0.3, 0.5, 0.2, 0.4], 'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
pro3 = {'A': [0.8, 0.0, 0.0, 0.2], 'C': [0.0, 0.6, 0.2, 0.0], 'G': [0.2, 0.2, 0.8, 0.0], 'T': [0.0, 0.2, 0.0, 0.8]}


# print(pro)


def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

# print(Count(ex1))


def Profile(Motifs):
    profile = {}
    count = Count(Motifs)
    # print(count)
    t = len(Motifs[0])
    k = len(Motifs)
    for symbol in "ACGT":
        profile[symbol] = []
        for i in range(t):
            profile[symbol].append(0.0)
    for symbol in "ACGT":
        for j in range(t):
            profile[symbol][j] = count[symbol][j] / float(k)
    return profile

# print(Profile(['GGC']))


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

# print(Consensus(ex1))


def Score(Motifs):
    score = 0
    consensus = Consensus(Motifs)
    k = len(Motifs)
    t = len(consensus)
    for i in range(k):
        for j in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1
    return score

# print(Score(ex1))


def Pr(Text, Profile):
    pr = 1
    k = len(Text)
    for i in range(k):
        pr *= Profile[Text[i]][i]
    return pr

# print(Pr(text, pro))

Dna2 = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC", "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG", "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC", "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC", "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG", "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA", "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA", "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG", "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG", "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]


def ProfileMostProbablePattern(Text, k, Profile):
    Prob = 0
    best = Text[0:k]
    l = len(Text)
    for i in range(l-k+1):
        pr = Pr(Text[i:i+k], Profile)
        if pr > Prob:
            Prob = pr
            best = Text[i:i+k]
    return best

# print(ProfileMostProbablePattern(text2, 5, pro2))
Dna1 = ["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"]


def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    # print(n)
    # print(Dna)
    # print(BestMotifs)
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        P = Profile(Motifs[0:1])
        # print(Motifs)
        # print(P)
        for l in range(1, t):
            # print(l)
            Motifs.append(ProfileMostProbablePattern(Dna[l], k, P))
            P = Profile(Motifs)
            # print(Motifs)
            # print(P)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# print(GreedyMotifSearch(Dna2, 15, 10))


# def CalculateEntropy(Profile):
#    k = len(Profile['A'])


def CountWithPseudocounts(Motifs):
    count = Count(Motifs)
    for letter in "ACGT":
        count[letter] = [x+1 for x in count[letter]]
    return count

# print(CountWithPseudocounts(ex1))


def ProfileWithPseudocounts(Motifs):
    count = CountWithPseudocounts(Motifs)
    profile = {}
    t = len(Motifs[0])
    k = len(Motifs)
    for symbol in "ACGT":
        profile[symbol] = []
        for i in range(t):
            profile[symbol].append(0.0)
    for symbol in "ACGT":
        for j in range(t):
            profile[symbol][j] = count[symbol][j] / (float(k) + 4)
    return profile

# print(Profile(ex1))
# print(ProfileWithPseudocounts(ex1))


def GreedyMotifSearchWithPsuedocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        P = ProfileWithPseudocounts(Motifs[0:1])
        for l in range(1, t):
            Motifs.append(ProfileMostProbablePattern(Dna[l], k, P))
            P = ProfileWithPseudocounts(Motifs)
            # print(Motifs)
            # print(P)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


Dna3 = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]


def Motifs(Profile, Dna):
    output = []
    k = len(Profile['A'])
    t = len(Dna)
    for i in range(t):
        output.append(ProfileMostProbablePattern(Dna[i], k, Profile))
    return output


# print(Motifs(pro3, Dna3))

def RandomMotifs(Dna, k, t):
    motif = []
    l = len(Dna[0])
    for i in range(t):
        start = random.randint(0, l - k)
        motif.append(Dna[i][start:start+k])
    return motif

# print(RandomMotifs(Dna3, 3, 5))


def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def Normalize(Probabilities):
    sum = 0
    for item in Probabilities.keys():
        sum += Probabilities[item]
    for item in Probabilities.keys():
        Probabilities[item] = Probabilities[item] / float(sum)
    return Probabilities


def WeightedDie(Probabilities):
    prob = 0
    kmer = ""
    roll = random.uniform(0, 1)
    for item in Probabilities.keys():
        prob += Probabilities[item]
        if roll < prob:
            kmer = item
            return kmer
    return kmer


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0, n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


def GibbsSampler(Dna, k, t, N):
    BestMotifs = []
    motifs = RandomMotifs(Dna, k, t)
    BestMotifs = motifs
    for j in range(N):
        i = random.randint(0, t-1)
        del motifs[i]
        profile = ProfileWithPseudocounts(motifs)
        motifs.insert(i, ProfileGeneratedString(Dna[i], profile, k))
        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs
    return BestMotifs
