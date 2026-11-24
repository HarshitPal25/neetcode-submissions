class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in present:
                return [present[required],i]
            present[nums[i]] = i