class Solution:
    def shipWithinDays(self,weights,days):
        l,u=max(weights),sum(weights)
        ans=sum(weights)
        while l<=u:
            mid=(l+u)//2
            days_needed=1
            count=0
            for i in range(len(weights)):
                #count+=weights[i]
                if count+weights[i]>mid:
                    days_needed+=1
                    count=weights[i]
                else:
                    count+=weights[i]
            if days_needed<=days:
                ans=mid
                u=mid-1
            else:
                l=mid+1
                
        return ans
    
if __name__=='__main__':
    weights=list(map(int,input('Enter the weights of the days:').split()))
    days=int(input('Enter the number of days:'))
    Ashu=Solution()
    print(Ashu.shipWithinDays(weights,days))