#taking input of values in array and searching for given value in array using linear search technique:
userInput=list(map(int,input().split()))
value=int(input())
def linear_search(lst,val):
    for idx in range(len(lst)):
        if userInput[idx]==val:
            return idx
index = linear_search(userInput,value)
print(f"value :- {value} is at index :- {index}")