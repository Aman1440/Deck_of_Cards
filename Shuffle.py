#program to shuffle a deck of cards
import itertools, random

deck = list(itertools.product(range(1,14), ["spade","heart","Diamond","club"]))

random.shuffle(deck)

print("your combination of cards is :")
for i in range(5):
  print(deck[i][0],"of", deck[i][1])
