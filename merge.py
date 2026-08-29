# Merge Two Sorted Lists — O(n + m)
# As shown in the reel: https://www.facebook.com/reel/1014845534701563
# Generated from the episode; edits here are overwritten. See the README.

def merge(L, R):
    out = []
    while L and R:
        if L[0] <= R[0]:
            out.append(L.pop(0))
        else:
            out.append(R.pop(0))
    return out + L + R
