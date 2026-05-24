class Ashu:
    def search(self,mat):
        final=-1
        max_ones=0
        for i in range(len(mat))    :
            l,u=0,len(mat[i])-1
            ans=len(mat[i])
            while l<=u:
                mid=(l+u)//2
                if mat[i][mid]==1:
                    ans=mid
                    u=mid-1
                else:
                    l=mid+1
            current=len(mat[i])-ans
            if current>max_ones:
                max_ones=current
                final=i
        return final
    
if __name__=='__main__':
    mat=[[0,1,1],[0,0,1],[1,1,1]]
    ganesh=Ashu()
    print(ganesh.search(mat))
    