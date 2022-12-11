from math import factorial, prod

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

    round = 1
    while round < 21:
        
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

        round += 1

    max_inspections = [0, 0]
    for monkey in monkeys:
        if monkey.inspections > max_inspections[0]:
            max_inspections[0] = monkey.inspections
            max_inspections.sort()

    print("Part 1:", max_inspections[1]*max_inspections[0])

    # Part 2
    monkeys = createMonkeys(data)

    monkey_checks = []
    for monkey in monkeys:
        monkey_checks.append(monkey.division)
    for monkey in monkeys:
        for i,item in enumerate(monkey.items):
            item_checks = {}
            for check in monkey_checks:
                item_checks[check] = item % check
            monkey.items[i] = item_checks

    round = 1
    while round < 10001:
        
        for monkey in monkeys:
            for item in monkey.items:
                # New inspection
                monkey.inspections += 1

                # Updating the check values for an item
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

                    item[check] 

                    # Updating the value if it's greater than the key value
                    if item[check] >= check:
                        item[check] = item[check] % check

                # Based on whether the item is dividible or not, pass the item
                # to the next monkey
                if item[monkey.division] == 0:
                    # Item is dividible
                    monkeys[monkey.true_throw].items.append(item)
                else:
                    # Item is not dividible
                    monkeys[monkey.false_throw].items.append(item)

            monkey.items = []

        round += 1

    # Calculating the level of monkey business
    max_inspections = [0, 0]
    for monkey in monkeys:
        if monkey.inspections > max_inspections[0]:
            max_inspections[0] = monkey.inspections
            max_inspections.sort()

    print("Part 2:", max_inspections[0]*max_inspections[1])

    return

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