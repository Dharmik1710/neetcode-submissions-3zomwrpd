import heapq

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures):
            # if not stack:
            #     stack.append(i)
            #     i+=1
            #     continue
            
            # if temperatures[i] <= temperatures[stack[-1]]:
            #     stack.append(i)
            #     i+=1
            #     continue
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            
            stack.append(i)
            i += 1
        return res


                
            

