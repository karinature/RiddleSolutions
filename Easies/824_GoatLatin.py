#
#   Date - 24.05.2022
#
#
# 824. Goat Latin
# Easy
#
# You are given a string sentence that consist of words separated by spaces.
# Each word consists of lowercase and uppercase letters only.
#
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
# The rules of Goat Latin are as follows:
#
#     If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
#         For example, the word "apple" becomes "applema".
#     If a word begins with a consonant (i.e., not a vowel),
#       remove the first letter and append it to the end, then add "ma".
#         For example, the word "goat" becomes "oatgma".
#     Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#         For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
#
# Return the final sentence representing the conversion from sentence to Goat Latin.
#
#
#
# Example 1:
#
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#
# Example 2:
#
# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
#
#
#
# Constraints:
#
#     1 <= sentence.length <= 150
#     sentence consists of English letters and spaces.
#     sentence has no leading or trailing spaces.
#     All the words in sentence are separated by a single space.
#
#
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
# from collections import defaultdict
import collections


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # res = []
        # for i, word in enumerate(sentence.split()):
        #     if word[0] in 'aeiouAEIOU':
        #         res.append(word + 'ma')
        #     else:
        #         res.append(word[1:] + word[0] + 'ma')
        #     res[-1]+='a'*(i+1)
        # return ' '.join(res)

        return ' '.join(
            word + 'ma' + 'a' * (i + 1) if word[0] in 'aeiouAEIOU'
            else word[1:] + word[0] + 'ma' + 'a' * (i + 1)
            for i, word in enumerate(sentence.split())
        )


def testing():
    sol = Solution()

    # result = sol.toGoatLatin(sentence="I speak Goat Latin")
    # # print(f"result: {result}")
    # assert ("Imaa peaksmaaa oatGmaaaa atinLmaaaaa" == result)
    #
    # result = sol.toGoatLatin(sentence="The quick brown fox jumped over the lazy dog")
    # # print(f"result: {result}")
    # assert (
    #         "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa" == result)

    result = sol.toGoatLatin(sentence="Each word consists of lowercase and uppercase letters only")
    # print(f"result: {result}")
    assert (
            "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa" == result)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
