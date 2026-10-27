class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = "".join(sorted(s)), "".join(sorted(t))

        return countS == countT