def main():
    fname = "./2023/Day 13/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    patterns = get_patterns(data)
    silver, gold = 0,0
    for pattern in patterns:
        silver += counter(pattern, 0)
        gold += counter(pattern, 1)
    print("Part 1:",silver)
    print("Part 2:",gold)

# Get pattern matrices from data
def get_patterns(data):
    patterns = []
    cur_pattern = []
    for row in data:
        if not len(row):
            patterns.append(cur_pattern)
            cur_pattern = []
            continue
        cur_pattern.append(row)
    patterns.append(cur_pattern)
    return patterns

# Find the mirror index in a pattern
def counter(pattern, mode):
        # Horizontal mirrors
        for r in range(0, len(pattern)-1):
            mirror_length = min(r, len(pattern)-r-2)
            s1 = pattern[r-mirror_length:r+1]
            s2 = pattern[r+1:r+2+mirror_length]
            if condition(s1,s2,mode): return 100*(r+1)
        # Vertical mirrors
        for c in range(0, len(pattern[0])-1):
            mirror_length = min(c, len(pattern[0])-c-2)
            s1,s2 = [], []
            for c1 in range(c-mirror_length, c+1):
                s = ""
                for r in range(0,len(pattern)):
                    s += pattern[r][c1]
                s1.append(s)
            for c2 in range(c+1, c+2+mirror_length):
                s = ""
                for r in range(0,len(pattern)):
                    s += pattern[r][c2]
                s2.append(s)
            if condition(s1,s2,mode): return c+1

# Check if mirror is in the place        
def condition(s1,s2,mode):
    s2 = s2[::-1]
    s1 = ''.join(s1)
    s2 = ''.join(s2)
    diffs = 0
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            diffs+=1
    if diffs == mode:
        return True
    return False


if __name__ == '__main__':
    main()

