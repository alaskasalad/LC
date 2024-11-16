class Sol:
    def checkTarget(self, nums, target) -> bool:
        i = 0;
        j = len(nums)-1

        while (i < j):
            cur = nums[i] + nums[j]
            if (cur < target):
                i += 1
            elif (cur > target):
                j -= 1
            else:
                return True
        return False


nums = [1, 2, 4, 6, 8, 6, 14, 15]
target = 13

a = Sol()
print(a.checkTarget(nums, target))
