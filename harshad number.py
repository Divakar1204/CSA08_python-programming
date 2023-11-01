num=int(input("enter the number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit
    temp=temp//10
    if num%sum==0:
        print("harshad number")
    else:
            print("not a harshad number")
