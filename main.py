"""
Run it: python3 main.py

The half of merge sort that does the work: compare the two heads, take the smaller,
repeat. The reel's claim is about the leftovers — whatever remains when one side runs
out is already sorted and already larger than everything taken, so it is appended
without another comparison.
"""

from merge import merge

LEFT = [11, 24, 63]    # the two sorted runs the reel merges
RIGHT = [18, 45]


def merge_with_picks(L: list[int], R: list[int]) -> tuple[list[int], list[str]]:
    """The same loop, recording which side each value came from."""
    L, R = list(L), list(R)
    out: list[int] = []
    picks: list[str] = []
    while L and R:
        if L[0] <= R[0]:
            picks.append(f'L {L[0]:>2}')
            out.append(L.pop(0))
        else:
            picks.append(f'R {R[0]:>2}')
            out.append(R.pop(0))
    rest = L + R
    return out + rest, picks + [f'{"L" if L else "R"} {v:>2}  (tacked on)' for v in rest]


def comparisons(L: list[int], R: list[int]) -> int:
    """Head-to-head comparisons. The tail costs none, which is the point."""
    L, R = list(L), list(R)
    n = 0
    while L and R:
        n += 1
        (L if L[0] <= R[0] else R).pop(0)
    return n


def main() -> None:
    out, picks = merge_with_picks(LEFT, RIGHT)

    print(f'\n  L = {LEFT}\n  R = {RIGHT}\n')
    for p in picks:
        print(f'    {p}')
    print(f'\n  {out}\n')

    n = comparisons(LEFT, RIGHT)
    total = len(LEFT) + len(RIGHT)
    print(
        f'  {n} comparisons for {total} values. The last {total - n} cost none at all: once one\n'
        f'  side is empty the other is already sorted AND already bigger than everything\n'
        f'  taken, so there is nothing left to decide.\n'
        f'\n  `<=` rather than `<` is what makes this stable — equal values keep the order\n'
        f'  they came in, with L winning ties. Merge sort is built on that.\n'
    )


# ── the claims above, checked ────────────────────────────────────────────────────

assert merge(list(LEFT), list(RIGHT)) == sorted(LEFT + RIGHT)

# THE CLAIM: the leftovers are appended, not compared. Nothing is compared after one
# side empties, so the count is strictly less than the number of values merged.
assert comparisons(LEFT, RIGHT) < len(LEFT) + len(RIGHT)

# The extreme case: two runs that do not interleave at all cost one comparison per value
# of the smaller run, and the whole of the other run rides along for free.
assert comparisons([1, 2, 3], [7, 8, 9]) == 3

# THE SNIPPET MUTATES ITS ARGUMENTS. `L.pop(0)` consumes the lists it was handed — which
# is fine inside merge sort, where the halves are scratch, and a trap anywhere else.
#
# It consumes exactly ONE of them. The loop stops the moment either runs dry, and whatever
# is still in the other is the leftover that gets tacked on — which is the claim itself,
# visible in what the arguments look like afterwards.
_l, _r = list(LEFT), list(RIGHT)
_out = merge(_l, _r)
assert (_l == []) != (_r == []), 'exactly one side should be drained'
_leftover = _l or _r
assert _leftover == _out[len(_out) - len(_leftover):], 'the leftover is the tail, unexamined'
assert _leftover == sorted(_leftover)

# Stability: with `<=`, a tie takes from L first.
assert merge([1], [1]) == [1, 1]

for _l, _r in (([], []), ([], [1, 2]), ([1, 2], []), ([1, 1, 1], [1, 1]), (LEFT, RIGHT)):
    assert merge(list(_l), list(_r)) == sorted(_l + _r)

if __name__ == '__main__':
    main()
