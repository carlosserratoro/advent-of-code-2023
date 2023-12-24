# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence


class DAG:
    def __init__(self):
        self._g = dict()

    def add_node(self, label):
        """Add a node having the given label."""
        if label not in self._g:
            self._g[label] = dict()

    def add_named_arc(self, label_from, label_to, arc_name):
        """Add a named arc to move from label_from to label_to."""
        self.add_node(label_from)
        self.add_node(label_to)
        self._g[label_from][arc_name] = label_to

    def get_destination_label(self, current_label, arc_name):
        """Get the label of the destination node."""
        return self._g[current_label][arc_name]

    @property
    def node_labels(self):
        for node_label in self._g:
            yield node_label
