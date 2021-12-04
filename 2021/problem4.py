import numpy as np


class BingoCard:
    def __init__(self, card_matrix):
        self.card = []
        self.bingo = False
        for line in card_matrix:
            line = [int(i.strip()) for i in line.strip().replace("  ", " ").split(" ")]
            self.card.append(line)
        self.card = np.array(self.card)

    def call_numbers(self, numbers: list):
        self.card_bool = np.isin(self.card, numbers)
        return self.card_bool

    def check_bingo(self):
        if np.any(np.all(self.card_bool, axis=1)):
            self.bingo = True
        elif np.any(np.all(self.card_bool, axis=0)):
            self.bingo = True


with open("input_problem4", "r") as file:
    input_data = file.read().split("\n\n")

number_calls = [int(i) for i in input_data[0].split(",")]
bingo_cards_input = input_data[1:]

bingo_cards_unplayed = []

for card_input_raw in bingo_cards_input:
    card_input = card_input_raw.split("\n")
    bingo_cards_unplayed.append(BingoCard(card_input))

bingo_cards = bingo_cards_unplayed

for i, number in enumerate(number_calls):
    for bingo_card in bingo_cards:
        bingo_card.call_numbers(number_calls[:i+1])
        bingo_card.check_bingo()
        if bingo_card.bingo:
            print(f"We have bingo!")
            winning_card = bingo_card
            break
    else:
        continue
    break

not_called = winning_card.card[np.where(winning_card.card_bool, False, True)]
answer1 = number * sum(not_called)

print(f"Answer to problem 4 part 1: {answer1}")

# Part 2
not_winning_cards = bingo_cards_unplayed
for i, number in enumerate(number_calls):

    for j, bingo_card in enumerate(not_winning_cards):
        bingo_card.call_numbers(number_calls[:i+1])
        bingo_card.check_bingo()
        if len(not_winning_cards) != 1:
            if bingo_card.bingo:
                del not_winning_cards[j]
        else:
            if bingo_card.bingo:
                break
            else:
                continue
    else:
        continue
    break

last_winning_card = not_winning_cards[0]
not_called = last_winning_card.card[np.where(last_winning_card.card_bool, False, True)]
answer2 = number * sum(not_called)

print(f"Answer to problem 4 part 2: {answer2}")
