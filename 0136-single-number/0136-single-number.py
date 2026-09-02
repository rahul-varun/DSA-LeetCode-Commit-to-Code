class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map={}
        for i in nums:
            if i not in map:
                map[i]=0
            map[i]=map[i]+1

        for i in map:
            if map[i]==1:
                return i
        
        return -1
        
        