class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers or positives ending in 0 (but not 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        # Reverse digits until we've processed at least half of them
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10

        # For even-length palindromes, x == reversed_half
        # For odd-length, the middle digit is extra in reversed_half, so reversed_half//10
        return x == reversed_half or x == reversed_half // 10
