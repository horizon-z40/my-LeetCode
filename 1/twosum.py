# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        for i in xrange(length-1):
          for j in xrange(i+1,length):
            if nums[i]+nums[j]==target:
              return [i,j]
            
if __name__=='__main__':
  a=Solution()
  nums=[1,3,5,7,9,11,13]
  tar=22
  print a.twoSum(nums,tar)
  






