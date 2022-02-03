# deck = input().split()
# number_of_shuffles = int(input())
#
# left_half = []
# right_half = []
#
# for shuffles in range(number_of_shuffles):
#     current_deck = []
#     half = int(len(deck)/2)
#     left_half = deck[0:half]
#     right_half = deck[half::]
#     for index_of_card in range(len(left_half)):
#         current_deck.append(left_half[index_of_card])
#         current_deck.append(right_half[index_of_card])
#     deck = current_deck
# print(deck)

card_deck = input()
shuffles = int(input())
shuffled_deck = card_deck.split(" ")
for i in range(shuffles):
    deck_1 = shuffled_deck[:len(shuffled_deck) // 2]
    deck_2 = shuffled_deck[len(shuffled_deck) // 2:]
    shuffled_deck = [cards for cards in zip(deck_1, deck_2) for cards in cards]
print(shuffled_deck)