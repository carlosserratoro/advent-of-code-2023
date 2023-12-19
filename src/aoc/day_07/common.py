# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_07.hand import Hand


def get_total_wins(lines, use_jokers):
    plays = []
    for line in lines:
        cards, bid_str = line.split(" ")
        plays.append((Hand(cards, use_jokers=use_jokers), int(bid_str)))

    total_winnings = 0
    for play_no, play in enumerate(sorted(plays)):
        _, bid = play
        total_winnings += (play_no + 1) * bid
    return total_winnings
