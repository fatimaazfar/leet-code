class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = str(x)[::-1]
        if rev == str(x):
            return True
        return False
        