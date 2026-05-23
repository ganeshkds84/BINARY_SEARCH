class Ashu:
    def splitArray(self,nums,k):
        if len(nums)<k:
            return -1
        l,u=max(nums),sum(nums)
        while l<=u:
            mid=(l+u)//2
            current=0
            split=1
            for num in nums:
                if current+num>mid:
                    split+=1
                    current=num
                else:
                    current+=num
            if split<=k:
                ans=mid
                u=mid-1
            else:
                l=mid+1
                
        return ans    
    
if __name__=='__main__':
    nums=list(map(int,input('Enter numbers:').split()))
    splits=int(input('Enter number of splits:'))
    ganesh=Ashu()
    print(ganesh.splitArray(nums,splits))
    