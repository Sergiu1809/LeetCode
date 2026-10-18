TIME VS SPACE COMPLEXITY

Time = how the NUMBER OF OPERATIONS grows with input size
Space = how much EXTRA MEMORY grows with input size

The input itself does NOT count toward space.
Only what the algorithm allocates on top of it.

------------------------------------------------

List -> O(1) access by INDEX, O(n) search by VALUE
Hash -> O(1) access by VALUE (average case)

Mechanism: hash function maps key -> array slot.

Python:
    dict = hash table with key -> value
    set = hash table with keys only
Both: O(1) average insert / lookup / delete.

--------------------------------------------------

COMBINING COMPLEXITIES

Sequential steps ADD, then keep the dominant term.
O(n log n) + O(n log n) + O(n) = O(n log n)
Constants drop. Faster-growing term wins.

Nested steps MULTIPLY.
loop over n, doing O(log n) work inside = O(n log n)

Growth order (slowest to fastest):
O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)

COMMON COSTS
sorting O(n log n)
binary search O(log n)
single pass O(n)
hash lookup O(1) 

sorted(x) -> build a new list, O(n) space
x.sort() -> sorts in place, O(1) extra space
Strings are immutable: sorted() is the only option.

EDGE CASE REFLEX
Iterating one collection while indexing another?
Check the lengths first.

----------------------------------------------------

HASH MAP: VALUE -> INDEX

When you need to know WHERE, not HOW MANY,
Store the index as the value

TWO SUM SHAPE
    for each num:
        complement = target - num
        if complement in seen: return [seen[complement], i]
        seen[num] = i

Insert AFTER the check. The dict then holds only
elements already passed, so nothing pairs with itself

dict[key] ->KeyError if missing
dict.get(key) -> None if missing
key in dict -> safest membership test

FALSY TRAP
0, "", [], None are all False in an 'if'
With indices as values, index 0 is falsy, so
'if seen.get(x):'silently fails on the first element.
Use 'in' for presence, not truthiness.