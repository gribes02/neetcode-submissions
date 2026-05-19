class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_counter = 0
        prod = 1
        output = [0] * len(nums)
        
        for num in nums:
            if num: prod = prod * num
            
            else: zero_counter += 1
        
        for i, num in enumerate(nums):
            if zero_counter > 1: return output

            if zero_counter: 
                if not num: 
                    output[i] = prod
                    return output
            
            else: 
                output[i] = prod // num

        return output


                

                

                    
