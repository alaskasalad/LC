class Sol:
    def findLen(self, nums, k):
        left = right = 0
        curr = 0
        ans = 0
        for left in range(len(k)):
            cur += nums[right]
            while (cur > k):
                cur -= nums[left]
                left += 1

            ans = max(ans, right - left +1)

        return ans


nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
a = Sol()

print(a.findLen(nums, k))
