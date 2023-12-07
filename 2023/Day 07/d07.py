class Hand():
    def __init__(self, hand, bid) -> None:
        self.cards = []
        self.uniques = {}
        self.bid = int(bid)
        self.hand_rank = 0
        self.joker_indexes = []
        for i,card in enumerate(hand):
            value = get_card_value(card)
            if value != -1: 
                self.cards.append(value)
            else: 
                self.joker_indexes.append(i)
                continue

            if self.cards[-1] not in self.uniques:
                self.uniques[self.cards[-1]] = 1
            else: self.uniques[self.cards[-1]] += 1

        if len(self.joker_indexes) < 5:

            #print(sorted_uniques)

            # joker logic
            sorted_uniques = sorted(self.uniques.items(), key=lambda x:x[1])
            real_cards = self.cards.copy()
            for i in self.joker_indexes:
                self.cards.insert(i,sorted_uniques[-1][0])
                self.uniques[sorted_uniques[-1][0]] += 1
                real_cards.insert(i,-1)
            
            self.hand_rank = 5 - len(list(self.uniques.values()))
            if self.hand_rank == 3 and max(list(self.uniques.values())) == 4:
                    self.hand_rank += 0.5
            elif self.hand_rank == 2 and max(list(self.uniques.values())) == 3:
                    self.hand_rank += 0.5

            self.cards = real_cards

        else: # all jokers
            self.cards = [-1,-1,-1,-1,-1]
            self.hand_rank = 4

#        print(self.hand_rank, self.cards)

        
        #print(self.cards, self.hand_rank)





def main():   
    fname = "./2023/Day 07/input.txt"
    file = open(fname, 'r')
    data = file.read().splitlines()
    hands = []
    for i,row in enumerate(data):
        #print(i)
        row = row.split()
        hands.append(Hand(row[0],row[1]))

    ranked_hands = []
    for hand in hands:
        added = False
        if len(ranked_hands) == 0:
            ranked_hands.append(hand)
        else:
            for i,hand_to_compare in enumerate(ranked_hands):
                if hand.hand_rank > hand_to_compare.hand_rank:
                    ranked_hands.insert(i, hand)
                    added = True
                elif hand.hand_rank == hand_to_compare.hand_rank:
                    for j in range(0,5):
                        if hand.cards[j] > hand_to_compare.cards[j]:
                            ranked_hands.insert(i, hand)
                            added = True
                            break
                        elif hand.cards[j] < hand_to_compare.cards[j]:
                            break
                if added == True:
                    break
            if added == False: ranked_hands.append(hand)
            

    total = 0
    for i,h in enumerate(ranked_hands):
        total += (len(ranked_hands)-i)*h.bid
        print(h.cards, h.hand_rank)

    print(total)



def get_card_value(str_card):
    if str_card == "A": return 14
    if str_card == "K": return 13
    if str_card == "Q": return 12
    if str_card == "J": return -1
    if str_card == "T": return 10
    else: return int(str_card)

if __name__ == "__main__":
    
    main()