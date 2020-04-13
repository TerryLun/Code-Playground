"""
500. Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American
keyboard like the image below.

Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""


def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # r1 = set('qwertyuiop')
    # r2 = set('asdfghjkl')
    # r3 = set('zxcvbnm')
    # lss = [r1, r2, r3]
    # r = []
    # result = []
    # for i in range(len(words)):
    #     okay = True
    #     w = words[i].lower()
    #     for ls in lss:
    #         if w[0] in ls:
    #             r = ls
    #             break
    #     for c in w:
    #         if c not in r:
    #             okay = False
    #             break
    #     if okay:
    #         result.append(words[i])
    # return result

    # clean
    rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
    result = []
    for w in words:
        lw = set(w.lower())
        for row in rows:
            if lw & row == lw:
                result.append(w)
    return result


inp = ["Hello", "Alaska", "Dad", "Peace"]
exp = ["Alaska", "Dad"]
print(findWords(inp) == exp)
