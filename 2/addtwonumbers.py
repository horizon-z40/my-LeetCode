class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_ListNode(x):
    print '--------------'
    while x:
      print x.val
      x=x.next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
#        res=ListNode(0)
#        while l1||l2:
        total=l1.val+l2.val
        num=total%10
        jinwei=total/10
        res=ListNode(num)
        tmp=res
        tmp1=l1.next
        tmp2=l2.next
        while tmp1!=None or tmp2!=None or jinwei==1:
            total=0
            if tmp1!=None:
                total=total+tmp1.val
            if tmp2!=None:
                total=total+tmp2.val
            total=total+jinwei
            jinwei=0
            num=total%10
            jinwei=total/10
            tmp.next=ListNode(num)
            tmp=tmp.next
            if tmp1!=None:
                tmp1=tmp1.next
            if tmp2!=None:
                tmp2=tmp2.next
        return res

if __name__=='__main__':
    num1=[5]
    a=ListNode(num1[0])
    tmp=a
    for i in xrange(1,len(num1)):
      tmp.next=ListNode(num1[i])
      tmp=tmp.next
    
    num1=[5]
    b=ListNode(num1[0])
    tmp=b
    for i in xrange(1,len(num1)):
      tmp.next=ListNode(num1[i])
      tmp=tmp.next
    xx=Solution()    
    c=xx.addTwoNumbers(a,b)
    
    print_ListNode(a)
    print_ListNode(b)    
    print_ListNode(c)