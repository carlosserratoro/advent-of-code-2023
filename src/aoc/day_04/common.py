# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import re

REGEX_NUMBERS_AND_PIPES = re.compile(r"(\||\d+)")


def parse_card(card):
    winning_numbers = set()
    our_numbers = set()

    card_number = None
    destination_set = winning_numbers
    for match_no, match in enumerate(REGEX_NUMBERS_AND_PIPES.finditer(card)):
        finding = match.group()
        if match_no == 0:
            card_number = int(finding)
        if match_no > 0:
            if finding == "|":
                # After the pipe we are going to get our numbers.
                destination_set = our_numbers
            else:
                destination_set.add(int(finding))
    return card_number, winning_numbers, our_numbers
