import sys  # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines()  # read in the input from STDIN
for i in range(len(lines)):
    print('Line ' + str(i+1) + ' is ' + str(len(lines[i])) + ' characters long.')
