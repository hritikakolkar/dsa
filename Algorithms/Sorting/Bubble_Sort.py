#Taking input from user to sort using bubble sorting technique. 
user_lst=list(map(int,input().split()))
#Let's get started.
#length of user inputed array.
len_user_lst=len(user_lst)
for index in range( len_user_lst ):
    for indexless in range( len_user_lst - index - 1 ):
        if user_lst[indexless]>user_lst[indexless+1]:
            user_lst[indexless],user_lst[indexless+1]=user_lst[indexless+1],user_lst[indexless]
print(user_lst)
