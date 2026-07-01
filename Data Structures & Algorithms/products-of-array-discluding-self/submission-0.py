from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        #LessComplicated
        # result = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if j!=i:
        #             prod *= nums[j]
        #     result.append(prod)
        # return result
        
        
        # Myfirstapproach    
        #  result = []
        #  for i in range(len(nums)):
        #     prod1 = 1
        #     prod2 = 1
        #     for j in range(i +1, len(nums)):
        #         prod1 *= nums[j]
        #     for k in range(0, i):
        #         prod2 *= nums[k]
        #     prod = prod1 * prod2
        #     result.append(prod)
        #  return result
