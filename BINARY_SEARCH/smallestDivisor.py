class Solution:
    def Ashu(self,nums,threshold):
        l,u=1,max(nums)
        ans=1
        while l<=u:
            mid=(l+u)//2
            count=0
            for i in range(len(nums)):
                count+=(nums[i]+mid-1)//mid
            if count<=threshold:
                ans=mid
                u=mid-1
            else:
                l=mid+1
                
        return ans
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    threshold=int(input('Enter the limit:'))
    ganesh=Solution()
    print(ganesh.Ashu(nums,threshold))