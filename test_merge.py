"""
Run it: python3 test_merge.py   (or: pytest)
"""

from main import LEFT, RIGHT, comparisons
from merge import merge


def test_it_merges_into_sorted_order():
    assert merge(list(LEFT), list(RIGHT)) == sorted(LEFT + RIGHT)


def test_the_leftovers_cost_no_comparisons():
    # The claim the episode is about. Once one side empties, the other is already sorted
    # AND already larger than everything taken, so there is nothing left to decide.
    assert comparisons(LEFT, RIGHT) < len(LEFT) + len(RIGHT)


def test_two_runs_that_do_not_interleave_cost_the_shorter_run():
    # The extreme case: the whole of the second run rides along for free.
    assert comparisons([1, 2, 3], [7, 8, 9]) == 3


def test_it_consumes_exactly_one_of_its_arguments():
    # `L.pop(0)` mutates. That is fine inside merge sort, where the halves are scratch,
    # and a trap anywhere else — so it is pinned down rather than left to be discovered.
    l, r = list(LEFT), list(RIGHT)
    out = merge(l, r)
    assert (l == []) != (r == []), 'exactly one side should be drained'
    leftover = l or r
    assert leftover == out[len(out) - len(leftover):]
    assert leftover == sorted(leftover)


def test_it_is_stable():
    # `<=` rather than `<`: a tie takes from L first, and merge sort is built on that.
    assert merge([1], [1]) == [1, 1]


def test_edge_cases():
    for l, r in (([], []), ([], [1, 2]), ([1, 2], []), ([1, 1, 1], [1, 1]), (LEFT, RIGHT)):
        assert merge(list(l), list(r)) == sorted(l + r)


if __name__ == '__main__':
    passed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
            passed += 1
    print(f'\n{passed} tests passed\n')
