# Brute Force
# Space Complexity O(1)
# Time Complexity O(n^2)

def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    return True
        return False



# Hash Set
# Space Complexity O(n)
# Time Complexity O(n)

def containsDuplicate(self, nums: list[int]) -> bool:
    seen = set() # Initialize an empty hash set to store seen values.
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False



