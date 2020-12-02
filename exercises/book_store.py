"""
The general idea for my solution is as followed:
1. Create a piles of books with max length = max number of unique
2. calculate the price of the piles
3. start transferring book from one pile to another and calculate price again
4. compare and decide the smallest basket price
"""
from collections import Counter
from itertools import combinations


# price is in cent instead of dollars
price = 800
discount = {
    1: 0,
    2: 0.05,
    3: 0.10,
    4: 0.20,
    5: 0.25
}


# we only care about size of piles not what in the piles
def create_piles(basket):
    piles = []
    max_dup = max(list(Counter(basket).values()))
    while max_dup > 1:
        # number of duplicates
        pile = list(set(basket))
        piles.append(pile)
        # remove the items from group from basket
        basket = list((Counter(basket) - Counter(pile)).elements())
        max_dup = max(list(Counter(basket).values()))

    piles.append(basket)
    return [len(pile) for pile in piles]


def piles_total_cost(piles, book_price=price):
    piles_total = [pile * book_price * (1-discount[pile]) for pile in piles]
    return sum(piles_total)


def total(basket):
    if not basket:
        return 0
    elif len(basket) == 1:
        return price
    piles = create_piles(basket)
    dif = max(piles) - min(piles)
    min_total = piles_total_cost(piles)
    while dif > 1:
        piles[0] -= 1
        piles[-1] += 1
        dif = max(piles) - min(piles)
        piles = sorted(piles, reverse=True)

        new_total = piles_total_cost(piles)
        if new_total < min_total:
            min_total = new_total
    return min_total


b = [1, 1, 2, 2, 3, 3, 4, 5]
print(create_piles(b))
print(piles_total_cost(create_piles(b)))
print(total(b))



