from math import sqrt
from argparse import ArgumentParser


def basic(n):
    if n <= 2:
        return None
    if n % 2 == 0:
        return [2, int(n/2)]
    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return [i, int(n/i)]


parser = ArgumentParser()
parser.add_argument('-n', '--number', help='number to be factorized', required=True)
args = parser.parse_args()

p1, p2 = basic(int(args.number))
print(args.number + ': ' + str(p1) + ', ' + str(p2))
