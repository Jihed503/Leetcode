class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            ch=str(i)
            s=0
            for j in ch:
                s+=int(j)
            if s in d:
                d[s]+=1
            else: d[s]=1
        maxi=0
        p=0
        for i,j in d.items():
            if j>maxi: 
                p=1
                maxi=j
            elif j==maxi: 
                p+=1
                
                
        return p