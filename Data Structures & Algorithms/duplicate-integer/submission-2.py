class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vector = []

        for num in nums:
            if num in vector:
                return True
            else:
                vector.append(num)
            
        return False
        