#   Advent of Code 2022 - Day 11
#   Eetu Knutars - @knuutti

# Bruh, this time I actually had to think and not just code...

class MONKEY:
    def __init__(self) -> None:
        self.items: list = []
        self.operation: str = None
        self.operator: int = None
        self.division: int = None
        self.true_throw: int  = None
        self.false_throw: int = None
        self.inspections = 0

def main():

    file_name = "D11_data.txt"
    file = open(file_name, 'r')
    data = file.read().split("\n\n")
    file.close()

    # Part 1
    monkeys = createMonkeys(data)

    round = 0
    while round < 20:
        round += 1
        
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items[i]
                if monkey.operation == "sum":
                    item = item + monkey.operator
                elif monkey.operation == "product":
                    item = item * monkey.operator
                else:
                    item = item ** 2
                item = item // 3

                if item % monkey.division == 0:
                    monkeys[monkey.true_throw].items.append(item)
                else:
                    monkeys[monkey.false_throw].items.append(item)

                monkey.inspections += 1

            monkey.items = []

    print("Part 1:", monkey_business(monkeys))

    # Part 2
    monkeys = createMonkeys(data)

    # For this task we can't track the item values (since they are approaching to infinity...) 
    # so instead we will track the divisibility with the division value of each monkey

    # List containing the division values of each monkey
    monkey_checks = []
    for monkey in monkeys:
        monkey_checks.append(monkey.division)
    
    # Changing the items from values to dictionaries (containing the divisibility information)
    for monkey in monkeys:
        for i,item in enumerate(monkey.items):
            item_checks = {}
            for check in monkey_checks:
                item_checks[check] = item % check
            monkey.items[i] = item_checks

    # Starting the loop
    round = 0
    while round < 10000:

        round += 1
        
        # Going through each monkey in order
        for monkey in monkeys:
            # Inspecting all the items of the monkey
            for item in monkey.items:
                
                monkey.inspections += 1

                # Updating the check values (tracking divisibility) for an item
                for check in monkey_checks:

                    if monkey.operation == "sum":
                        # Sum
                        item[check] += monkey.operator
                    elif monkey.operation == "product":
                        # Product
                        item[check] = item[check] * monkey.operator
                    else:
                        # Exponent
                        item[check] = item[check] ** 2

                    # Updating the value if it's greater than the key value
                    if item[check] >= check:
                        item[check] = item[check] % check

                # Based on whether the item is dividible or not, pass the item to the next monkey
                if item[monkey.division] == 0:
                    # Item is dividible
                    monkeys[monkey.true_throw].items.append(item)
                else:
                    # Item is not dividible
                    monkeys[monkey.false_throw].items.append(item)

            monkey.items = []

    print("Part 2:", monkey_business(monkeys))

    return

# Function for calculating the level of monkey business
def monkey_business(monkeys):
    max_inspections = [0, 0]
    for monkey in monkeys:
        if monkey.inspections > max_inspections[0]:
            max_inspections[0] = monkey.inspections
            max_inspections.sort()
    return max_inspections[0]*max_inspections[1]

# Creating the monkey list
def createMonkeys(data):

    monkey_list: list[MONKEY] = []

    for monkey in data:
        line = monkey.split("\n")

        m = MONKEY()

        # Starting items
        m.items = line[1].lstrip("Starting items: ").split(", ")
        for i in range(len(m.items)):
            m.items[i] = int(m.items[i])
        
        # Operation
        if line[2].find("*") < 1:
            m.operation = "sum"
            m.operator = int(line[2][line[2].index("+")+1:])
        else:
            m.operation = "product"
            operator = line[2][line[2].index("*")+1:]
            if operator == " old":
                m.operation = "power"
                m.operator = 2
            else:
                m.operator = int(operator)

        m.division = int(line[3].lstrip("Test: divisible by "))
        m.true_throw = int(line[4].lstrip("If true: throw to monkey "))
        m.false_throw = int(line[5].lstrip("If false: throw to monkey "))

        monkey_list.append(m)

    return monkey_list



if __name__ == "__main__":
    main()