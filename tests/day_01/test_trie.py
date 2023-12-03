# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_01.trie import Trie


def test_trie():
    trie = Trie()
    trie["a"] = 1
    trie["ab"] = 2
    trie["ac"] = 3

    assert trie.feed("a") is True
    assert trie.len_feed == 1
    assert trie.last_value == 1

    assert trie.feed("b") is True
    assert trie.len_feed == 2
    assert trie.last_value == 2

    assert trie.feed("b") is False
    assert trie.len_feed == 3
    assert trie.last_value == 2

    trie.starve()
    assert trie.len_feed == 0
    assert trie.last_value is None

    assert trie.feed("x") is False
    assert trie.len_feed == 1
    assert trie.last_value is None
    trie.starve()

    assert trie.feed("a") is True
    assert trie.len_feed == 1
    assert trie.last_value == 1

    assert trie.feed("c") is True
    assert trie.len_feed == 2
    assert trie.last_value == 3

    assert trie.feed("d") is False
    assert trie.len_feed == 3
    assert trie.last_value == 3
