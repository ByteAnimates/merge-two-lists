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



if __name__ == '__main__':
    main()
