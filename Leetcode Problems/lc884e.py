"""
884. Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of
lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.
"""


def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    count = {}
    result = []
    words = A.split(' ') + B.split(' ')
    for w in words:
        if w in count.keys():
            count[w] += 1
        else:
            count[w] = 1
    for k, v in count.items():
        if v == 1:
            result.append(k)
    return result


A = "this apple is sweet"
B = "this apple is sour"
exp = ["sweet", "sour"]
print(uncommonFromSentences(A, B) == exp)

A = "apple apple"
B = "banana"
exp = ["banana"]
print(uncommonFromSentences(A, B) == exp)
