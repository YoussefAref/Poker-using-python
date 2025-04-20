from collections import Counter

RANKS = {'2': 2, '3':3, '4':4, '5':5, '6':6, '7':7,
         '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def parse_hand(raw):
    cards = []
    for token in raw:
        t = token.replace(' ', '')
        rank, suit = t[:-1], t[-1]
        cards.append((RANKS[rank], suit))
    return cards

def hand_score(raw_hand):
    hand = parse_hand(raw_hand)
    values = sorted([v for v, s in hand], reverse=True)
    suits = [s for v, s in hand]
    counts = Counter(values)
    is_flush = len(set(suits)) == 1
    uniq = sorted(set(values))
    is_wheel = uniq == [2,3,4,5,14]
    is_straight = (len(uniq)==5 and uniq[0] - uniq[-1] == 4) or is_wheel
    top_straight = 5 if is_wheel else max(uniq)

    freq = sorted(((cnt, val) for val, cnt in counts.items()), reverse=True)
    tiebreakers = []
    for cnt, val in freq:
        tiebreakers.extend([val]*cnt)

    if is_straight and is_flush:
        category = 8
        tiebreakers = [top_straight]
    elif freq[0][0] == 4:
        category = 7
    elif freq[0][0] == 3 and freq[1][0] == 2:
        category = 6
    elif is_flush:
        category = 5
    elif is_straight:
        category = 4
        tiebreakers = [top_straight]
    elif freq[0][0] == 3:
        category = 3
    elif freq[0][0] == 2 and freq[1][0] == 2:
        category = 2
    elif freq[0][0] == 2:
        category = 1
    else:
        category = 0

    return (category, *tiebreakers)

def compare_hands(hand1, hand2):
    score1 = hand_score(hand1)
    score2 = hand_score(hand2)
    if score1 > score2:
        return 1
    elif score1 < score2:
        return -1
    else:
        return 0
