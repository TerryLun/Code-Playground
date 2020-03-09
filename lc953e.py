"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
given words are sorted lexicographicaly in this alien language.
"""


def isAlienSorted(words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """
    # alien_dict = {k: v for v, k in enumerate(order, 1)}
    # alien_dict[' '] = 0
    # longest = 0
    # for w in words:
    #     longest = max(longest, len(w))
    # for i in range(len(words)):
    #     words[i] = words[i].ljust(longest)
    # for i in range(len(words) - 1):
    #     word1 = words[i]
    #     word2 = words[i+1]
    #     for j in range(len(word1)):
    #         if alien_dict[word1[j]] > alien_dict[word2[j]]:
    #             return False
    #         elif alien_dict[word1[j]] < alien_dict[word2[j]]:
    #             break
    # return True
    order_index = {c: i for i, c in enumerate(order)}

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        # Find the first difference word1[k] != word2[k].
        for k in range(min(len(word1), len(word2))):
            # If they compare badly, it's not sorted.
            if word1[k] != word2[k]:
                if order_index[word1[k]] > order_index[word2[k]]:
                    return False
                break
        else:
            # If we didn't find a first difference, the
            # words are like ("app", "apple").
            if len(word1) > len(word2):
                return False

    return True


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order) is True)

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order) is False)

words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order) is False)

words = ["", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order) is True)

words = ["app", ""]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order) is False)

words = [""]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order) is True)
