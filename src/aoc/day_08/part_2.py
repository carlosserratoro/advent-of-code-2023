# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import math
import os
from aoc.common import get_lines
from aoc.day_08.common import build_graph


def find_ending_loop_length(g, instructions, node_label):
    """Apply the instructions until an end loop is found, return its length.

    After inspecting the problem, it was found that after the
    instructions are applied a number of times, it arrives to
    an ending state, and this ending state starts a loop that
    repeats the path after the same number of instructions.

    In a first implementation, the path was returned, and its
    length was computed by the caller, but it was found that the
    path was so long that keeping the track of the traversed
    node made the memory to explode. Thus, just the length of the
    loop is returned.
    """
    len_loop = 0
    while True:
        for instruction in instructions:
            node_label = g.get_destination_label(node_label, instruction)
            len_loop += 1
        loop_found = node_label.endswith("Z")
        if loop_found:
            return len_loop


def get_num_steps_simultaneous(lines):
    g, instructions = build_graph(lines)

    # Traverse the graph from all starting points '??A'.
    starting_node_labels = [label for label in g.node_labels if label.endswith("A")]

    # For each starting node, get the moment in which we arrive to an end
    # node, that for the particular case of this problem means a loop starts.
    # So the moment in which we'll arrive simultaneously to an end state for
    # all the possible paths is the least common multiple of all the loop
    # lengths.
    #
    # Note that: this was an assumption based on the detailed inspection of
    #            the first path found, from which the generalisation to the
    #            other paths was made. The result obtained was approved by
    #            Advent of Code so the assumption was correct --- but, this
    #            could not have been the case.
    loops_lengths = []
    for node_label in starting_node_labels:
        loops_lengths.append(find_ending_loop_length(g, instructions, node_label))
    return math.lcm(*loops_lengths)


if __name__ == "__main__":
    script_path = os.path.abspath(os.path.dirname(__file__))
    input_path = os.path.join(script_path, "inputs/parts_1_2.txt")
    print("Day 08, Part 2:", get_num_steps_simultaneous(get_lines(input_path)))
