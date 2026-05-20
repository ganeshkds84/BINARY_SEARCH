class Ashu:
    def search(self,nums,target):
        l=0
        u=len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]==target:
                return True
            if nums[l]==nums[mid]==nums[u]:
                l+=1
                u-=1
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    u=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[u]:
                    l=mid+1
                else:
                    u=mid-1
        return False

if __name__=='__main__':
    nums=list(map(int,input('Enter numbers:').split()))
    target=int(input('Enter the target value'))
    ganesh=Ashu()
    print(ganesh.search(nums,target))
    