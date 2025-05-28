class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: empty needle is always found at index 0
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        # If needle longer than haystack, it can't be found
        if m > n:
            return -1
        
        # Slide a window of length m over haystack
        for i in range(n - m + 1):
            # Compare substring; slicing cost is O(m)
            if haystack[i:i+m] == needle:
                return i
        
        return -1
