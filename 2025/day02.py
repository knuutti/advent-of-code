from math import sqrt

fname = "day02.txt"
file = open(fname, 'r')

id_ranges = file.readline().split(",")
file.close()

id_total = 0
id_total_gold = 0
id_total_silver = 0

for r in id_ranges:
    constraints = r.split("-")
    start_id = int(constraints[0])
    end_id = int(constraints[1])

    for id in range(start_id, end_id+1):
        invalid_id = False
        id_str = str(id)
        n = len(id_str)
        if n % 2 == 0:
            if id_str[0:int(n/2)] == id_str[int(n/2):]:
                id_total += id
                id_total_gold += id
                invalid_id = True

        if not invalid_id:
            # Checking for different seq lengths
            for i in range(1, int(n/2)+1):
                if n % i != 0: 
                    continue

                flag = False
                curr = id_str[0:i]
                for idx in range(2*i,n+1,i):
                    if curr == id_str[idx-i:idx]:
                        curr = id_str[idx-i:idx]
                    else:
                        flag = True
                        break

                if not flag:
                    id_total_gold += id
                    break



print("Silver:", id_total)
print("Gold:", id_total_gold)