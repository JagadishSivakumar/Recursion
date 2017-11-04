#Factorial of n numbers using Recursion
def fact(n):
    if(n<=1):
        return(1)
    else:
        return(n*fact(n-1))
n=int(input("Enter the Value"))
print("Factorial of the number is" ,fact)
