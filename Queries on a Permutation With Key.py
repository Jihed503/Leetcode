class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        l=[i+1 for i in range(m)]
        lo=[]
        for i in range(len(queries)):
            lo.append(l.index(queries[i]))
            l.remove(queries[i])
            li=[]
            li.append(queries[i])
            l=li+l
        return lo
        