from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        decreasing = deque()
        s = []
        for i in range(len(nums)):
            while len(decreasing) > 0 and decreasing[-1] < nums[i]:
                decreasing.pop()
            decreasing.append(nums[i])
            if i - k + 1 >= 0:
                if decreasing[0] == nums[i - k + 1]:
                    max_ = decreasing.popleft()
                    s.append(max_)
                else:
                    s.append(decreasing[0])
        return s