class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create a frequency map for t
        tfreq = dict()
        for i in t:
            tfreq[i] = 1 + tfreq.get(i, 0)
        window = dict()
        left = 0
        right = 0
        have = 0
        need = len(tfreq)
        min_len = float('inf')
        min_window = ""
        while right < len(s):
            window[s[right]] = 1 + window.get(s[right], 0)
            # check if we have what we need
            if s[right] in tfreq and tfreq[s[right]] == window[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left : right + 1]
                if s[left] in tfreq and tfreq[s[left]] == window[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1
            right += 1
        return min_window
