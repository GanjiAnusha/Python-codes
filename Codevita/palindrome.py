class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                a = s[i:j+1]
                if a == a[::-1]:
                    ans += 1
        return ans