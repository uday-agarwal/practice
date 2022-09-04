# Rob houses such that two adjacent houses cannot be robbed 
# and loot is to be maximised.
# [2, 1, 1, 2] => 4

class Solution:
    def rob(self, nums) -> int:
        loot = [0] * len(nums)
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        loot[0] = nums[0]
        loot[1] = max(nums[0], nums[1])
        
        for house in range (2, len(nums)):
            loot[house] = max(loot[house - 1], loot[house - 2] + nums[house])
        
        return loot[len(nums) - 1]

s = Solution()
print(s.rob([2, 1, 1, 2]))
