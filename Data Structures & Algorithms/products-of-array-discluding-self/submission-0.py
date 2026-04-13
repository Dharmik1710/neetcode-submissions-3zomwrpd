class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zeros = 0
        for num in nums:
            if num:
                product = product * num
            else:
                zeros += 1
        for num in nums:
            if num == 0:
                if zeros == 1:
                    result.append(product)
                else:
                    result.append(0)
            else:
                if zeros > 0:
                    result.append(0)
                else:
                    result.append(product//num)
        return result
        