import sys

digit_string = sys.argv[1]

sum = 0
for i in digit_string:
    i = int(i)
    sum += i
print(sum)
