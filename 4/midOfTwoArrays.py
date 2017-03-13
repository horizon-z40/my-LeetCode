'''
归并排序法

'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1=len(nums1)
        l2=len(nums2)
        if l1==0:
            l1_flag=False
        else:
            l1_flag=True
        if l2==0:
            l2_flag=False
        else:
            l2_flag=True
        nums=[]
        
        l=l1+l2
        for i in xrange(l):
            if l1_flag and l2_flag:
                if nums1[0]<nums2[0]:
                    nums.append(nums1.pop(0))
                    l1-=1
                    if l1==0:
                      l1_flag=False
                else:
                    nums.append(nums2.pop(0))
                    l2-=1
                    if l2==0:
                      l2_flag=False
            elif l1_flag==False:
                nums.extend(nums2)
                break
            elif l2_flag==False:
                nums.extend(nums1)
                break
            
        if l%2==0:
            ret=(nums[l/2-1]+nums[l/2])/2.0
        else:
            ret=nums[(l-1)/2]
        return ret
        
if __name__=='__main__':
    nums1 = [1, 3]
    nums2 = [2]
    a=Solution()
    ans=a.findMedianSortedArrays(nums1,nums2)
    