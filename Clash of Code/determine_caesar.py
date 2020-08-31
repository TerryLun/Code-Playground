"""
golf: determine if the first word is caesar encrypted from the second
"""

print('false'if len({(ord(c)-ord(d))%26for c,d in zip(input(),input())})-1else'true')