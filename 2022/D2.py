# Advent of Code 2022 - Day 2
# Eetu Knutars / @knuutti

def main():

    data_file = open('D2_data.txt', 'r')
    data = data_file.readlines()
    data_file.close()

    points1, points2 = 0,0

    m1 = [
    #    X  Y  Z
        [4, 8, 3],  # A
        [1, 5, 9],  # B
        [7, 2, 6]   # C
    ]

    m2 = [
    #    X  Y  Z
        [3, 4, 8],  # A
        [1, 5, 9],  # B
        [2, 6, 7]   # C
    ]

    for game in data:
        opponent = ord(game[0])-65
        you = ord(game[2])-88
        
        points1 += m1[opponent][you]
        points2 += m2[opponent][you]

    print(f"Part 1: {points1}")
    print(f"Part 2: {points2}")

    return



if __name__ == "__main__":
    main()
    
    

