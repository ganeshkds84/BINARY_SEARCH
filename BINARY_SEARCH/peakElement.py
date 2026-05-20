class Ashu:
    def peakEle(self,nums):
        l,u=0,len(nums)-1
        while l<u:
            mid=(l+u)//2
            if nums[mid]>nums[mid+1]:
                u=mid
            else:
                l=mid+1
                
        return l
    
if __name__=='__main__':
    nums=list(map(int,input('Enter numbers:').split()))
    ganesh=Ashu()
    print(ganesh.peakEle(nums))