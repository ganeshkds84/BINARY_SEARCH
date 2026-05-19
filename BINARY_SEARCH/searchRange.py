class Solution:
    def searchRange(self,nums,target):
        l,u=0,len(nums)-1
        f,c=-1,-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]<=target:
                if nums[mid]==target:
                    c=mid
                l=mid+1
            else:
                u=mid-1
        l,u=0,len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    f=mid
                u=mid-1
            else:
                l=mid+1
        return f,c

if __name__=='__main__':
    
    nums=list(map(int,input('Enter numbers in asc order:').split(',')))
    target=int(input('Enter the target value:'))
    obj=Solution()
    print(obj.searchRange(nums,target))
    