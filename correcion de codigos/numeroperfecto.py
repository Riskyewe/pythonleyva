num1=0
while num1 <=1000:
    i=1
    sum=0
    while i<num1:
        if num1 % i==0:
            sum+=i
if num1==sum:
    print(num1," Es perfecto")
num1+=1
