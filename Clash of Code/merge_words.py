a = input().split()
r = a[0]
for s in a[1:]:
    i = len(s)
    while i >= 0:
        if s[:i].lower() == r[-i:].lower():
            r = r[:-i] + s
            break
        i -= 1
    if i == -1:
        r += ' ' + s
print(r)

"""
inp: how are you?
exp: how are you?

inp: What the fuck!
exp: Whathe fuck!

inp: kayak KAYAK yakuzA
exp: KAyakuzA

inp: Coding Game
exp: CodinGame
"""
