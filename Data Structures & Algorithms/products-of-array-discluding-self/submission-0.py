class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        counter = 0
        output = []
        
        for i, num in enumerate(nums):
            prod = 1
            for j, num_2 in enumerate(nums):
                if j != i:
                    prod = prod * num_2
            output.append(prod)

        return output
                

                

                    
