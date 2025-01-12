class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2!=0:
            return False

        ostack = []
        ocstack = []
        n=len(s)

        for i in range(n):
            if locked[i] == '0':
                ocstack.append(i)
            elif s[i] == '(':
                ostack.append(i)
            elif s[i] == ')':
                if ostack:
                    ostack.pop()
                elif ocstack:
                    ocstack.pop()
                else:
                    return False

        while ostack and ocstack and ostack[-1] < ocstack[-1]:
            ostack.pop()
            ocstack.pop()

        return not ostack

        
