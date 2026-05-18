class Solution:
    def lower(self,nums,x):
        l=0
        u=len(nums)-1
        ans=len(nums)
        while l<=u:
            mid=(l+u)//2
            if nums[mid]>=x:
                ans=mid
                u=mid-1
            else:
                l=mid+1
        return ans
    
if __name__=="__main__":
    nums=list(map(int,input('Enter numbers in asc order:').split()))
    x=int(input("Enter target value:"))
    obj=Solution()
    print(obj.lower(nums,x))