def foctorial(n):
    if n==1:
            return n
    else:
          return n*foctorial(n-1)
n=int(input("enter a no.: "))
if n<0:
      print("factorial does not exist for negative numbers")
elif n==0:
      print("factorial of 0 is 1")  
else:
      print("factorial of",n,"is",foctorial(n))