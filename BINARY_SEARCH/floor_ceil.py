class Solution:
    def floorCeil(self,nums,target):
        l=0
        u=len(nums)-1
        f,c=-1,-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]>=target:
                c=nums[mid]
                u=mid-1
            else:
                l=mid+1
        l,u=0,len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]<=target:
                l=mid+1
                f=nums[mid]
            else:
                u=mid-1
        return f,c
    
if __name__=="__main__":
    nums=list(map(int,input('Enter numbers in asc order:').split(',')))
    target=int(input('Enter target value:'))
    obj=Solution()
    print(obj.floorCeil(nums,target))
    