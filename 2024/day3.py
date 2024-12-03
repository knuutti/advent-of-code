import re

silver = 0
gold = 0

data = open("input_day3.txt", 'r').read()

# Parses all valid mul, do and dont substrings into one list
substrings = re.findall("mul[(]\\d+,\\d+[)]|do[(][)]|don't[(][)]", data)

do = True
for s in substrings:
    if s[0] == "m":
        a = s.split(",")
        product = int(a[1][:-1])*int(a[0][4:])
        silver += product
        gold += product*do
    elif s[2] == "n":
        do = False
    elif s[0] == "d": do = True

print("Silver:", silver)
print("Gold", gold)