# Merge Two Sorted Lists

**O(n + m)** · [Watch the reel](https://www.facebook.com/reel/1014845534701563)

The working code from the [@ByteAnimates](https://www.facebook.com/ByteAnimates) reel.

```bash
python3 merge.py
python3 main.py
```

No dependencies. Python 3.9+.

### `merge.py`

```python
def merge(L, R):
    out = []
    while L and R:
        if L[0] <= R[0]:
            out.append(L.pop(0))
        else:
            out.append(R.pop(0))
    return out + L + R
```

### Files

| | |
| --- | --- |
| `main.py` | run this — the demo, with real inputs and the claims asserted |
| `merge.py` | the reel snippet, generated from the episode |

---

The snippet above is generated from the video itself — what you read is byte-for-byte
what was typed on screen. A fix to it belongs in the episode, so open an issue and the
next reel carries it. Everything else here is hand-written and welcome as a pull request.
