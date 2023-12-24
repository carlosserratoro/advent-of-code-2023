# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

import re
from aoc.day_08.graph import DAG


REGEX_NODE_LINE = re.compile(r"(\w+)")


def parse_node_line(line):
    return REGEX_NODE_LINE.findall(line)


def build_graph(lines):
    """Build the graph from the input and get the traversal instructions."""
    instructions = ""
    g = DAG()
    for line_no, line in enumerate(lines):
        if line_no == 0:
            instructions = line
        elif line_no >= 2:
            node_current, node_left, node_right = parse_node_line(line)
            g.add_node(node_current)
            g.add_named_arc(node_current, node_left, "L")
            g.add_named_arc(node_current, node_right, "R")
    return g, instructions
