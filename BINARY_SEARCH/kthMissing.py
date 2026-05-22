class Ashu:
    def KthMissing(self,nums,k):
        l,u=0,len(nums)-1
        while l<=u:
            mid=(l+u)//2
            missing=nums[mid]-(mid+1)
            if missing<k:
                l=mid+1
            else:
                u=mid-1
        return l+k
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    k=int(input('Enter the missing number:'))
    ganesh=Ashu()
    print(ganesh.KthMissing(nums,k))