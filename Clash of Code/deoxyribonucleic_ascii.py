"""
Given a string of N DNA bases (A, C, G, or T) representing the upper left "quadrant" of a double helix, display the full
sequence as pretty ASCII art.

As an example, the input "GATTACA" must result in the following:

 GC
A--T
T---A
T----A
 A----T
  C---G
   A--T
    TA
    CG
   A--T
  T---A
 T----A
A----T
G---C

Bear in mind that A and C always pair with T and G, respectively and vice versa, and that the right "strand" encodes the
same information as the left but in reverse.


Input
8
GTTAAGTC

Output
 GC
T--A
T---A
A----T
 A----T
  G---C
   T--A
    CG
    CG
   T--A
  G---C
 A----T
A----T
T---A
T--A
 GC


Input
16
TCGAAGCACCGTAGCG

Output
 TA
C--G
G---C
A----T
 A----T
  G---C
   C--G
    AT
    GC
   G--C
  C---G
 A----T
T----A
C---G
G--C
 CG
 CG
G--C
C---G
T----A
 A----T
  C---G
   G--C
    GC
    AT
   C--G
  G---C
 A----T
A----T
G---C
C--G
 TA
"""

n = int(input())
s = input()
s += s[::-1]
cd = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
sd = '1000123443210001'
dd = '0234432002344320'
for i in range(2 * n):
    print(' ' * int(sd[i % 16]) + s[i] + '-' * int(dd[i % 16]) + cd[s[i]])
