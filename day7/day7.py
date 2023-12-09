from collections import Counter

with open("day7/day7.txt", "r", encoding="utf-8") as file:
    input = file.readlines()


class Hand:
    counter = Counter()

    def __init__(self, hand: str, bid: str, joker: bool = False) -> None:
        self.joker = joker
        self.bid = int(bid)

        self.hand_num = [self.num_val(char) for char in hand]
        self.type = self.get_type(hand)

    def get_type(self, hand: str) -> int:
        self.counter.clear()
        self.counter.update(hand)

        diff = len(self.counter)
        most_com = self.counter.most_common(1)[0][1]

        if self.joker and "J" in hand and hand != "JJJJJ":
            diff -= 1

            j_num = self.counter["J"]
            if j_num == most_com:
                most_com += self.counter.most_common(2)[1][1]
            else:
                most_com += j_num

        if diff == 5:  # high card
            return 0
        elif diff == 4:  # one pair
            return 1
        elif diff == 3:
            if most_com == 2:  # two pairs
                return 2
            else:  # three of kind
                return 3
        elif diff == 2:
            if most_com == 3:  # full house
                return 4
            else:  # four of kind
                return 5
        else:  # five of kind
            return 6

    def num_val(self, char: str) -> int:
        if char.isdigit():
            return int(char)

        if self.joker:
            j_val = 0
        else:
            j_val = 11

        return {"A": 14, "K": 13, "Q": 12, "J": j_val, "T": 10}[char]

    def __gt__(self, other):
        if other.type != self.type:
            return self.type > other.type

        return self.hand_num > other.hand_num


def one():
    hands = [Hand(hand, bid) for hand, bid in [line.split() for line in input]]
    hands.sort()

    result = 0
    for i, hand in enumerate(hands):
        result += hand.bid * (i + 1)

    print(result)


def two():
    hands = [
        Hand(hand, bid, joker=True) for hand, bid in [line.split() for line in input]
    ]
    hands.sort()

    result = 0
    for i, hand in enumerate(hands):
        result += hand.bid * (i + 1)

    print(result)


one()
two()
