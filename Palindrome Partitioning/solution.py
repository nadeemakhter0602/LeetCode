class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, i, j):
            if i == j:
                return True
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def allPalindromes(i, partition, palindromes):
            if i >= len(s):
                palindromes.append(partition)
                return palindromes
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    allPalindromes(j + 1, partition + [s[i : j + 1]], palindromes)
            return palindromes

        return allPalindromes(0, [], [])
