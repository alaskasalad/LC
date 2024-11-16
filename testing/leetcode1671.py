class Solution(object):
    def minimumMountainRemovals(self, nums):
        my_hashmap = {}
        # going forward 
        counter = 0 
        for i in range((len(nums) // 2)):
            print("nums[i]", nums[i], " nums[i+1]", nums[i+1])
            if nums[i] < nums[i+1]:
                my_hashmap[i] = nums[i]
            else:
                counter += 1
                print("Counter:", counter)

        for i in range(len(nums) -1, len(nums)//2, -1):
            print("nums[i]", nums[i], " nums[i-1]", nums[i-1])
            if nums[i] < nums[i-1]:
                my_hashmap[i] = nums[i]
            else:
                counter += 1
                print("Counter:", counter)
        return counter


sol = Solution()
result = sol.minimumMountainRemovals([4,3,2,1,1,2,3,1])
print("Result:", result)
