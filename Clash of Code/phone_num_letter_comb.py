"""
Back in day, people sent text messages using the number pad where each number was associated with 3-4 letters of the
alphabet. You could hit the same number repeatedly to cycle through each of its letters. Or you could just press each
number once and, in the end, the phone would guess what word you desired.

Today you will BE the phone and let's assume the user is using the latter method of input (1 number per letter). Given a
string of numbers, output all possible letter combinations in alphabetical order.

Here are the letters associated with each number:
2 = abc
3 = def
4 = ghi
5 = jkl
6 = mno
7 = pqrs
8 = tuv
9 = wxyz

Input
Line 1: A string S of digits to map
Output
All possible described outputs for S in alphabetical order.

Constraints
2 ≤ Length of S ≤ 9

test cases:

Input
5
Output
j
k
l

Input
23
Output
ad
ae
af
bd
be
bf
cd
ce
cf

Input
426
Output
gam
gan
gao
gbm
gbn
gbo
gcm
gcn
gco
ham
han
hao
hbm
hbn
hbo
hcm
hcn
hco
iam
ian
iao
ibm
ibn
ibo
icm
icn
ico

Input
6969
Output
mwmw
mwmx
mwmy
mwmz
mwnw
mwnx
mwny
mwnz
mwow
mwox
mwoy
mwoz
mxmw
mxmx
mxmy
mxmz
mxnw
mxnx
mxny
mxnz
mxow
mxox
mxoy
mxoz
mymw
mymx
mymy
mymz
mynw
mynx
myny
mynz
myow
myox
myoy
myoz
mzmw
mzmx
mzmy
mzmz
mznw
mznx
mzny
mznz
mzow
mzox
mzoy
mzoz
nwmw
nwmx
nwmy
nwmz
nwnw
nwnx
nwny
nwnz
nwow
nwox
nwoy
nwoz
nxmw
nxmx
nxmy
nxmz
nxnw
nxnx
nxny
nxnz
nxow
nxox
nxoy
nxoz
nymw
nymx
nymy
nymz
nynw
nynx
nyny
nynz
nyow
nyox
nyoy
nyoz
nzmw
nzmx
nzmy
nzmz
nznw
nznx
nzny
nznz
nzow
nzox
nzoy
nzoz
owmw
owmx
owmy
owmz
ownw
ownx
owny
ownz
owow
owox
owoy
owoz
oxmw
oxmx
oxmy
oxmz
oxnw
oxnx
oxny
oxnz
oxow
oxox
oxoy
oxoz
oymw
oymx
oymy
oymz
oynw
oynx
oyny
oynz
oyow
oyox
oyoy
oyoz
ozmw
ozmx
ozmy
ozmz
oznw
oznx
ozny
oznz
ozow
ozox
ozoy
ozoz
"""
import collections

d = {'2': 'abc',
     '3': 'def',
     '4': 'ghi',
     '5': 'jkl',
     '6': 'mno',
     '7': 'pqrs',
     '8': 'tuv',
     '9': 'wxyz'}
a = [d[i] for i in input()]
q = collections.deque()
for c in a[0]:
    q.append(c)
for s in a[1:]:
    temp = collections.deque()
    while q:
        temp.append(q.popleft())
    while temp:
        x = temp.popleft()
        for c in s:
            q.append(x + c)
for i in q:
    print(i)
