from numpy import argmax

fname = "day03.txt"
file = open(fname, 'r')
banks = file.read().splitlines()
    
def best_batteries(M: int) -> int:

    total_joltage = 0

    for b in banks:
        n = len(b)
        best_joltage = 0
        joltages = list(map(lambda i: int(b[i]), list(range(n))))

        for i in range(M-1,-1,-1):

            if i == 0:
                best_joltage += max(joltages)

            else:
                largest_index = argmax(joltages[:-i])
                largest_value = joltages[largest_index]
                joltages = joltages[largest_index+1:]
                best_joltage += largest_value * 10**(i)
            
        total_joltage += best_joltage

    return total_joltage

print("Silver:", best_batteries(2))
print("Gold:", best_batteries(12))



    