# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_08.graph import DAG


def test_dag_only_nodes():
    g = DAG()
    g.add_node("a")
    g.add_node("b")
    assert g._g == {"a": dict(), "b": dict()}


def test_dag_add_edge_existing_nodes():
    g = DAG()
    g.add_node("a")
    g.add_node("b")
    g.add_named_arc("a", "b", "a->b")
    assert g._g == {"a": {"a->b": "b"}, "b": dict()}


def test_dag_add_edge_non_existing_nodes():
    g = DAG()
    g.add_named_arc("a", "b", "a->b")
    assert g._g == {"a": {"a->b": "b"}, "b": dict()}
