import sys  # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines()  # read in the input from STDIN
# input = lines[0]
# pat = lines[1]


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

print(HammingDistance("GGGCCGTTGGT", "GGACCGTTGAC"))
print(HammingDistance("CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA","CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"))
