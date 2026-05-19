class Solution:
    def countOccurence(self,nums,target):
        l,u=0,len(nums)-1
        f,c=0,0
        while l<=u:
            mid=(l+u)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    f=mid
                u=mid-1
            else:
                l=mid+1
        l,u=0,len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]<=target:
                if nums[mid]==target:
                    c=mid
                l=mid+1
            else:
                u=mid-1
        if f==0 and c==0:
            return 0
        else:
            return c-f+1
        
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers in asc order:').split()))
    target=int(input('Enter the target value:'))
    obj=Solution()
    print(obj.countOccurence(nums,target))