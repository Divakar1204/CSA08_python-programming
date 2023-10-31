test_str = "The cat on the wall"
 

print("The original string is : " + test_str)
 

res = []
temp = ''
flag = 1
for ele in test_str:
    if ele == ' ' and flag:
        res.append(temp)
        temp = ''
        flag = 0
    else :
        temp += ele
res.append(temp)
                     
 
print("Initial word separated list : " + str(res))
