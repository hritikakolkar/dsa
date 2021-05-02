#taking user input ot sort a list using merge sort:
#userIpLst=list(map(int,input().split()))
#Cool
#Let's get started
def merge(left_lst,right_lst):
    final_lst=[]
    li,ri=0,0
    while li<len(left_lst):
        if left_lst[li]>right_lst[ri]:
            final_lst.append(right_lst[ri])
            ri+=1
        else:
            final_lst.append(left_lst[li])
            li+=1
    return final_lst
"""
def merge_sort(userIpLst,start=0,end=len(userIpLst)):
    mid=(start + end)//2
    ans=merge(merge_sort(userIpLst,start,mid-1),merge_sort(userIpLst,mid,end))
    return ans
"""
print(merge([1,2,3,4],[4,63,24,2]))