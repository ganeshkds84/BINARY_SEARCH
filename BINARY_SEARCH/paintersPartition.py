class Ashu:
    def paint(self,a,b,c):
        l,u=max(c),sum(c)
        ans=u
        while l<=u:
            mid=(l+u)//2
            current=0
            splits=1
            for num in c:
                if current+num>mid:
                    splits+=1
                    current=num
                else:
                    current+=num
            if splits<=a:
                ans=mid
                u=mid-1
            else:
                l=mid+1
        final=ans*b
        return final
    
if __name__=='__main__':
    a=int(input('Enter number of painters:'))
    b=int(input('Cost for painting each unit:'))
    c=list(map(int,input('Enter the blocks to be painted:').split()))
    ganesh=Ashu()
    print(ganesh.paint(a,b,c))