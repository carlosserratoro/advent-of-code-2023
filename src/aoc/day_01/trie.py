# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence


class Trie:
    """Trie

    The trie sets the keys by overriding existing keys
    with the new values set, so in the case of duplicated
    keys, the last value set is the one stored.

    Allows to search in a progressive way, by feeding one
    character at a time. So to search for the word `word`,
    the following calls must be done: `trie.feed('w')`,
    `trie.feed('o')`, `trie.feed('r')`, `trie.feed('d')`.
    """

    def __init__(self):
        self._data = dict()
        self._value = None

        # Internal cursor to keep track of the node in which we
        # are according to the feed provided.
        self._cursor = None

        # Stores the length of the feed.
        self.len_feed = 0

        # Stores the last value found while feeding the trie.
        self.last_value = None

    def __setitem__(self, key, value):
        """Add a new pair (key, value) to the trie."""
        self._add(key, value)

    def _add(self, key, value, key_idx=0):
        """Auxiliary method to add a new pair (key, value) to the trie."""
        if key_idx < len(key):
            c = key[key_idx]
            if c not in self._data:
                self._data[c] = Trie()
            self._data[c]._add(key, value, key_idx + 1)
        if key_idx == len(key) - 1:
            c = key[key_idx]
            self._data[c]._value = value

    def starve(self):
        """Reset any previous feeds."""
        self._cursor = None
        self.len_feed = 0
        self.last_value = None

    def feed(self, c):
        """Feed the trie with one character.

        If the character fed keeps advancing in the trie, return True;
        else, return False. If the character resulted in advancing
        to a node that has a value, it is stored in `last_value`.
        """
        self.len_feed += 1
        if self._cursor:
            self._cursor = self._cursor._data.get(c)
        elif self.len_feed == 1:
            self._cursor = self._data.get(c)
        if self._cursor:
            self.last_value = self._cursor._value
        return bool(self._cursor)
