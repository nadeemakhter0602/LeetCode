class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            n = len(s)
            if n == 1:
                return True
            for i in range(n // 2):
                if s[i] != s[n - i - 1]:
                    return False
            return True

        def allPalindromes(s, partition, palindromes):
            if not s:
                palindromes.append(partition)
            for idx in range(len(s)):
                if isPalindrome(s[: idx + 1]):
                    allPalindromes(
                        s[idx + 1 :], partition + [s[: idx + 1]], palindromes
                    )
            return palindromes

        return allPalindromes(s, [], [])
