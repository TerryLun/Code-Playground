def find_rep(s, t):
    t_len = len(t)
    count = 0
    while len(s) >= t_len:
        if s[:t_len] == t:
            count += 1
            s = s[t_len:]
        else:
            return False
    if len(s) and t[:len(s)] != s:
        return False
    return count, len(s), t_len


s = input()
i = 1
max_rep = 0
max_ls = ''
max_lt = ''
target = ''
while i < len(s):
    t = s[:i]
    if find_rep(s, t):
        c, ls, lt = find_rep(s, t)
        if c > max_rep:
            max_rep = c
            max_ls = ls
            max_lt = lt
            target = t
    i += 1
if max_ls:
    print(target + '*' + '(' + str(max_rep) + '+' + str(max_ls) + '/' + str(max_lt) + ')')
elif target:
    print(target + '*' + str(max_rep))
else:
    print(s + '*1')

"""
input:
hellohellohel
exp ouput:
hello*(2+3/5)

input:
aaaaaaaaaaaaaaa
exp ouput:
a*15

input:
aaaaarg
exp ouput:
aaaaarg*1

input:
abcdabcdabcdab
exp ouput:
abcd*(3+2/4)

input:
fuuuuuuuuuuuuuufuuuuuuu
exp ouput:
fuuuuuuuuuuuuuu*(1+8/15)

input:
lollolpwnzlollolpwnzlollolpwnzcraplollolpwnzlollolpwnzlollolpwnzcraplollolpwnzlollolpwnzlollolpwnzcraplollolpwnzlollolpwnzlollolpwnzcraplollolpwnzlollolpwnzlollolpwnzcraplollolpwnz
exp ouput:
lollolpwnzlollolpwnzlollolpwnzcrap*(5+10/34)
"""
