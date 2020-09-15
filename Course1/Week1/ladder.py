import sys

number = int(sys.argv[1])
n_of_stairs = 1
n_of_spaces = number - 1

while (number > 0):
    print(" "*n_of_spaces + "#"*n_of_stairs)
    n_of_stairs += 1
    n_of_spaces -= 1
    number -= 1
