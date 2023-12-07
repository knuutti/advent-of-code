# Advent of Code 2023 - Day 7
# Eetu Knutars / @knuutti

from collections import OrderedDict

def main():   
    fname = "./2023/Day 07/day7_bigboy.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    print("Part 1:",analyse(data,0))
    print("Part 2:",analyse(data,1))

    # Doesn't work for data with dublicate hands

def analyse(data, mode):
    # Generates hands using the Hand class
    hands = {}

    for i,row in enumerate(data):
        row = row.split()
        new_hand = Hand(row[0],row[1], mode)
        hands[new_hand.level] = new_hand.bid

    od = OrderedDict(sorted(hands.items(), reverse=True))

    total = 0
    for i,h in enumerate(od):
        rank = (len(od)-i)
        bid = od[h]
        total += rank*bid
    return total

class Hand():
    def __init__(self, hand, bid, mode):
        self.cards = []
        self.uniques = {}
        self.bid = int(bid)
        self.joker_indexes = self.determine_cards(hand, mode)
        self.level = self.determine_level()

    # Gets the level (goodness) of the hand
    def determine_level(self):
        if len(self.joker_indexes) < 5:

            # Joker logic: replace jokers with value that occur the most
            sorted_uniques = sorted(self.uniques.items(), key=lambda x:x[1])
            real_cards = self.cards.copy()
            for i in self.joker_indexes:
                self.cards.insert(i,sorted_uniques[-1][0])
                self.uniques[sorted_uniques[-1][0]] += 1
                real_cards.insert(i,1)
            
            # Determining the level of the hand
            level = 2*(5 - len(list(self.uniques.values())))
            
            # 4 uniques vs. full house
            if level == 6 and max(list(self.uniques.values())) == 4:
                    level += 1
            # 3 uniques vs. 2 pairs
            elif level == 4 and max(list(self.uniques.values())) == 3:
                    level += 1

            # Replacing the joker cards with value 1
            self.cards = real_cards

            level = (level)*(14**5)
            real_cards.reverse()
            for i,card in enumerate(real_cards):
                level += (card-1)*(14**i)

        else: # Special case where all cards are jokers
            level = 8*(14**5)
        return level

    # Turns the string list of cards into integer list
    # Returns the indeces of jokers (if mode is set to allow jokers)
    def determine_cards(self, hand, mode):
         joker_indexes = []
         for i,card in enumerate(hand):
            value = self.get_card_value(card, mode)
            if value != 1: 
                self.cards.append(value)
            else: 
                joker_indexes.append(i)
                continue

            if self.cards[-1] not in self.uniques:
                self.uniques[self.cards[-1]] = 1
            else: self.uniques[self.cards[-1]] += 1
         return joker_indexes

    # Get card value from string
    # Treatment of "J" depends on the mode
    def get_card_value(self, str_card, mode):
        if str_card == "A": return 14
        if str_card == "K": return 13
        if str_card == "Q": return 12
        if str_card == "J": 
            if mode: return 1
            else: return 11
        if str_card == "T": return 10
        return int(str_card)

if __name__ == "__main__":
    main()