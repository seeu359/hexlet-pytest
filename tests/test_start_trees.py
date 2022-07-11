from hexlet_pytest.start_trees import remove_first_level


def test_remove_first_level():
    assert remove_first_level([]) == []
    assert remove_first_level([1, 100, 3]) == []
    assert remove_first_level([1, 2, [3, 5], [[4, 3], 2]]) == [3, 5, [4, 3], 2]
    assert remove_first_level([[5], 1, [3, 4]]) == [5, 3, 4]
    assert remove_first_level([
        [1, [3, 2]],
        2,
        [3, 5],
        2,
        [130, [1, [550, 10]]],
    ]) == [1, [3, 2], 3, 5, 130, [1, [550, 10]]]
