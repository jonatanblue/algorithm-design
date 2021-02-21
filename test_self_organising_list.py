from self_organising_list import SelfOrganisingList


def test_overwrite_existing_key():
    sol = SelfOrganisingList(initial_items=[("a", 100), ("b", 200), ("c", 299)])
    sol.write("c", 300)
    assert sol.items == [("c", 300), ("a", 100), ("b", 200)]


def test_write():
    sol = SelfOrganisingList(initial_items=[("a", 100), ("b", 200), ("c", 300)])
    sol.write("d", 400)
    assert sol.items == [("d", 400), ("a", 100), ("b", 200), ("c", 300)]


def test_read():
    sol = SelfOrganisingList(initial_items=[("a", 100), ("b", 200), ("c", 300)])
    assert sol.read("b") == 200
    assert sol.items == [("b", 200), ("a", 100), ("c", 300)]


def test_read_not_found():
    sol = SelfOrganisingList(initial_items=[("a", 100), ("b", 200), ("c", 300)])
    assert sol.read("d") is None
    assert sol.items == [("a", 100), ("b", 200), ("c", 300)]


def test_move_to_top():
    sol = SelfOrganisingList(initial_items=[("a", 100), ("b", 200), ("c", 300)])
    assert sol.move_to_top("b") == ("b", 200)
    assert sol.items == [("b", 200), ("a", 100), ("c", 300)]
