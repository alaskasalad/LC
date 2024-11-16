class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
       
        while (left < right):
            cur = s[left]
            s[left] = s[right]
            s[right] = cur
            left += 1
            right -= 1
