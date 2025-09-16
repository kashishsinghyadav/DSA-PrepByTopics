

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            while len(stack) >= 2:
                v1 = stack.pop()
                v2 = stack.pop()
                gcd = math.gcd(v1, v2)
                
                if gcd > 1:
                    lcm = (v1 * v2) // gcd
                    stack.append(lcm) 
                else:
                    stack.append(v2)
                    stack.append(v1)
                    break  
        
        return stack
