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
                real_cards.insert(i,-1)
            
            # Determining the level of the hand
            # Level 4 = "5 uniques", ..., Level 0 = "high card"
            level = 5 - len(list(self.uniques.values()))
            
            # 4 uniques vs. full house
            if level == 3 and max(list(self.uniques.values())) == 4:
                    level += 0.5
            # 3 uniques vs. 2 pairs
            elif level == 2 and max(list(self.uniques.values())) == 3:
                    level += 0.5

            # Replacing the joker cards with value -1
            self.cards = real_cards

        else: # Special case where all cards are jokers
            self.cards = [-1,-1,-1,-1,-1]
            level = 4

        return level

    # Turns the string list of cards into integer list
    # Returns the indeces of jokers (if mode is set to allow jokers)
    def determine_cards(self, hand, mode):
         joker_indexes = []
         for i,card in enumerate(hand):
            value = self.get_card_value(card, mode)
            if value != -1: 
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
            if mode: return -1
            else: return 11
        if str_card == "T": return 10
        return int(str_card)