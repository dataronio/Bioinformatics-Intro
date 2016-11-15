import sys  # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines()  # read in the input from STDIN


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

print(ReverseComplement(lines[0]))
