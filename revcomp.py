import sys

seq = sys.argv[1]

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

print("".join(complement.get(base, base) for base in reversed(seq)))