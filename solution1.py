import math
num =4  
x = 1  
if num < 0:  
   print("Sorry try with different no")  
elif num == 0:  
   print("try with different no") 
elif num>=1000000:
    print("out of range")
else:  
   for i in range(1,num + 1):  
       x = x*i  
per_no = x/num
sum=0
for i in range(num):
    no=per_no-1
    sum=sum+no
    per_no-=1
    
r=x-sum
final=r-1
print(math.floor(final))
