from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        decreasing = deque()
        s = []
        for i in range(len(nums)):
            while len(decreasing) > 0 and decreasing[-1] < nums[i]:
                decreasing.pop()
            decreasing.append(nums[i])
            window.append(nums[i])
            if len(window) == k:
                if decreasing[0] == window[0]:
                    max_ = decreasing.popleft()
                    s.append(max_)
                else:
                    s.append(decreasing[0])
                window.popleft()
        return s