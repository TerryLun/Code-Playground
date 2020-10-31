"""
Alice and Bob are playing a game of Hangman wherein they each have a go at guessing the letters of a word or phrase
until they've revealed the entire thing. Unfortunately, they forgot to keep score during the round and now the rest of the alphabet has been concatenated onto the end of their strings of guesses. They're very competitive and need to know who won (and by how much).

Given the word or phrase they were trying to guess along with their respective guesses (plus all the unguessed letters),
determine which player revealed all the letters using the fewest attempts.

Notes: Alice always goes first, but thankfully Bob has selective amnesia and doesn't remember the solution when he gets
the same puzzle that Alice just solved. Some of the phrases contain non-alphabetical characters; these did not need to
be guessed by the players as they were revealed at the start of the game.


Input
CodinGame
ETAOINSHRDLUMGCBFJKPQVWXYZ
ETAOINSHRDLUGPMZCBFJKQVWXY

Output
Alice
2


Input
42: the meaning of life, the universe, and everything.
RSTLNEJAGFUXHKMDVIYOBCPQWZ
RSTLNEIGHAFMVDYOUBCJKPQWXZ

Output
Bob
3


Input
senselessness
ENSBLACDFGHIJKMOPQRTUVWXYZ
EVAUWNSLBCDFGHIJKMOPQRTXYZ

Output
Alice
3


Input
Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch
QBKFWRGZOCSJYADNIHEVTLPMUX
NAWORYLDPGBEHICFSTJKMQUVXZ

Output
Bob
5


Twelve plus one = eleven plus two.
TSLWOVQGNUEPABCDFHIJKMRXYZ
LETOVNSPUDWABCFGHIJKMQRXYZ

Output
Bob
1


Input
hajj
ALICEXSOGWNMBUQDRKYHPTVZJF
DISNEYCZLJKMVAGRTOXUFWHBPQ

Output
Bob
2
"""

inp = input().lower()
s = set()
for c in inp:
    if c.isalpha():
        s.add(c)
ia = input().lower()
ib = input().lower()
a = set()
b = set()
ac = bc = 1111


def validate(c, s, st):
    if c in s:
        st.add(c)
    return True if len(s) == len(st) else False


for i, (x, y) in enumerate(zip(ia, ib)):
    if validate(x, s, a):
        ac = min(ac, i)
    if validate(y, s, b):
        bc = min(bc, i)

print('Alice' if ac <= bc else 'Bob')
print(abs(ac - bc))
