def compare(l1,l2):
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            return True
        elif l1[i] < l2[i]:
            return False
    return False
def card(p_cards):
    if bool(True) in royal_flush(p_cards):
        return 10, royal_flush(p_cards)[1]
    elif bool(True) in straight_flush(p_cards):
        return 9, straight_flush(p_cards)[1]
    elif bool(True) in four_of_a_kind(p_cards):
        return 8, four_of_a_kind(p_cards)[1]
    elif bool(True) in full_house(p_cards):
        return 7, full_house(p_cards)[1]
    elif bool(True) in flush(p_cards):
        return 6, flush(p_cards)[1]
    elif bool(True) in straight(p_cards):
        return 5, straight(p_cards)[1]
    elif bool(True) in three_of_a_kind(p_cards):
        return 4, three_of_a_kind(p_cards)[1]
    elif bool(True) in two_pairs(p_cards):
        return 3, two_pairs(p_cards)[1]
    elif bool(True) in one_pair(p_cards):
        return 2, one_pair(p_cards)[1]
    else:
        return 1, high_card(p_cards)
def royal_flush(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    if straight_flush(p_cards)[0] and p[0] == 14:
        return True, None
    return False, None
def straight_flush(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    if straight(p_cards)[0] and flush(p_cards)[0]:
        return True, p[0]
    return False, None
def four_of_a_kind(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    if p.count(p[1]) == 4:
        for num in p:
            if p.count(num) == 4:
                p.pop(p.index(num))
                p.pop(p.index(num))
                p.pop(p.index(num))
                p.insert(0, p.pop(p.index(num)))
        return True, p
    return False, None
def full_house(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    if p.count(p[0]) == 2 and p.count(p[-1]) == 3 or p.count(p[0]) == 3 and p.count(p[-1]) == 2:
        for num in p:
            if p.count(num) == 3:
                p.pop(p.index(num))
                p.pop(p.index(num))
                p.insert(0, p.pop(p.index(num)))
            elif p.count(num) == 2:
                p.pop(p.index(num))
                p.insert(1, p.pop(p.index(num)))
        return True, p
    return False, None
def flush(p_cards):
    color = [card[-1] for card in p_cards]
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    if color.count(color[0]) == 5:
        return True, p
    return False, None
def straight(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]])
    if p in [[2, 3, 4, 5, 14],[2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10], [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [9, 10, 11, 12, 13], [10, 11, 12, 13, 14]]:
        return True, p[-1]
    return False, None
def three_of_a_kind(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    if p.count(p[2]) == 3:
        for num in p:
            if p.count(num) == 3:
                p.pop(p.index(num))
                p.pop(p.index(num))
                p.insert(0, p.pop(p.index(num)))
        return True, p
    return False, None
def two_pairs(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    if p.count(p[1]) == 2 and p.count(p[3]) == 2:
        for num in p:
            if p.count(num) == 2:
                p.pop(p.index(num))
                p.insert(0, p.pop(p.index(num)))
        p[:2] = sorted(p[:2], reverse=True)
        return True, p
    return False, None
def one_pair(p_cards):
    p = sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
    for i in range(4):
        if p.count(p[i]) == 2:
            p.remove(p[i])
            p.insert(0, p.pop(i))
            return True, p
    return False, None
def high_card(p_cards):
    return sorted([x.index(a)+2 for a in [card[0] for card in p_cards]], reverse=True)
x = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
count = 0
for line in open(r'C:\Users\Klacik\Desktop\Programing\Python\Project Euler\Text\p054_poker.txt').readlines():
    if line != ' ':
        round = line.split()
        p1 = sorted(round[:5])
        p2 = sorted(round[5:])
        if card(p1)[0] > card(p2)[0]:
            count += 1
        elif card(p1)[0] == card(p2)[0]:
            if compare(card(p1)[1], card(p2)[1]):
                count += 1

print('Answer:', count)
