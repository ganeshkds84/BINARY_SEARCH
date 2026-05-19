class Solution:
    def insert(self,nums,target):
        l=0
        u=len(nums)-1
        ans=len(nums)
        while l<=u:
            mid=(l+u)//2
            if nums[mid]>=target:
                ans=mid
                u=mid-1
            else:
                l=mid+1
        return ans
    
if __name__=="__main__":
    nums=list(map(int,input("Enter ditinct numbers in asc order:").split(',')))
    target=int(input('Enter target value:'))
    obj=Solution()
    print(obj.insert(nums,target))