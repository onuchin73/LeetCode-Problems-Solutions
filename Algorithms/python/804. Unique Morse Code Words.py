# Input: words = ["gin","zen","gig","msg"]
# Output: 2

from typing import List

morze: List[str] = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                    "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

words: List[str] = ["gin", "zen", "gig", "msg"]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        for w in words:
            t = ''
            for l in w:
                t += morze[ord(l) - ord('a')]
            s.add(t)

        return len(s)


print(Solution().uniqueMorseRepresentations(words))
