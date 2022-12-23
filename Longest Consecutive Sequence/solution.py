class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        longest = 0
        for i in nums:
            length = 1
            if i-1 not in l:
                while i+length in l:
                    length += 1
            longest = max(length, longest)
        return longest