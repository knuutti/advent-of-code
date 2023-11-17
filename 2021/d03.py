import numpy

def main():

    fname = "d3_data.txt"
    file = open(fname, 'r')
    content = file.readlines()
    
    n = len(content)
    m = len(content[0]) - 1

    bits = [0 for _ in range(m)]

    for row in content:
        for i,bit in enumerate(row.rstrip("\n")):
            bits[i] += int(bit)

    # Creating the binary numbers based on bit count for each slot
    gamma = []
    epsilon = []
    for bit in bits:
        if bit > n/2:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    # Converting to decimal
    gamma_desimal = 0
    epsilon_desimal = 0
    for i in range(m):
        gamma_desimal += gamma[i] * (2**(m-1-i))
        epsilon_desimal += epsilon[i] * (2**(m-1-i))

    print(f"Part 1: {gamma_desimal * epsilon_desimal}")

    cont = content
    temp = []
    bit_counter = 0
    a = 0
    b = 0
    i = 0
    while (i < m):
        for row in cont:
            bit_counter += int(row[i])
            a += 1
        if bit_counter < a/2:
            b = 0
        else:
            b = 1
        for row in cont:
            if int(row[i]) == b:
                temp.append(row)
        cont = temp
        temp = []
        bit_counter = 0
        a = 0
        i += 1

    oxygen = cont[0].rstrip("\n")

    cont = content
    temp = []
    bit_counter = 0
    a = 0
    b = 0
    i = 0
    while (i < m):
        for row in cont:
            bit_counter += int(row[i])
            a += 1
        if bit_counter < a/2:
            b = 1
        else:
            b = 0
        for row in cont:
            if int(row[i]) == b:
                temp.append(row)
        cont = temp
        if len(cont) == 1:
            break
        temp = []
        bit_counter = 0
        a = 0
        i += 1

    co2 = cont[0].rstrip("\n")

    oxy_desi = 0
    co2_desi = 0
    for i in range(m):
        oxy_desi += int(oxygen[i]) * (2**(m-1-i))
        co2_desi += int(co2[i]) * (2**(m-1-i))

    print(f"Part 2: {oxy_desi * co2_desi}")

            


if __name__ == "__main__":
    main()






    