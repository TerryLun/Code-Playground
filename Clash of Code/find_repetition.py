def find_rep(inp_string, tar_string):
    tar_length = len(tar_string)
    count = 0
    while len(inp_string) >= tar_length:
        if inp_string[:tar_length] == tar_string:
            count += 1
            inp_string = inp_string[tar_length:]
        else:
            return False
    if len(inp_string) and tar_string[:len(inp_string)] != inp_string:
        return False
    return count, len(inp_string), tar_length


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
