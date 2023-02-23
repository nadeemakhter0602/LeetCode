class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)
        l = 0
        r = m - 1
        while(True):
            i = (l+r)//2
            j = (m+n)//2 - i - 2
            aleft = nums1[i] if i>=0 else float('-inf')
            aright = nums1[i+1] if i+1<m else float('inf')
            bleft = nums2[j] if j>=0 else float('-inf')
            bright = nums2[j+1] if j+1<n else float('inf')
            if aleft<=bright and bleft<=aright:
                if (m+n)%2==0:
                    return (max(aleft,bleft)+min(aright,bright))/2
                else:
                    return min(aright,bright)
            elif aleft>bright:
                r = i-1
            else:
                l = i+1