# Brute Force
# Space Complexity: O(1)
# Time Complexity: O(n^2)

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

#Hash Map
# Space Complexity: O(n)
# Time Complexity: O(n)
# Insight: don't search for the partner, compute it (target - num).
#          Dict maps value -> index, so the lookup returns a position
#          Check BEFORE inserting, or an element pairs with itself

def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        pair = target - nums[i]
        if pair in seen:
            return [i, seen[pair]]
        seen[nums[i]] = i
    return []
