# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import os
from aoc.common import get_lines
from aoc.day_08.common import build_graph


def get_num_steps(lines):
    g, instructions = build_graph(lines)

    # Traverse the graph from 'AAA' till we arrive to 'ZZZ'
    # following the instructions.
    num_steps = 0
    node_label = "AAA"
    while node_label != "ZZZ":
        for instruction in instructions:
            node_label = g.get_destination_label(node_label, instruction)
            num_steps += 1
    return num_steps


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 08, Part 1:", get_num_steps(get_lines(input_path)))
