class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq={}
        for i in nums1:
            freq[i]=freq.get(i,0)+1
        
        res=[]
        for i in nums2:
            count=freq.get(i,0)
            if count==0:
                continue
            res.append(i)
            freq[i]=count-1

        return res
        
        