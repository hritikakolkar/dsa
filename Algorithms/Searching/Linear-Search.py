#taking input of values in array and searching for given value in array using linear search technique:
userIp=list(map(int,input().split()))
value=int(input())
def linear_search(lst,val):
    for ele_idx in range(len(lst)):
        if userIp[ele_idx]==val:
            return ele_idx
index=linear_search(userIp,value)
print(index)