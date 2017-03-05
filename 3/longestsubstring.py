'''
花的时间太多了，再练习

'''
#==============================================================================
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         size=len(s)
#         maxlength=0
#         length=0
#         table=[]
#         i=0
#         while i<size:
#             c=s[i]
#             if c in table:
#                 
#                 i=i-(length-table.index(c))+1
#                 table=[]
#                 table.append(s[i])
#                 length=1
#             else:
#                 table.append(c)
#                 length=length+1
#                 if length>maxlength:
#                     maxlength=length
# #            print table,length,i
#             i=i+1
#         return maxlength
#==============================================================================
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        size=len(s)
        maxlength=0
        length=0
        table=[]
        i=0
        while i<size:
            c=s[i]
            if c in table:
                weizhi=table.index(c)
                table=table[weizhi+1:]
                table.append(c)
                length=len(table)
            else:
                table.append(c)
                length=length+1
                if length>maxlength:
                    maxlength=length
            
            i=i+1
            print table,length,i
        return maxlength
        
if __name__=='__main__':
    test="bbbbb"    
    a=Solution()
    num=a.lengthOfLongestSubstring(test)