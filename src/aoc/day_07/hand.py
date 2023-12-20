# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from collections import defaultdict
from aoc.day_07.hand_types import HandTypes
from aoc.day_07.card_strenghts import CARD_STRENGTHS, CARD_STRENGTHS_JOKER


class Hand:
    def __init__(self, hand, use_jokers=False):
        self._hand = hand
        self._use_jokers = use_jokers

        self._cards = defaultdict(lambda: 0)
        for card in hand:
            self._cards[card] += 1

        # Accessed through the property hand_type.
        self._hand_type = None

        # Accessed through the property strength.
        self._strength = None

    def _apply_jokers(self):
        """Apply the jokers to promote the hand to the strongest type possible."""
        num_jokers = self._cards.get("J", 0)

        # If we have all jokers, then we have a special case. For the purpose
        # of the cards that we store in `_cards`, we don't care which one we
        # have, so we can leave them as they are, as long as they all are equal.
        if num_jokers != 5:
            for _ in range(num_jokers):
                max_card = [
                    k
                    for (k, v) in sorted(
                        self._cards.items(), key=lambda i: i[1], reverse=True
                    )
                    if k != "J"
                ][0]
                self._cards["J"] -= 1
                self._cards[max_card] += 1
            self._cards.pop("J", None)

    @property
    def hand_type(self):
        if not self._hand_type:
            if self._use_jokers:
                self._apply_jokers()

            values = tuple(sorted(self._cards.values()))
            if values == (5,):
                self._hand_type = HandTypes.FIVE_OF_A_KIND
            elif values == (1, 4):
                self._hand_type = HandTypes.FOUR_OF_A_KIND
            elif values == (2, 3):
                self._hand_type = HandTypes.FULL_HOUSE
            elif values == (1, 1, 3):
                self._hand_type = HandTypes.THREE_OF_A_KIND
            elif values == (1, 2, 2):
                self._hand_type = HandTypes.TWO_PAIR
            elif values == (1, 1, 1, 2):
                self._hand_type = HandTypes.ONE_PAIR
            else:
                self._hand_type = HandTypes.HIGH_CARD
        return self._hand_type

    @property
    def strength(self):
        if not self._strength:
            card_strengths = (
                CARD_STRENGTHS_JOKER if self._use_jokers else CARD_STRENGTHS
            )
            base = len(card_strengths)
            self._strength = 0
            for card_no, card in enumerate(reversed(self._hand)):
                self._strength += base**card_no * card_strengths[card]
        return self._strength

    def __lt__(self, other):
        """Make this class sortable."""
        return (self.hand_type < other.hand_type) or (
            self.hand_type == other.hand_type and self.strength < other.strength
        )
