class Solution:
    
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        elif len(s)==k:
            return True
        else:
            d={}
            for c in s:
                if c not in d:
                    d[c]=1
                else:
                    d[c]+=1
            odd=0
            for i in d.values():
                if i%2!=0:
                    odd+=1
            return odd<=k